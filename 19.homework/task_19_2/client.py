import requests

def upload_image(image_path):
    url = 'http://127.0.0.1:8080/upload'
    with open(image_path, 'rb') as img:
        files = {'image': img}
        response = requests.post(url, files=files)
        if response.status_code == 201:
            image_url = response.json()['image_url']
            print('Зображення завантажено успішно:', image_url)
            return image_url
        else:
            print('Помилка при завантаженні зображення:', response.json())
            return None

def get_image(filename):
    url = f'http://127.0.0.1:8080/image/{filename}'
    headers = {'Content-Type': 'text'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('URL зображення:', response.json())
    else:
        print('Помилка при отриманні зображення:', response.json())

def delete_image(filename):
    url = f'http://127.0.0.1:8080/delete/{filename}'
    response = requests.delete(url)
    if response.status_code == 200:
        print('Зображення видалено:', response.json())
    else:
        print('Помилка при видаленні зображення:', response.json())

if __name__ == '__main__':
    image_url = upload_image('sample_image.jpg')
    if image_url:
        filename = image_url.split('/')[-1]
        get_image(filename)
        delete_image(filename)