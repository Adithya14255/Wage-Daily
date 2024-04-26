# flask_basics
 
uname = request.form['username']
            email = request.form['email']
         	password = request.form['password']
			query = "insert into users(username,email,password) values(%s,%s,%s) ;"
        	my_cursor.execute(query,(uname,email,password))
    		mydb.commit()
    		return render_template('login.html')
    return render_template('login.html')