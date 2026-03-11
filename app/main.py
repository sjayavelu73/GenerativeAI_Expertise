from fastapi import FastAPI
from datetime import datetime
import json

from .schemas import *
from .llm import call_llm
from .prompts import summarize_prompts, sentiment_prompts

app = FastAPI()


@app.get("/health")
def health():

    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
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

