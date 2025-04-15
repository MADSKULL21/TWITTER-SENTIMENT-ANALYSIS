from setuptools import setup, find_packages

setup(
    name="tweet-sentiment-analysis",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.31.0",
        "scikit-learn>=1.6.1",
        "nltk>=3.8.1",
        "numpy>=1.26.0",
    ],
    python_requires=">=3.9",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple application that analyzes the sentiment of tweets or text input",
    keywords="sentiment analysis, twitter, nlp",
    url="https://github.com/yourusername/tweet-sentiment-analysis",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
