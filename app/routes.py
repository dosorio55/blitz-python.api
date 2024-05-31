from app import app

# Define your API routes here
@app.route('/')
def index():
    return 'Welcome to your Flask API!'
