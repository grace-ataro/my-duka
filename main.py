from flask import Flask,render_template,request,redirect

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
 cur.execute("SELECT * from products;")
 products = cur.fetchall()
 print("products")

 return render_template("products.html",products=products)


@app.route("/sales")
def sales():
 cur = conn.cursor()
 cur.execute("SELECT s.id,p.name,s.quantity,s.created_at from products as p join sales as s on s.pid=p.id;")
 sales = cur.fetchall()
 cur.execute("SELECT * from products;")
 products=cur.fetchall()
 print("sales")

 return render_template("sales.html",sales=sales,products=products)
 
@app.route('/save-product',methods=['POST'])
def save_product():
    myname=request.form['name']
    mybp=request.form['bp']
    mysp=request.form['sp']
    myquantity=request.form['quantity']
    print(myname,mybp,mysp,myquantity)
    cur=conn.cursor()
    cur.execute("INSERT INTO products(name,buying_price,selling_price,quantity)VALUES (%s, %s, %s, %s)",(myname,mybp,mysp,myquantity))
    conn.commit()

    return redirect("/products")
                
@app.route('/save-sales',methods=['POST'])
def save_sales():
    pid=request.form['pid']
    quantity=request.form['quantity']
    print(pid,quantity)
    cur=conn.cursor()
    cur.execute("INSERT INTO sales(pid,quantity,created_at)VALUES (%s, %s,%s)",(pid,quantity,"now()"))
    conn.commit()

    return redirect("/sales")

@app.route('/dashboard')
def dashboard():
 cur = conn.cursor()
 cur.execute("SELECT sum((p.selling_price*s.quantity)-(p.buying_price*s.quantity))as total,p.name FROM products as p join sales as s on s.pid=p.id group by p.name;")
 rows = cur.fetchall()
 a = []
 b = []
 for i in rows:
    a.append(i[1])
    b.append(float(i[0]))
 cur.execute("SELECT SUM(p.selling_price * s.Quantity) as TotalSales FROM  products  as p JOIN sales as s ON s.pid = p.id GROUP BY created_at;")
 rows = cur.fetchall()
 a = []
 b = []
 for i in rows:
    a.append(i[0])
    b.append(float(i[0]))
 
 return render_template("dashboard.html",products=a,sales=b)

app.run(debug=True)