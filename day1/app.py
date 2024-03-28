from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
mydb=mysql.connector.connect(host='localhost',user='root',password='3010',db='sowji')
with mysql.connector.connect(host='localhost',user='root',password='3010',db='sowji'):
    cursor=mydb.cursor(buffered=True)
    cursor.execute("Create table if not exists additems(itemid varchar(30),name varchar(30),description varchar(20))")
    cursor.execute("Create table if not exists studentfeedback(name varchar(50),email varchar(200),branch varchar(30),feedback TEXT)")
    cursor.execute("Create table if not exists registration(name varchar(50),mobile varchar(20),email varchar(50) unique,address varchar(50),password varchar(20))")
@app.route('/home')
def home():
    return 'sowji'
@app.route('/login')    
def index():
    return "login page" 
@app.route('/sam/<int:num>')
def sam(num):
    return f'sowji roll num is {str(num)}'
@app.route('/benny/<int:number>')
def greater_num(number):
    if(number>25):
        return "number is greater than 25"
    else:
        return "number is less than 25"
@app.route('/lakshmi')
def homepage():
    return render_template('lakshmi.html')
@app.route('/feedback',methods=['GET','POST'])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        branch=request.form.get("branch")
        feedback=request.form.get("feedback")
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into studentfeedback values(%s,%s,%s,%s)',[name,email,branch,feedback])
        mydb.commit()
        cursor.close()
        print(name)
        print(email)
        print(branch)
        print(feedback)
    return render_template('feedbackform.html')
@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method=="POST":
        username=request.form.get("username")
        mobile=request.form.get("mobile")
        email=request.form.get("email")
        address=request.form.get("address")
        password=request.form.get("password")
        cursor=mydb.cursor(buffered=True)
        cursor.execute('insert into registration values(%s,%s,%s,%s,%s)',[username,mobile,email,address,password])
        mydb.commit()
        cursor.close()
        print(username)
        print(mobile)
        print(email)
        print(address)
        print(password)
    return render_template('registration.html')
app.run()