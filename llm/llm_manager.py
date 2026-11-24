from llm.gemini import GeminiClient
from llm.groq import GroqClient

from utils.logger import logger


class LLMManager:

    def __init__(self):

        self.gemini = GeminiClient()

        self.groq = GroqClient()

    def generate(
        self,
        prompt: str
    ):

        try:

            logger.info(
                "Using Gemini..."
            )

            response = self.gemini.generate(
                prompt
            )

            return response, "Gemini"

        except Exception as e:

            logger.error(
                f"Gemini Failed : {e}"
            )

            logger.info(
                "Switching to Groq..."
            )

            response = self.groq.generate(
                prompt
            )

            return response, "Groq"