
import re
import json

import azure.functions as func

from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def init():

    global model
    global vectorizer

    model = joblib.load('sentimentpredictor/model.pkl')
    vectorizer = joblib.load('sentimentpredictor/tfidf.pkl')


def preprocess_string(inputstring):

    cleanedstring = [re.sub(r'[^a-zA-Z0-9]',' ', D).lower().strip() for D in inputstring]
    cleanedstring = [re.split(r'\s+', D) for D in cleanedstring if D != '']
    cleanedstring = [[x for x in s if x.isalpha()] for s in cleanedstring]
    cleanedstring = [' '.join(x) for x in cleanedstring]

    return cleanedstring


def main(req: func.HttpRequest):
    
    init()

    parsed_data = req.get_json()
    comment = parsed_data['comment']

    comment = preprocess_string(comment)

    comment_vec = vectorizer.transform(comment)

    sentiment = model.predict(comment_vec)
    keys = ["Comment {} sentiment".format(i) for i in range(1, len(sentiment)+1)]

    output = dict(zip(keys, sentiment))
    
    return json.dumps(output)