# NEWSFLASH - News App

A modern news search application built with FastAPI and vanilla JavaScript.

## Features

- 🔍 Search news by location or topic
- 📍 Quick access to popular cities (New York, London, Tokyo, Paris)
- 🎯 Trending topics (#Technology, #Climate, #Sports)
- 🎨 Beautiful dark theme UI with smooth animations
- ⚡ Real-time news fetching from NewsAPI
- 📱 Responsive mobile-first design

## Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Update API Key (Optional):**
   - Open `app.py` and replace `NEWS_API_KEY` with your own from [newsapi.org](https://newsapi.org)

## Running the App

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Then open your browser and navigate to:
```
http://localhost:8000
```

## Project Structure

- `app.py` - FastAPI backend with news fetching endpoint
- `index.html` - Frontend UI with embedded CSS and JavaScript
- `news.py` - Standalone news fetching utility
- `requirements.txt` - Python dependencies

## How It Works

1. **Frontend** - User enters a location or clicks on cities/topics
2. **JavaScript** - Captures user input and sends request to `/news` endpoint
3. **Backend** - FastAPI fetches news from NewsAPI and returns results
4. **Frontend** - Displays results with automatic numbering and formatting
5. **Error Handling** - Shows appropriate error/empty states

## API Endpoint

### GET /news
Fetch news articles for a specific location

**Query Parameters:**
- `location` (required, min length: 2) - Location or topic to search for

**Response:**
```json
{
  "location": "London",
  "articles": [
    {
      "title": "Article Title",
      "source": "Source Name",
      "url": "https://...",
      "description": "..."
    }
  ],
  "status": "success"
}
```

## Keyboard Shortcuts

- **Enter** - Search for news from the search bar
- **Click** - City buttons or trending topics for quick search

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Notes

- The app displays the top 5 most popular articles
- Articles are sorted by popularity
- Links open in a new tab
- Empty state is shown when no articles are found
