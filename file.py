from flask import Flask,request,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='hungama'
app.config['MYSQL_DB']='class'
#app.secret_key('abcd')
conn=MySQL(app)
@app.route('/',methods=['POST','GET'])

def home():
    msg=""
    if request.method=='POST':
        uname = request.form["uname"]
        eid = request.form["email_id"]
        pwd = request.form["password"]
        con = conn.connection.cursor()
        query = "select username,password,email_id from users where username=%s and password=%s and email_id=%s"
        con.execute(query,(uname,pwd,eid))
        result=con.fetchall()
        if result:
            return "successfully logged in"
        else:
            msg="invalid input/s"
    return render_template("home2.html",message=msg)

def home():
    msg=""
    if request.method=='POST':
        uname = request.form["uname"]
        eid = request.form["email_id"]
        pwd = request.form["password"]
        con = conn.connection.cursor()
        query = "select username,password,email_id from users where username=%s and password=%s and email_id=%s"
        con.execute(query,(uname,pwd,eid))
        result=con.fetchall()
        if result:
            return "successfully logged in"
        else:
            msg="invalid input/s"
    return render_template("home2.html",message=msg)



@app.route('/output',methods=['POST','GET'])
def output():
    return "nothing"

if __name__ == '__main__':
    app.run(debug=True,port=5001)