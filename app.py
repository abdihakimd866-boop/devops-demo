
# A simple web app that we'll auto-deploy with Jenkins

from flask import Flask
import os

app = Flask(__name__)

# Movie list (we'll change this later to see auto-deploy!)
MOVIES = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Interstellar"
]

@app.route('/')
def home():
    """Main page showing movie recommendations"""
   
    # Get version from environment (Jenkins will set this)
    version = os.getenv('APP_VERSION', '1.0')
    build_number = os.getenv('BUILD_NUMBER', 'local')
   
    # Build HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title> Movie Recommender</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 50px;
                text-align: center;
                margin: 0;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 40px;
                max-width: 600px;
                margin: 0 auto;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }}
            h1 {{
                font-size: 48px;
                margin-bottom: 10px;
            }}
            .subtitle {{
                font-size: 18px;
                opacity: 0.9;
                margin-bottom: 30px;
            }}
            .movies {{
                background: rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 30px;
                margin-top: 30px;
            }}
            .movie {{
                font-size: 24px;
                margin: 15px 0;
                padding: 15px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                transition: transform 0.2s;
            }}
            .movie:hover {{
                transform: scale(1.05);
                background: rgba(255, 255, 255, 0.2);
            }}
            .footer {{
                margin-top: 40px;
                font-size: 14px;
                opacity: 0.8;
            }}
            .version {{
                background: #10b981;
                padding: 10px 20px;
                border-radius: 20px;
                display: inline-block;
                margin-top: 20px;
                font-weight: bold;
            }}
            .build {{
                background: #3b82f6;
                padding: 8px 16px;
                border-radius: 15px;
                display: inline-block;
                margin-top: 10px;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎬 Movie Recommender</h1>
            <p class="subtitle">Top movies you should watch this weekend!</p>
           
            <div class="movies">
    """
   
    # Add each movie
    for movie in MOVIES:
        html += f'            <div class="movie">{movie}</div>\n'
   
    html += f"""
            </div>
           
            <div class="version">
                Version: {version}
            </div>
            <div class="build">
                Build: #{build_number}
            </div>
           
            <div class="footer">
                <p>🚀 Deployed automatically with Jenkins CI/CD</p>
                <p>Every code push triggers automatic deployment!</p>
            </div>
        </div>
    </body>
    </html>
    """
   
    return html

@app.route('/health')
def health():
    """Health check endpoint - Jenkins uses this to verify deployment"""
    return {
        'status': 'healthy',
        'app': 'movie-recommender',
        'movies_count': len(MOVIES)
    }

if __name__ == '__main__':
    # Run on port 5000
    print("Movie Recommender starting on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
