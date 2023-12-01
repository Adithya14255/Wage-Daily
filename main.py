from flask import *
from flask_mysqldb import MySQL
from templates import *


app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='hungama'
app.config['MYSQL_DB']='class'
app.secret_key="1234"
conn=MySQL(app)
@app.route('/',methods=['POST','GET'])

def home():
    return render_template("home.html")

@app.route('/add_worker',methods=['POST','GET'])
def add_worker():
    msg=''
    if request.method=='POST':
        uname = request.form["uname"]
        pwd = request.form["pswd"]
        con = conn.connection.cursor()
        query = "select employee_id,username,password from users where username=%s and password=%s"
        con.execute(query,(uname,pwd))
        result=con.fetchall()
        if result:
            return redirect(url_for('truehome',name=result[0][0]))
        else:
            msg="Invalid Username/Password"
    return render_template("add_worker.html",message=msg)

@app.route('/add_request',methods=['POST','GET'])
def add_request(name):
    if request.method=='POST':
        ename = request.form["ename"]
        tj = request.form["tj"]
        dist = request.form["dist"]
        locality = request.form["locality"]
        pincode = request.form["pincode"]
        contact = request.form["contact"]
        workreq = request.form["workreq"]
        wage = request.form["wage"]
        con = conn.connection.cursor()
        query = "insert into request(wage,ename,tj,dist,locality,pincode,contact,workreq) values(%s,%s,%s,%s,%s,%s,%s,%s) ;"
        con.execute(query,(wage,ename,tj,dist,locality,pincode,contact,workreq))
        con.connection.commit()
        con.close()
        flash("request added!")
        return redirect(url_for('truehome'))
  
    return render_template("add_request.html")



@app.route('/truehome/<string:name>',methods=['POST','GET'])
def truehome(name):
    con=conn.connection.cursor()
    con.execute("select * from request;")
    result=con.fetchall()
    return render_template("truehome.html",result=result,uname=name)

@app.route('/request_accept/<string:sno>/<string:name>',methods=['POST','GET'])
def request_accept(sno,name):
    con=conn.connection.cursor()
    con.execute("select ename,tj,locality,pincode,contact,wage from request where ename=%s",[sno])
    result=con.fetchall()
    return render_template("request_accept.html",result=result,name=name)

@app.route('/completion/<string:sno>/<string:name>',methods=['POST','GET'])
def completion(sno,name):
        con=conn.connection.cursor()
        query='delete from request where ename=%s;'
        con.execute(query,[sno])
        con.connection.commit()
        con.close()
        return render_template("completion.html",name=name)

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=="POST":
        uname= request.form['uname']
        password= request.form['pswd']
        email=request.form['email']
        con=conn.connection.cursor()
        query='insert into users (username,email_id,password) values(%s,%s,%s);'
        con.execute(query,(uname,email,password))
        con.connection.commit()
        con.close()
        flash('new user created!')
        return redirect(url_for('add_worker'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)