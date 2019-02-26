
import os
import numpy as np
import re
from functools import reduce
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

def abbr_exp_prob (model, vectorizer, abbr):
    
    abbr_split = re.split('_', abbr)
    #idxs = []
    probas = []
    words = []
    
    for abbrv in abbr_split:
        abbrprobs = model.predict_proba(vectorizer.transform([abbrv]))
        idx = np.argpartition(abbrprobs, -5)
        #idxs.append(idx[0,-5:])
        probas.append(abbrprobs[0,idx[0,-5:]])
        words.append(model.classes_[idx[0,-5:]])
        
    return probas, words


def mult_all(x,y):
    probs = []
    for i in x:
        for j in y:
            probs.append(i*j)
    return probs


def build_elns(x,y):
    elns = []
    for i in x:
        for j in y:
            elns.append(i + " " + j)
    return elns


def get_possible(model, vectorizer, abbr):

    probs, words = abbr_exp_prob(model, vectorizer, abbr.lower())

    eln_probs = np.array(reduce(mult_all, probs))
    poss_elns = np.array(reduce(build_elns, words))

    residx = np.argpartition(eln_probs, -5, axis = 0)[-5:]

    eln_probs = eln_probs[residx]
    poss_elns = poss_elns[residx]

    #poss_elns = {}
    poss_elns = [(y,int(x*100)) for x,y in sorted(zip(eln_probs,poss_elns), reverse=True)]
    #eln_probs = sorted(eln_probs, reverse=True)

    return poss_elns#, eln_probs


def get_possible_dict(model, vectorizer, abbr):

    probs, words = abbr_exp_prob(model, vectorizer, abbr.lower())

    eln_probs = np.array(reduce(mult_all, probs))
    poss_elns = np.array(reduce(build_elns, words))

    residx = np.argpartition(eln_probs, -5, axis = 0)[-5:]

    eln_probs = eln_probs[residx]
    poss_elns = poss_elns[residx]

    #poss_elns = {}
    poss_elns = {y: int(x*100) for x,y in sorted(zip(eln_probs,poss_elns), reverse=True)}
    #eln_probs = sorted(eln_probs, reverse=True)

    return poss_elns#, eln_probs
