import os
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Settings:
    api_key: str = field(repr=False)
    model: str

def load_settings() -> Settings:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model = os.getenv("OPENAI_MODEL", "").strip()

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing.")
    if not model:
        raise ValueError("OPENAI_MODEL is missing.")

    return Settings(api_key=api_key, model=model)