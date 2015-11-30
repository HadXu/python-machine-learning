# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:50:19 2015

@author: hadxu
"""
import sqlite3
import pickle
import os
from vectorizer import vect
clf = pickle.load(open(os.path.join('pkl_objects','classifier.pkl'),'rb'))

import numpy as np
label = {0:'negative', 1:'positive'}
example = ['I dislike this movie']
#X = vect.transform(example)
#print('Prediction: %s\nProbability: %.2f%%' % (label[clf.predict(X)[0]], np.max(clf.predict_proba(X))*100))


conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()

c.execute("SELECT * FROM review_db")

results = c.fetchall()
conn.close()
print results