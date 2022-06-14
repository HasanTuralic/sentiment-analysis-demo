from classifier import SentimentClassifier
from flask import Flask, request
import json

# create a Flask instance
app = Flask(__name__)
# load pre-trained classifier
classifier = SentimentClassifier()

# A simple HTML Form to test the API
description = """
                <!DOCTYPE html>
                <head>
                <title>Sentiment Analysis Demo</title>
                </head>
                <body>  
                    <h1>Sentiment Analysis Demo</h1>
                    <form action="http://localhost:5000/api" method="post" enctype='application/json'>
                        <input name="messages" id="messages" value="I liked the movie.">
                        <button type="submit">Predict</button>
                    </form>
                </body>
                """

# root url '/' shows simple landing page


@app.route('/', methods=['GET'])
def hello_world():
    # return a html format string that is rendered in the browser
    return description


@app.route('/api', methods=['POST'])
def predict():
    try:
        # handles also form data because of simple HTML demo
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            messages = request.json
        elif (content_type == 'application/x-www-form-urlencoded'):
            messages = [request.form["messages"]]
        prediction = classifier.predict(messages)
        return json.dumps(prediction)
    except Exception as e:
        return json.dumps({'error': str(e)})


if __name__ == "__main__":
    # for debugging locally
    app.run(debug=True, host='0.0.0.0', port=5000)

    # for production
    #app.run(host='0.0.0.0', port=5000)
