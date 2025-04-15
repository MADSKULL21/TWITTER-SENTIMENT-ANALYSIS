# Tweet Sentiment Analysis

A simple application that analyzes the sentiment of tweets or text input.

## Project Structure

```
├── data/                  # Data files
│   ├── training.1600000.processed.noemoticon.csv  # Training data
│   └── Twitter_sentiment_Analysis.ipynb           # Notebook for model training
├── models/                # Model files
│   ├── model.pkl          # Trained sentiment analysis model
│   └── vectorizer.pkl     # TF-IDF vectorizer
├── src/                   # Source code
│   ├── app.py             # Streamlit application
│   └── config.py          # Configuration file
├── .gitignore             # Git ignore file
├── LICENSE                # License file
├── main.py                # Main entry point
├── README.md              # This file
├── requirements.txt       # Dependencies
└── setup.py               # Setup script for package installation
```

## Installation

### Prerequisites

- Python 3.9 or higher

### Option 1: Using pip

1. Clone the repository
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

### Option 2: Development Installation

1. Clone the repository
2. Install in development mode:
   ```
   pip install -e .
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```
   or
   ```
   streamlit run src/app.py
   ```

2. Enter a tweet or text in the input area
3. Click "Analyze Tweet" to see the sentiment analysis result

## Features

- Simple text input for tweet analysis
- Example tweets for testing
- Clean, minimal output showing sentiment (Positive/Negative) with emoji
