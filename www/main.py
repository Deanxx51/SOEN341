from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/askquestion")
def askquestion():
    return render_template("ask_questions.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/userpost")
def userpost():
    return render_template("user_posts.html")

@app.route("/usersettings")
def usersettings():
    return render_template("user_settings.html")

@app.route("/mail", methods=['POST'])
def sendMail():
    mailName = request.form.get('Name')
    mailSender = request.form.get('email')
    mailMessage = request.form.get('Message')

if(__name__ == "__main__"):
    app.run()