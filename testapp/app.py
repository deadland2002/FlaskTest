from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
def test():
    return "testing"

@app.route("/ok")
def ok():
    return "ok"