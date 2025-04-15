import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords once, using Streamlit's caching
@st.cache_resource
def load_stopwords():
    nltk.download('stopwords')
    return stopwords.words('english')

import os

# Load model and vectorizer once
@st.cache_resource
def load_model_and_vectorizer():
    # Get the absolute path to the models directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(os.path.dirname(current_dir), 'models')

    # Load the model and vectorizer
    with open(os.path.join(models_dir, 'model.pkl'), 'rb') as model_file:
        model = pickle.load(model_file)
    with open(os.path.join(models_dir, 'vectorizer.pkl'), 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Define sentiment prediction function
def predict_sentiment(text, model, vectorizer, stop_words):
    # Preprocess text
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)
    text = [text]
    text = vectorizer.transform(text)

    # Predict sentiment
    sentiment = model.predict(text)
    return "Negative" if sentiment == 0 else "Positive"

# Function to get emoji for sentiment
def get_sentiment_emoji(sentiment):
    if sentiment == "Positive":
        return "😃"
    else:  # Negative
        return "😞"

# Set up page configuration
st.set_page_config(page_title="Tweet Sentiment Analysis", page_icon="📊")

# Main app logic
def main():
    st.title("Tweet Sentiment Analysis")

    # Load stopwords, model, vectorizer only once
    stop_words = load_stopwords()
    model, vectorizer = load_model_and_vectorizer()

    # Create text input area
    st.subheader("Enter a tweet to analyze")
    tweet_text = st.text_area("Paste or type a tweet here", height=150,
                           placeholder="Enter the tweet text you want to analyze...")

    # Add example tweets button
    if st.button("Show Example Tweets"):
        st.info("Example tweets you can copy and paste:")
        examples = [
            "I absolutely love this new phone! The camera quality is amazing and battery life is outstanding. Best purchase I've made this year! #happy",
            "This service is terrible. I've been waiting for 2 hours and still no response from customer support. Will never use again. #frustrated",
            "Just watched the new Spider-Man movie and it was pretty good. Some parts were great but the ending was a bit predictable.",
            "Can't believe how bad the weather is today. Was planning a picnic but now everything is ruined. So disappointed!",
            "Just got a promotion at work! So excited for this new chapter in my career. Hard work really does pay off!"
        ]
        for example in examples:
            st.code(example, language=None)

    # Analyze button
    if st.button("Analyze Tweet"):
        if tweet_text.strip():
            # Predict sentiment
            sentiment = predict_sentiment(tweet_text, model, vectorizer, stop_words)

            # Get emoji for the sentiment
            emoji = get_sentiment_emoji(sentiment)

            # Display simple output: sentiment word + emoji
            st.write(f"{sentiment} {emoji}")
        else:
            st.warning("Please enter a tweet to analyze.")

if __name__ == "__main__":
    main()
