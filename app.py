from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional
import requests
import os

app = FastAPI(title="NewsFlash API")

# Replace with your actual NewsAPI key
NEWS_API_KEY = "62f425894ac84ca482200c1a499e6d4c"

def fetch_news(location: str, api_key: str):
    url = f"https://newsapi.org/v2/everything?q={location}&sortBy=popularity&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return [
            {
                "title": article.get("title"),
                "source": article.get("source", {}).get("name") if article.get("source") else "Unknown",
                "url": article.get("url"),
                "description": article.get("description")
            }
            for article in articles[:5]
        ]
    elif response.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get("/news")
def get_news(location: str = Query(..., min_length=2)):
    try:
        articles = fetch_news(location, NEWS_API_KEY)
        if articles:
            return JSONResponse(content={"location": location, "articles": articles, "status": "success"})
        else:
            return JSONResponse(content={"location": location, "articles": [], "message": "No news articles found for this location.", "status": "empty"})
    except HTTPException as e:
        raise e

app.mount("/", StaticFiles(directory=".", html=True), name="static")
