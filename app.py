from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/breakfast")
def breakfast():
    return render_template("breakfast.html")

@app.route("/lunch")
def lunch():
    return render_template("lunch.html")

@app.route("/dinner")
def dinner():
    return render_template("dinner.html")

@app.route("/sidedishes")
def side_dishes():
    return render_template("sidedishes.html")

@app.route("/dessert")
def dessert():
    return render_template("dessert.html")





if __name__ == "__main__":
    app.run(port=8000, debug=True)