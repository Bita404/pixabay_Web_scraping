import requests


headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://pixabay.com/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://media.istockphoto.com/id/1411644878/video/wave-sea-turquoise-rolling-slow-crash-rocks-pattern-coastline-sunset-paradise-island-4k-copy.jpg?b=1&s=640x640&k=20&c=Z206SOtYYkahOLsNUJyqsqPHB_ou6v4Hjx03u7kFozk=',
    headers=headers,
)
print(response.content)
data = response.content
with open("videocover.jpg", "wb") as img:
    img.write(data)
print(response)
