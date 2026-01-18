#This is based on a template - html , css and js files - just the integration
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def card():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()