from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer



app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_sentiment(input: TextInput):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(input.text)
    
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.10:
        sentiment = "Negative"
    elif compound_score <= 1.00:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return {
        "sentiment": sentiment,
        "scores": sentiment_scores
    }
