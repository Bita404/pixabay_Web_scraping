import requests
import csv
import concurrent.futures

def download(image_data):
    url = image_data["URL"]
    image_response = requests.get(url)
    with open(f"image_{image_data['id']}.jpg", "wb") as file:
        file.write(image_response.content)
    print(f"Downloaded image {image_data['id']}/{image_data['num_images']}")

def download_from_pixabay( num_images, api_key):
    base_url = "https://pixabay.com/api/"
    params = {
        "key": api_key,
        "image_type": "photo",
        "per_page": num_images
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    image_data = []
    for i, image in enumerate(data["hits"]):
        tags = image["tags"]
        creator_name = image["user"]
        image_url = image["largeImageURL"]
        title = image["userImageURL"]
        resolution = f"{image['imageWidth']}x{image['imageHeight']}"
        image_data.append({
            "id": i + 1,
            "num_images": num_images,
            "Tags": tags,
            "Creator": creator_name,
            "URL": image_url,
            "Title": title,
            "Resolution": resolution
        })

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download, image_data)

    keys = image_data[0].keys()
    with open("pixabay_images.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(image_data)

    print("Image downloading and CSV creation completed.")



num_images = 10
api_key = "41944678-39b6d49cec7fd580a769da914"
download_from_pixabay( num_images, api_key)
