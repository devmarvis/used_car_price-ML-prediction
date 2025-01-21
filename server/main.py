from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = request.get_json()

    response = jsonify(util.predict_price(util.data_processor(data)))

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5005)
