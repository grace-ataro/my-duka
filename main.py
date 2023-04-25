from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
app.run()
@app.route("/products")
def products():
    return render_template("products.html")
app.run()