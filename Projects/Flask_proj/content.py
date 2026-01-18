#Content creation
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():
    return "<h1 align=center> Add your name at the the end of the URL</h1>"

@app.route("/<name>")
def hello(name):
    return f"<h1> Hello {name} </h1>"\
            "<p> This is fist flask server. Learning python"\
            "<p><img src='https://media0.giphy.com/media/12mX8YzVVmomuA/100.webp?cid=ecf05e4700yz4tlshs1yuwv7ekcgqut2xamuq06i6ejcpb0a&rid=100.webp&ct=g' margin=200 padding=200></p>"


if __name__ == "__main__":
    app.run(debug=True)
