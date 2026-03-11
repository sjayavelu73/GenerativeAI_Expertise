from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    text: str
    max_length: int


class SummaryResponse(BaseModel):
    summary: str


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float
    explanation: str

