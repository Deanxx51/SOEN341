from flask import Flask, request, render_template, redirect, url_for, session
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Unicode, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from py.databaseModel import User, User_Obj, Question, Answer
from datetime import date

app = Flask(__name__)
app.secret_key = 'dsfgjs'

_engine = create_engine("sqlite:///py/database.db", echo=True)
_SessiomMaker = sessionmaker(bind=_engine)
sessionDB = _SessiomMaker()

@app.route("/")
def index():
    userLog = session.get('userLog')
    questions = sessionDB.query(Question).all()
    questionsR = questions[::-1]
    return render_template("index.html", questions=questionsR, userLog=userLog)

@app.route("/askquestion")
def askquestion():
    userLog = session.get('userLog')
    return render_template("ask_questions.html", userLog=userLog)

@app.route("/question", methods=['GET'])
def question():
    userLog = session.get('userLog')
    title = request.args.get('title')
    question = sessionDB.query(Question).filter_by(Title=title).first()
    answers = sessionDB.query(Answer).filter_by(Question_ID=question.ID).all()
    return render_template("question.html", question=question, userLog=userLog, answers=answers)

@app.route("/userpost")
def userpost():
    userLog = session.get('userLog')
    questions = sessionDB.query(Question).filter_by(User_ID=userLog["Username"]).all()
    questionsR = questions[::-1]
    return render_template("user_posts.html", questions=questionsR, userLog=userLog)

@app.route("/usersettings")
def usersettings():
    userLog = session.get('userLog')
    return render_template("user_settings.html", userLog=userLog)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route("/create_user", methods=['POST'])
def create_user():
    username = request.form.get('userRegister')
    name = request.form.get('nameRegister')
    password = request.form.get('pass1Register')
    password2 = request.form.get('pass2Register')

    if(password == password2 and username != "" and username != sessionDB.query(User).filter_by(Username=username).first().Username):
        userData = User()
        userData.Username = username
        userData.Name = name
        userData.Password = password
        sessionDB.add(userData)
        sessionDB.commit()

        session['userLog'] = User_Obj(userData.ID, username, name, password, "", None).__dict__

    return redirect(url_for('index'))

@app.route("/create_question", methods=['POST'])
def create_question():
    userLog = session.get('userLog')
    questionTitle = request.form.get('questionTitle')
    questionComplete = request.form.get('questionComplete')

    if(sessionDB.query(Question).filter_by(Title=questionTitle).first() == None):
        question = Question()
        question.Title = questionTitle
        question.Question = questionComplete
        question.Date = date.today()
        question.User_ID = userLog["Username"]
        sessionDB.add(question)
        sessionDB.commit()

    return redirect(url_for('index'))

@app.route("/login_user", methods=['POST'])
def login_user():
    username = request.form.get('userLogin')
    password = request.form.get('passLogin')

    user = sessionDB.query(User).filter_by(Username=username).first()

    if(user != None and password == user.Password):

        session['userLog'] = User_Obj(user.ID, user.Username, user.Name, user.Password, user.Interest, None).__dict__

    return redirect(url_for('index'))

@app.route("/change_name", methods=['POST'])
def change_name():
    userLog = session.get('userLog')
    name = request.form.get('nameEdit')
    userLog["Name"] = name
    user = sessionDB.query(User).filter_by(Username=userLog["Username"]).first()
    user.Name = name
    sessionDB.add(user)
    sessionDB.commit()

    return redirect(url_for('usersettings'))

@app.route("/edit_interest", methods=['POST'])
def edit_interest():
    userLog = session.get('userLog')
    interest = request.form.get('editInterest')
    userLog["Interest"] = interest
    user = sessionDB.query(User).filter_by(Username=userLog["Username"]).first()
    user.Interest = interest
    sessionDB.add(user)
    sessionDB.commit()

    return redirect(url_for('usersettings'))

@app.route("/change_password", methods=['POST'])
def change_password():
    userLog = session.get('userLog')
    oldPassword = request.form.get('oldPassword')
    newPassword = request.form.get('newPassword')
    if(oldPassword == newPassword):
        userLog['Password'] = newPassword
        user = sessionDB.query(User).filter_by(Username=userLog["Username"]).first()
        user.Interest = newPassword
        sessionDB.add(user)
        sessionDB.commit()

        return redirect(url_for('usersettings'))
    else:
        return redirect(url_for('index'))

@app.route("/delete_question", methods=['GET'])
def delete_question():
    Q = request.args.get('dfsudgs')
    deleteQuestion = sessionDB.query(Question).filter_by(Title=Q).first()
    for answer in sessionDB.query(Answer).filter_by(Question_ID=deleteQuestion.ID).all():
        sessionDB.delete(answer)
        sessionDB.commit()
    sessionDB.delete(deleteQuestion)
    sessionDB.commit()

    return redirect(url_for('userpost'))
        
@app.route("/add_answer", methods=['POST'])
def add_answer():
    userLog = session.get('userLog')
    ans = request.form.get('inputAnswer')
    qID = request.form.get('question_id')
    qName = request.form.get('Name_id')
    answer = Answer()
    answer.Answer = ans
    answer.Vote = 0
    answer.Date = date.today()
    answer.Question_ID = qID
    answer.User_ID = userLog["Username"]
    sessionDB.add(answer)
    sessionDB.commit()

    return redirect("/question?title="+qName)



if(__name__ == "__main__"):
    app.run()