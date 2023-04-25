from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    username="Grace Ataro"
    return render_template("index.html",username=username)
app.run()
@app.route("/products")
def products():
    return render_template("products.html")
app.run()