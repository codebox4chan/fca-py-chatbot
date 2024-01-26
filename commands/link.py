import os
import requests
from io import BytesIO

def download_image(url, save_directory, filename):
    response = requests.get(url)
    if response.status_code == 200:
        save_path = os.path.join(save_directory, filename)
        os.makedirs(save_directory, exist_ok=True)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return save_path
    return None

def command(input_value, thread_userid=None):
    config = {"name": "link", "version": "1.0.0", "description": "sends image attach", "credits": "Kenneth Panio", "cooldown": "1"}
    
    if input_value == "__config__":
        return config
    
    if input_value.startswith(config['name'] + ' ') or input_value == config['name']: 
        image_url = 'https://i.imgur.com/xU5YB4e.gif'
        save_directory = './imgCache'
        image_filename = 'img.gif'
        
        saved_image_path = download_image(image_url, save_directory, image_filename)
        
        if saved_image_path:
            with open(saved_image_path, 'rb') as file:
                image_data = BytesIO(file.read())
            os.remove(saved_image_path)
            return {'messages': ["Kenneth Panio"], 'image': [image_data]}
        
        return {'messages': ["Failed to download image."]}
    
    return {'messages': [f"Default option in {config['name']}: {config['description']}"]}
