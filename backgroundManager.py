import requests
from pprint import pprint
from random import randint, choice
import os

class BackgroundManager:

    def __init__(self):

        self.HEADER = {
            "Authorization": os.environ["BACKGROUND_IMAGE_KEY"]
        }

        self.QUERY = "Celebration"

    def get_image(self):
        parameters = {
            "query": self.QUERY,
            "orientation": "landscape",
            "size": "large",
            "page": str(randint(1, 15))
        }

        response = requests.get(url="https://api.pexels.com/v1/search", headers=self.HEADER, params=parameters)
        photos = response.json()['photos']
        random_photo = choice(photos)["src"]["landscape"]
        print(random_photo)
        response.raise_for_status()

        return random_photo
