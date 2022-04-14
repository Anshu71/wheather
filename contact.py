from flask import Flask,render_template,request,redirect,session,flash
import mysql.connector
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)
conn=mysql.connector.connect(host="localhost",user="root", password='', database="contact_us")
cursor=conn.cursor()

@app.route('/')
def landpage():
    return render_template("landing.html")

@app.route('/contact',methods=['POST'])
def contact():
    name=request.form.get('name')
    email=request.form.get('email')
    message=request.form.get('message')

    cursor.execute("""SELECT * FROM contact_us Where name Like '{}' email like this '{}' and message like this '{}'""".format(name,email,message))
    userdata=cursor.fetchall()
    print(userdata)

    if len(userdata)>0:
        session['sr_no']=userdata
        return redirect('landing.html')
    

if __name__=='main_':
    app.run(debug=True)






# from flask import Flask, request, jsonify
# app = Flask(__name__)
# import pymysql

# @app.route('/users',methods=['POST'])
# def get_users():
#     conn=pymysql.connect(host='localhost',user='root',password='',db='contact_us')
#     cur=conn.cursor()
#     cur.execute("INSERT INTO `contact_us`(`name`, `email`, `message`) VALUES ('[value-2]','[value-3]','[value-4]')")
#     output=cur.fetchall()
#     print(output)
#     return jsonify(output)


# if __name__ == "__main__":
#     app.run(debug=True)
#     app.run(host="0.0.0.0", post=int("1234"), debug=True)