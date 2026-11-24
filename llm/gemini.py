import google.generativeai as genai

from config import config


class GeminiClient:

    def __init__(self):

        genai.configure(
            api_key=config.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            config.GEMINI_MODEL
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.model.generate_content(
            prompt
        )

        return response.text