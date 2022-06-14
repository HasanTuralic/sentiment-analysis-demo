# Sentiment Analysis Demo

A simple demo of a sentiment analysis model. The model is a fine-tuned BertForSequenceClassification and has been trained using huggingface and PyTorch libraries. The trained model needs to be separately downloaded (instructions in Installation). The model can be tested using a REST API, which was implemented using flask. Furthermore, the model can be tested via a simple web interface. The application is containerized using docker.

## :rocket: Installation

1. Create virtual environment `python -m venv venv`
2. Start virtual environment `venv\scripts\activate` (win) or `source venv/bin/activate` (unix, mac)
3. Install dependencies `pip install -r requirements.txt`
4. Download trained model [here](https://www.dropbox.com/s/6lqh70dkgwnvq4s/sentiment-analysis-model.zip?dl=0) and extract files to the  `model` directory.
5. Change directory `cd src` and run app `python api.py`

## :whale: Containerize using Docker

1. `docker build --tag sentiment-analysis .`
2. `docker run -d -p 5000:5000 sentiment-analysis`

## :computer: Usage

### Test via API 

Using Postman for example, send **POST** request to `http://localhost:5000/api`

Set headers:
```
Content-Type: application/json
```
Body must contain a list of messages, for example:
```
[
    "I liked the movie",
    "There is a book on the desk",
    "I hate it!"
]
```
The API returns a prediction for each message consisting of the message, the predicted label and a confidence score. For example:

```
[
    {
        "message": "I liked the movie", 
        "prediction": "positive", 
        "score": 0.9988993406295776
    }, 
    {
        "message": "There is a book on the desk", 
        "prediction": "neutral", 
        "score": 0.9967913031578064
    }, 
    {
        "message": "I hate it!", 
        "prediction": "negative",
        "score": 0.9833186864852905
    }
]
```

### Test via Browser 

Open `http://localhost:5000/` and type in message.

## Code layout

| Directory | Description |
| --- | --- |
| notebooks/sentiment-analysis.ipynb | Notebook used for data analysis and training the model. |
| src/api.py | Staring point of the app. Implements the API using flask. |
| src/classifier.py | Loads the trained model and tokenizer. Used to perform predictions. |
| src/model | Should contain the trained model downloaded from [this link](https://www.dropbox.com/s/6lqh70dkgwnvq4s/sentiment-analysis-model.zip?dl=0). |
