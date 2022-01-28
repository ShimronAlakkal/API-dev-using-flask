from flask import Flask, jsonify
from pip import main

app = Flask(__name__)

@app.get("/")
def index():
    return "you're now at root"

if __name__ == '__main__':
    app.run(debug = True)
    