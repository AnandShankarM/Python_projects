from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Backend"

@app.route("/data")
def data():
    return jsonify({
        "message": "Hello Backend",
        "type": "json"
    })

if __name__ == "__main__":
    app.run(debug=True)

