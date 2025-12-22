from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from webScraper import fetch_website_contents
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize OpenAI client
openai_client = OpenAI()

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

def summarize_website(url):
    """Fetch website content and generate summary using OpenAI"""
    try:
        website = fetch_website_contents(url)
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_for(website)
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error summarizing website: {str(e)}")

@app.route('/api/summarize', methods=['POST'])
def summarize():
    """API endpoint to summarize a website"""
    try:
        data = request.get_json()
        
        if not data or 'url' not in data:
            return jsonify({'error': 'URL is required'}), 400
        
        url = data['url']
        
        # Validate URL format
        if not url.startswith(('http://', 'https://')):
            return jsonify({'error': 'Invalid URL format. Must start with http:// or https://'}), 400
        
        # Get summary
        summary = summarize_website(url)
        
        return jsonify({
            'success': True,
            'url': url,
            'summary': summary
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("ERROR: No API key found. Please add OPENAI_API_KEY to your .env file")
        exit(1)
    
    print("Starting Flask API server...")
    print("API will be available at http://localhost:5000")
    app.run(debug=True, port=5000)
