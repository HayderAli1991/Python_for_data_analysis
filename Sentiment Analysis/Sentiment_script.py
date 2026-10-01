# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:49:30 2026

@author: Dell
"""

# To install libraries
# pip install wordcloud
# pip install langdetect
# pip install sumy
# pip install textblob

# Wordcloud - This package is used to generate word cloud images.
# Langdetect - This library is used for language detection.
# Sumy - Automatic summarization of text documents and articles.
# TextBlob - TextBlob is a library for processing textual data

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from langdetect import detect
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from textblob import TextBlob


# Reading the CSV file
df = pd.read_csv('chatgpt1.csv')

# Creating function to detect languages 
x = df['Text'][0]
lang = detect(x)


def det(x):
    try:
        lang = detect(x)
    except:
        lang = 'other'
    return lang


df['lang'] = df['Text'].apply(det)
df = df.loc[df['lang'] == 'en'] # Thks is filtering 
df = df.reset_index(drop = True) # drop True will remove the filtered index and create a new index


# Cleaning some text 
#df['Text'] = df['Text'].str.replace('https', '')
#df['Text'] = df['Text'].str.replace('http', '')
#df['Text'] = df['Text'].str.replace('t.co', '')

# Developing a sentiment function

def get_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'
    
df['sentiment'] = df['Text'].apply(get_sentiment)

# Generating a word cloud

comment_words = ''
stopwords = set(STOPWORDS)

for val in df.Text:
    val = str(val)
    tokens = val.split()
    comment_words = comment_words + ' '.join(tokens) + ' '

wordcloud = WordCloud(width=900, height=500, background_color = 'black', 
                      stopwords = stopwords, min_font_size=10).generate(comment_words)

plt.figure(figsize = (8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout()
plt.show()

import seaborn as sns

sns.set_style('whitegrid')
plt.figure(figsize=(10,5))

sns.countplot(x = 'sentiment' , data = df)
plt.xlabel('Sentiment')
plt.ylabel('Count of Sentiment')
plt.title('Sentiment Distribution')
plt.show()







































































































































































































































































