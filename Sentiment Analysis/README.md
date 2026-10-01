***Project 4: Sentiment Analysis***

The dataset

This dataset contains a collection of tweets with the hashtag #chatgpt. It is called chatgpt1.csv

The tweets were scraped from Twitter and cover a range of topics related to the ChatGPT language model. The dataset includes the following information for each tweet:

Tweet text
User information (username, user ID, location, etc.)
Tweet timestamp
Retweet and favorite count
Hashtags used in the tweet
URLs

***Overview***

A new AI company wants to do some competitor research on ChatGPT. They have managed to scrape data on
X.com (Twitter). The dataset provides a glimpse into the online conversation surrounding the ChatGPT language model. The AI company wants to know if the sentiment of ChatGPT is positive or not.


***What is sentiment***
Sentiment analysis, a branch of natural language processing (NLP) and data analytics. It involves the computational identification and categorization of opinions or emotions within text data. It aims to determine the attitude or emotional tone of a writer or speaker, classifying it as positive, negative, or neutral. This is particularly useful in understanding public opinion on various topics, brands, or products.

So for example, if I say “this drink tastes terrible” - this is a harsh statement, it will have a negative sentiment.
If I say “this drink is delicious!” - this is a good statement, it will have a positive sentiment.
If I say “this drink is blue in colour” - this is neither good or bad, so it will have a neutral sentiment Some things to note: the word “is” doesn’t really contribute to the sentiment so sometimes it’s useful to remove these words. This is know as removing stopwords. Other words include “a”, “the”, “it” etc.


In our project, we are going to use a model that processes natural language and decides if the tweet is negative,positive or neutral. The model we’re using is TextBlob - it has been trained on a lot of social media data.











