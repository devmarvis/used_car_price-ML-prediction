from flask import Flask, request, jsonify
from flask_cors import CORS
from . import util

app = Flask(__name__)
CORS(app)

util.load_saved_artifacts()

@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = request.get_json()

    response = jsonify(util.predict_price(util.data_processor(data)))

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    app.run(port=5005)
