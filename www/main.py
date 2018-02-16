from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Unicode, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from py.databaseModel import User, User_Obj, Question

app = Flask(__name__)

_engine = create_engine("sqlite:///py/database.db", echo=True)
_SessiomMaker = sessionmaker(bind=_engine)
session = _SessiomMaker()

userLog = User_Obj("", "", "", "", "", None)

@app.route("/")
def index():
    questions = session.query(Question).all()
    global userLog
    return render_template("index.html", questions=questions, userLog=userLog)

@app.route("/askquestion")
def askquestion():
    return render_template("ask_questions.html")

@app.route("/question", methods=['GET'])
def question():
    title = request.args.get('title')
    question = session.query(Question).filter_by(Title=title).first()
    global userLog
    return render_template("question.html", question=question, userLog=userLog)

@app.route("/userpost")
def userpost():
    global userLog
    return render_template("user_posts.html", userLog=userLog)

@app.route("/usersettings")
def usersettings():
    global userLog
    return render_template("user_settings.html", userLog=userLog)

@app.route("/create_user", methods=['POST'])
def create_user():
    username = request.form.get('userRegister')
    name = request.form.get('nameRegister')
    password = request.form.get('pass1Register')
    password2 = request.form.get('pass2Register')

    if(password == password2 and username != "" and username != session.query(User).filter_by(Username=username).first()):
        userData = User()
        userData.Username = username
        userData.Name = name
        userData.Password = password
        session.add(userData)
        session.commit()

        userLog = User_Obj(userData.ID, username, name, password)

        return redirect(url_for('index'))

@app.route("/login_user", methods=['POST'])
def login_user():
    username = request.form.get('userLogin')
    password = request.form.get('passLogin')

    user = session.query(User).filter_by(Username=username).first()

    if(user != None and password == user.Password):

        global userLog
        userLog = User_Obj(user.ID, user.Username, user.Name, user.Password, user.Interest, None)

        return redirect(url_for('index'))
        

if(__name__ == "__main__"):
    app.run()