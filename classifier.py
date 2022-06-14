from transformers import TextClassificationPipeline, BertForSequenceClassification, BertTokenizer

id2label = {0: 'negative', 1: 'neutral', 2: 'positive'}


class SentimentClassifier():

    def __init__(self):
        model = BertForSequenceClassification.from_pretrained('./model', id2label=id2label)
        tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
        self.pipe = TextClassificationPipeline(
            model=model,
            tokenizer=tokenizer,
            return_all_scores=True)

    def predict(self, messages):
        data = []
        predictions = self.pipe(messages)
        for m, p in zip(messages, predictions):
            p.sort(key=lambda x: x["score"], reverse=True)
            data.append({
                "message": m,
                "prediction": p[0]["label"],
                "score": p[0]["score"]
            })
        return data
