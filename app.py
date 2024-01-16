from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user_question = request.form['question']

        # get the answer from pipeline
        ai_answer = getAnswer(user_question)
        
        # add as many variables as you want to render in the template
        return render_template('index.html', answer = ai_answer, question = user_question)

def getAnswer(user_question):
    # load pipeline
    model = pipeline("question-answering", "deepset/roberta-base-squad2")

    # read a context
    f = open("earth.txt", "r")
    earth_context = f.read()

    # get answer
    result = model(question = user_question, context = earth_context)
    answer = result["answer"].capitalize() + ". I am " + str(round(result["score"] * 100)) + "% sure."

    # return answer
    return answer

# Piple result: 
# {'score': 0.9792739152908325, 'start': 31, 'end': 40, 'answer': 'Dartmouth'}

# Default model: 
# distilbert-base-cased-distilled-squad

# deepset/roberta-base-squad2