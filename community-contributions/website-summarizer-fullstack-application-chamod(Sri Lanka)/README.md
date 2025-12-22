# Website Summarizer App

A React application that connects to your Python web scraper to generate AI-powered summaries of websites.

## Project Structure

```
practice/
├── api.py                      # Flask API backend
├── webScraper.py              # Web scraping functions
├── .env                       # Environment variables (OPENAI_API_KEY)
└── website-summarizer/        # React frontend
    ├── src/
    │   ├── App.js             # Main React component
    │   └── App.css            # Styles
    └── package.json
```

## Setup Instructions

### 1. Backend Setup (Flask API)

Make sure you have all required Python packages installed:

```bash
pip install flask flask-cors python-dotenv beautifulsoup4 requests openai
```

Your `.env` file should contain:
```
OPENAI_API_KEY=sk-proj-your-api-key-here
```

### 2. Frontend Setup (React)

The React app has already been created. Dependencies are installed.

## Running the Application

### Step 1: Start the Flask API Server

Open a terminal and run:

```bash
cd "d:\AI Course\practice"
python api.py
```

The API will start on `http://localhost:5000`

You should see:
```
Starting Flask API server...
API will be available at http://localhost:5000
```

### Step 2: Start the React Development Server

Open a **new terminal** and run:

```bash
cd "d:\AI Course\practice\website-summarizer"
npm start
```

The React app will open automatically in your browser at `http://localhost:3000`

## How to Use

1. Make sure both servers are running (Flask on port 5000, React on port 3000)
2. Open your browser to `http://localhost:3000`
3. Enter a website URL (e.g., `https://edwarddonner.com`)
4. Click "Summarize"
5. Wait for the AI to generate a snarky summary!

## API Endpoints

### POST /api/summarize
Summarize a website

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "success": true,
  "url": "https://example.com",
  "summary": "Markdown formatted summary..."
}
```

### GET /api/health
Health check endpoint

**Response:**
```json
{
  "status": "ok"
}
```

## Troubleshooting

### "Failed to connect to the API"
- Make sure the Flask server is running on port 5000
- Check that you're not getting any errors in the Flask terminal

### "No API key found"
- Make sure your `.env` file exists in the `practice` folder
- Verify your `OPENAI_API_KEY` is set correctly

### CORS errors
- The Flask-CORS package should handle this automatically
- If you still see CORS errors, restart the Flask server

### Port already in use
- If port 5000 is already in use, you can change it in `api.py`:
  ```python
  app.run(debug=True, port=5001)  # Change to any available port
  ```
- Then update the React app's fetch URL in `App.js` to match

## Features

- ✅ Beautiful, responsive UI
- ✅ Real-time website summarization using OpenAI GPT-4o-mini
- ✅ Markdown rendering for formatted summaries
- ✅ Error handling and loading states
- ✅ CORS enabled for local development
- ✅ Snarky, humorous summaries!

## Tech Stack

**Backend:**
- Flask (Python web framework)
- BeautifulSoup4 (Web scraping)
- OpenAI API (AI summaries)
- Flask-CORS (Cross-origin support)

**Frontend:**
- React (UI framework)
- react-markdown (Markdown rendering)
- Modern CSS with gradients and animations
