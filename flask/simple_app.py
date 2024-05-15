from flask import Flask

# callable wsgi-приложение
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world"
