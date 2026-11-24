from groq import Groq

from config import config


class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=config.GROQ_API_KEY
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.client.chat.completions.create(

            model=config.GROQ_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content