#Guessing game
from flask import Flask, session
from random import randint
app = Flask(__name__)
app.secret_key = "guess-game-secret-key"

@app.route("/")
def hi():
    session["number"] = randint(0,9)
    return "<h1 align=center> Guess a number between 0 and 9</h1>"\
            "<p align=center><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></p>"

@app.route("/<int:usernumber>")
def show_number(usernumber):
    number = session.get("number")
    if usernumber < number:
        return "<h1 style='color:red' align=center> Too low, try again"\
                "<p align=center><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></p>"
    elif usernumber > number:
        return "<h1 style='color:violet' align=center> Too high, try again"\
                "<p align=center><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></p>"
    else:
        return "<h1 style='color:green' align=center> You found me" \
               "<p align=center><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></p>"

if __name__ == "__main__":
    app.run(debug=True)