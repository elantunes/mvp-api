from flask_cors import CORS
from flask import Flask

app2 = Flask(__name__)

CORS(app2)

@app2.get("/po")
def hello_world():
    return "<p>Hello, World!</p>"