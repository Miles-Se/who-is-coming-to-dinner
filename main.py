from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/menutable")
def menutable():
    return render_template("generic.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")


@app.route("/biographies")
def biographies():
    return render_template("biographies.html")


@app.route("/secretelements")
def elements():
    return render_template("secretelements.html")


if __name__ == "__main__":
    app.run(debug=True)
