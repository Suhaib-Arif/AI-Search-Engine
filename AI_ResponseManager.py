import openai
import os

class AI_Manager:

    def __init__(self):
        self.ai_api_key = os.environ["AI API KEY"]
        openai.api_key = self.ai_api_key
        self.model = "gpt-3.5-turbo"
        self.role = "assistant"

    def get_reply(self,query):

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": self.role,
                    "content": query
                 }
            ]
        )


        reply = response["choices"][0]["message"]["content"]

        return reply

    def generate_image(self,description):

        response = openai.Image.create(
            prompt=description,
            n=1,
            size="1024x1024"
        )

        image = response['data'][0]['url']

        return image