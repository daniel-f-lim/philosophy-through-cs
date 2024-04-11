from io import BytesIO
from PIL import Image
import requests

def open_git_image(filename):
    image_url = f"https://raw.githubusercontent.com/daniel-f-lim/philosophy-through-cs/main/{filename}"
    response = requests.get(image_url)
    return Image.open(BytesIO(response.content))