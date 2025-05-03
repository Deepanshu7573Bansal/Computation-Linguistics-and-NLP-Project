# Import libraries
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import textdistance
import re
from collections import Counter

# Flask app
app=Flask(__name__)

# Upload txt file
words=[]
with open('Book_Corpus.txt','r',encoding='utf-8') as f:
    data=f.read()
    data=data.lower()
    word=re.findall(r'\w+',data)
    words=words+word

# Correct text by duplicate words
v=set(words)

# Check frequency of words
word_frequency=Counter(words)

# Calculate the probability of the each word
Total_words=sum(word_frequency.values())

probability={}
for k in word_frequency.keys():
    probability[k]=word_frequency[k]/Total_words

# -- App --
@app.route('/')
def index():
    return render_template('index.html',suggestions=None)

# -- App with main logic --
@app.route('/suggest',methods=['POST'])
def suggest():
    keyword=request.form['keyword'].lower()
    if keyword:
        similarities=[1-(textdistance.Jaccard(qval=2)).distance(w,keyword) for w in word_frequency.keys()]
        df=pd.DataFrame.from_dict(probability,orient='index').reset_index()
        df.columns=['Word','Prob']
        df['Similarity']=similarities
        suggestions=df.sort_values(['Similarity','Prob'],ascending=False)[['Word','Similarity']]
        suggestions_list=suggestions.to_dict('records')
        return render_template('index.html',suggestions=suggestions_list[0:5])
    

# Main function
if __name__=='__main__':
    app.run(debug=True)