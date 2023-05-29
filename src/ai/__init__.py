from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import faiss
from openai.error import RateLimitError
from pydantic import BaseSettings, Field

from src.config import config_instance


class ModelSelections(BaseSettings):
    text_davinci: str = Field(default='text-davinci-003')
    gpt_4: str = Field(default='gpt-4')
    gpt_4_revision: str = Field(default='gpt-4-0314')
    gpt_35_turbo: str = Field(default='gpt-3.5-turbo-0301')


class AIEngine:
    """

    """

    def __init__(self, api_key: str = config_instance().openai_api_key, model: str = ModelSelections.text_davinci,
                 use_tokens: int = 10):
        self._engine = model
        self._open_ai = openai
        self._open_ai.api_key = api_key
        self._use_tokens = use_tokens
    def load_chain(self, ):
    def completion(self, _prompt: str) -> str | None:
        """
        **completion**

        :param _prompt:
        :return:
        """
        try:
            prompt_response = self._open_ai.Completion.create(
                engine=self._engine,
                prompt=_prompt,
                max_tokens=self._use_tokens
            )
            return prompt_response.choices[0].text.strip()
        except RateLimitError as e:
            return None

