from typing import Protocol
from openai import OpenAI
from novacommerce.config import Settings
from novacommerce.schemas import LLMAnswer

class LLMProvider(Protocol):
    def generate(self, instructions: str, input_text: str) -> LLMAnswer:
        ...

    def close(self) -> None:
        ...

class OpenAIProvider:
    def __init__(self, settings: Settings) -> None:
        self._model = settings.model
        self._client = OpenAI(
            api_key=settings.api_key,
            timeout=30,
            max_retries=0
        )

    def generate(self, instructions: str, input_text: str) -> LLMAnswer:
        if not input_text.strip():
            raise ValueError("Input text must not be empty.")

        response = self._client.responses.parse(
            model=self._model,
            instructions=instructions,
            input=input_text,
            text_format=LLMAnswer,
            max_output_tokens=1024,
            store=False
        )

        if response.status != "completed":
            raise RuntimeError(f"Model response was {response.status}.")

        answer = response.output_parsed
        if answer is None:
            raise RuntimeError("The model did not return a validated answer.")

        return answer

    def close(self) -> None:
        self._client.close()