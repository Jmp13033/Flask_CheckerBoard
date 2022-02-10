from os import name
from flask import Flask, render_template, url_for



app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/4")
def about():
    return render_template("four.html")



@app.route('/<x>/<y>')
def changeSquares(x, y):
    return render_template("squares.html", rows=int(x), columns=int(y))


if __name__== "__main__":
    app.run(debug=True) 

