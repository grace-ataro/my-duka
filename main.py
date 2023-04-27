from flask import Flask,render_template

import psycopg2

app=Flask(__name__)

try:
    conn=psycopg2.connect("dbname='myduka' user='postgres' host='localhost' password='18090000'")
    print("Database connected succesfully")
except Exception as e:
    print("I am unable to connect to database",e)    
@app.route("/")
def home():
    username="Grace Ataro"
    return render_template("index.html",username=username)


@app.route("/products")
def products():
    
    # products=[
    #     (1,"omo",40,50,100,),
    #     (2,"bread",50,60,200,),
    #     (3,"milk",60,65,150,)
    # ]
 cur = conn.cursor()
 cur.execute("SELECT*from products;")
 products = cur.fetchall()
 print("products")
 return render_template("products.html",products=products)

app.run()
