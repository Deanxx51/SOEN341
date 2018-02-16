from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Unicode, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from py.databaseModel import User, User_Obj, Question, Answer
from datetime import date

app = Flask(__name__)

_engine = create_engine("sqlite:///py/database.db", echo=True)
_SessiomMaker = sessionmaker(bind=_engine)
session = _SessiomMaker()

userLog = User_Obj("", "", "", "", "", None)

@app.route("/")
def index():
    global userLog
    questions = session.query(Question).all()
    questionsR = questions[::-1]
    return render_template("index.html", questions=questionsR, userLog=userLog)

@app.route("/askquestion")
def askquestion():
    global userLog
    return render_template("ask_questions.html", userLog=userLog)

@app.route("/question", methods=['GET'])
def question():
    global userLog
    title = request.args.get('title')
    question = session.query(Question).filter_by(Title=title).first()
    answers = session.query(Answer).filter_by(Question_ID=question.ID).all()
    return render_template("question.html", question=question, userLog=userLog, answers=answers)

@app.route("/userpost")
def userpost():
    global userLog
    questions = session.query(Question).filter_by(User_ID=userLog.Username).all()
    questionsR = questions[::-1]
    return render_template("user_posts.html", questions=questionsR, userLog=userLog)

@app.route("/usersettings")
def usersettings():
    global userLog
    return render_template("user_settings.html", userLog=userLog)

@app.route("/create_user", methods=['POST'])
def create_user():
    global userLog
    username = request.form.get('userRegister')
    name = request.form.get('nameRegister')
    password = request.form.get('pass1Register')
    password2 = request.form.get('pass2Register')

    if(password == password2 and username != "" and username != session.query(User).filter_by(Username=username).first().Username):
        userData = User()
        userData.Username = username
        userData.Name = name
        userData.Password = password
        session.add(userData)
        session.commit()

        userLog = User_Obj(userData.ID, username, name, password, "", None)

    return redirect(url_for('index'))

@app.route("/create_question", methods=['POST'])
def create_question():
    global userLog
    questionTitle = request.form.get('questionTitle')
    questionComplete = request.form.get('questionComplete')

    if(session.query(Question).filter_by(Title=questionTitle).first() != None):
        question = Question()
        question.Title = questionTitle
        question.Question = questionComplete
        question.Date = date.today()
        question.User_ID = userLog.Username
        session.add(question)
        session.commit()

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

@app.route("/change_name", methods=['POST'])
def change_name():
    global userLog
    name = request.form.get('nameEdit')
    userLog.Name = name
    user = session.query(User).filter_by(Username=userLog.Username).first()
    user.Name = name
    session.add(user)
    session.commit()

    return redirect(url_for('usersettings'))

@app.route("/edit_interest", methods=['POST'])
def edit_interest():
    global userLog
    interest = request.form.get('editInterest')
    userLog.Interest = interest
    user = session.query(User).filter_by(Username=userLog.Username).first()
    user.Interest = interest
    session.add(user)
    session.commit()

    return redirect(url_for('usersettings'))

@app.route("/change_password", methods=['POST'])
def change_password():
    global userLog
    oldPassword = request.form.get('oldPassword')
    newPassword = request.form.get('newPassword')
    if(oldPassword == newPassword):
        userLog.Password = newPassword
        user = session.query(User).filter_by(Username=userLog.Username).first()
        user.Interest = newPassword
        session.add(user)
        session.commit()

        return redirect(url_for('usersettings'))
    else:
        return redirect(url_for('index'))

@app.route("/delete_question", methods=['GET'])
def delete_question():
    global userLog
    Q = request.args.get('dfsudgs')
    deleteQuestion = session.query(Question).filter_by(Title=Q).first()
    for answer in session.query(Answer).filter_by(Question_ID=deleteQuestion.ID).all():
        session.delete(answer)
        session.commit()
    session.delete(deleteQuestion)
    session.commit()

    return redirect(url_for('userpost'))
        
@app.route("/add_answer", methods=['POST'])
def add_answer():
    global userLog
    ans = request.form.get('inputAnswer')
    qID = request.form.get('question_id')
    qName = request.form.get('Name_id')
    answer = Answer()
    answer.Answer = ans
    answer.Vote = 0
    answer.Date = date.today()
    answer.Question_ID = qID
    answer.User_ID = userLog.Username
    session.add(answer)
    session.commit()

    return redirect("/question?title="+qName)

if(__name__ == "__main__"):
    app.run()