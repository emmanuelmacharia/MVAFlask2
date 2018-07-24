from flask import Flask, url_for, request, render_template;
from app import app;
import redis

r =redis.StrictRedis(host='localhost', port = 6379, db=0,  charset = 'utf-8', decode_responses = True)
#server/
@app.route('/')
def hello():

   #Works the same  
   #r=redis.StrictRedis('localhost', 6379, 0)
    #r=redis.StictRedis()
    """Renders a sample page."""
    createlink = "<a href= '" + url_for('create') + "'> Create a question</a>";
    return "Hello World!"+"<br />" + createlink

#server /create
@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method=='GET':
        #send user the form
        return render_template('createquestion.html')
    elif request.method == 'POST':
        #reading the form
        title = request.form['title']
        question = request.form['question']
        answer = request.form['answer']
        #store answer

        #return the template
        return render_template('questioncreated.html', question = question);
    else:
        return "<h1>Invalid question</h1>";

#server/question/<title>
@app.route('/question/<title>', methods = ['GET', 'POST']) #this is a Vanity URL
def question(title):
    if request.method == 'GET':
        #send user the form
        question = 'Question here'
        #read question from database

        return render_template('Answers.html', question=question);
    elif request.method == 'POST':
        #user attempts to answer the question
        Submittedanswer = request.form['Submittedanswer'];

        #get answer from database
        answer = 'Answer'
        if Submittedanswer == answer:
            return render_template('correct.html')
        else:
            return render_template('wrong.html', Submittedanswer = Submittedanswer, answer = answer);
    return "<h2>" + title + "</h2>";
