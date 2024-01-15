from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_question = request.form['question']
        ai_answer = 'This is your answer!!'
        
        # add as many variables as you want to render in the template
        return render_template('index.html', answer = ai_answer, question = user_question)

