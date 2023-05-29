from fastapi import APIRouter
from src.main.main import ai_engine

prompt_api = APIRouter()


@prompt_api.post("/process-prompt")
def process_prompt(prompt: str):
    return ai_engine.completion(_prompt=prompt)


