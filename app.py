from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",)

@app.route("/", methods=["POST"])
def greet():
    nama = request.form.get("nama")
    return render_template("index.html", nama=nama)