from flask import Flask, render_template, request, jsonify
from predictor import main

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()

    X = data["X"]
    Y = data["Y"]
    mode = data["mode"]
    value = data["value"]

    result = main(X, Y, mode, value)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
