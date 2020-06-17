from flask import Flask,render_template,flash,request,session,redirect,url_for
import sqlite3
from datetime import timedelta


app=Flask(__name__)
app.secret_key = "jazy"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template("index.html")
# def adminn(admin):
#     return f"hello {admin}!"
#
# #

@app.route("/weather")
def Forecast():
        # if "usrname" in session:
            conn = sqlite3.connect("test2.db")
            c = conn.cursor()
            c.execute("SELECT * from forecasts")
            rows = c.fetchall()
            return  render_template("table.html",row=rows)
            conn.commit
            conn.close()
        # else:
        #     return redirect("login.html")
@app.route("/Cities")
def City():
        # if "usrname" in session:

            conn = sqlite3.connect("test2.db")
            c = conn.cursor()
            c.execute("SELECT * from cities")
            cities = c.fetchall()
            return  render_template("Cities.html",Citydata=cities)
            conn.commit
            conn.close()
        # else:
            # return render_template("login.html")



@app.route("/update",methods=['POST',"GET"])
def update():
    # if "usrname" in session:

        if request.method == "POST":

            id = request.form["id"]
            name=request.form["cityname"]
            url=request.form["url"]
            conn = sqlite3.connect("test2.db")
            c = conn.cursor()
            c.execute("UPDATE cities SET nameofcity=?,url=? WHERE id=?",(name,url,id))
            conn.commit()
            conn.close()
            return render_template("update.html")
         # else:
         #      flash("You have to login or Signup first")
              # return render_template("login.html")


@app.route("/deleterecord",methods = ["POST","GET"])
def deleterecord():
    if request.method == "POST":
        # if "usrname" in session:

            id = request.form["id"]
            conn = sqlite3.connect("test2.db")
            c = conn.cursor()
            c.execute("delete from cities where id = ?",id)
            conn.commit()
            conn.close()
            return render_template("delete.html")
    # else:
    #     return render_template("login.html")

@app.route('/signup',methods=["POST","GET"])
def signup():
    if request.method == "POST":
        name = request.form["nm"]
        email = request.form["email"]
        usrname = request.form["usr"]
        pas = request.form["pass"]
        # session["User"]=usrname
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()

        c.execute("INSERT INTO userdata(Name,Username,Email,Password)VALUES(:Name,:Username,:Email,:Password)",{'Name': name,'Username': usrname,'Email': email,'Password': pas})
        conn.commit()
        conn.close()
        render_template("login.html")
    else:
        return render_template("login.html")









@app.route('/admin',methods=["POST","GET"])
def admin():
    if request.method == "POST":

        session.permanent = True
        city_name = request.form["cityname"]
        Url = request.form["url"]
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("INSERT INTO cities(nameofcity,url)VALUES(:nameofcity,:url)",{'nameofcity': city_name ,'url' : Url})
        conn.commit()
        conn.close()
        flash("Added successfully")

        return redirect(url_for("home"))

# @app.route('/login',methods=['POST','GET'])
# def login():
#     if "usrname" not in session:
#         return render_template("")


if __name__== '__main__':
        app.run(debug=True)
