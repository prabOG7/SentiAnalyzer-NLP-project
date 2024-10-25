from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return "Positive"
    elif scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example usage
question = "I'm really excited to learn about NLP and sentiment analysis!"
sentiment = analyze_sentiment(question)
print(f"The sentiment of the question is: {sentiment}")