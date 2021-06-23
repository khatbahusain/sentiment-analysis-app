from flask import Flask
from flask import request

import requests
import json
import os


app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return '''<h1>Please enter a sentence to predict the sentiment:</h1><form method="POST">
    <input name="text">
    <input type="submit">
</form>'''


@app.route('/', methods=['POST'])
def main():

    text = request.form['text']
    processed_text = text.upper()

    scoring_uri = os.environ.get("SCORING_URI")
    key = os.environ.get("KEY")


    # Set the appropriate headers
    headers = {"Content-Type": "application/json"}
    headers["Authorization"] = f"Bearer {key}"


    data = {'text': [text]}


    data = json.dumps(data)


    resp = requests.post(scoring_uri, data=data, headers=headers)
    print(resp)

    
    data = json.loads(resp.text)


    sent, score = data['sentiment'], data['score']


    return "<h1>Sentence : "+text+"</h1><h1>Sentiment : "+sent+"</h1><h1>Score : "+score+"</h1>"
