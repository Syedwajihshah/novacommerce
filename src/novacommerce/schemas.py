from pydantic import BaseModel, ConfigDict

class LLMAnswer(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    answer: str
    needs_more_information: bool