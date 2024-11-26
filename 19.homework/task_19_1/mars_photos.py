import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)
data = response.json()

if 'photos' in data and len(data['photos']) > 0:
    print(f"Знайдено {len(data['photos'])} фотографій.")

    if not os.path.exists('mars_photos'):
        os.makedirs('mars_photos')

    for i, photo in enumerate(data['photos']):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content

        with open(f'mars_photos/mars_photo{i + 1}.jpg', 'wb') as f:
            f.write(img_data)
        print(f"Збережено фото mars_photo{i + 1}.jpg")
else:
    print("Фотографії не знайдені.")