from fastapi import FastAPI
from datetime import datetime
import json

from .schemas import *
from .llm import call_llm
from .prompts import summarize_prompts, sentiment_prompts

app = FastAPI()

app = FastAPI(
    title="FastAPI LLM API",
    description="Endpoints for text summarization and sentiment analysis",
    version="1.0.0",
)

# -----------------------------
# Pydantic models
# -----------------------------
class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 60  # default max_length

class SentimentRequest(BaseModel):
    text: str

# -----------------------------
# Root route
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI. FastAPI LLM API running",
        "endpoints": ["/health", "/summarize", "/analyze-sentiment"],
        "docs": "/docs",
        "redoc": "/redoc"
    }

# -----------------------------
# Health check
# -----------------------------
@app.get("/health")
def health_check():
    from datetime import datetime
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.post("/summarize", response_model=SummaryResponse)
async def summarize(req: SummarizeRequest):

    prompt = summarize_prompts["few_shot"].format(
        text=req.text,
        max_length=req.max_length
    )

    result = await call_llm(prompt)

    return {"summary": result}


@app.post("/analyze-sentiment", response_model=SentimentResponse)
async def sentiment(req: SentimentRequest):

    prompt = sentiment_prompts["few_shot"].format(text=req.text)

    result = await call_llm(prompt,json_mode=True)

    data = json.loads(result)

    return data

