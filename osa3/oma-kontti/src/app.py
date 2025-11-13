from flask import Flask

app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')

@app.route('/')
def home():
    return "Welcome to the Flask application!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)