from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h2>Car Price Prediction...</h2>"


if __name__ == "__main__":
    app.run(port=5005)
