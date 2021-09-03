from textblob import TextBlob

reviews = [
    'I love this app, it is amazing ',
    "The experience using this app was bad as hell",
    "This app is really helpful",
    "Damn the app is a piece os shit",
    'Don\'t download the app you will regret it'
]

positive_reviews = []
negative_reviews = []

for review in reviews:
    review_polarity, review_subjectivity = TextBlob(review).sentiment
    review_sentiment = {
        'review': review,
        'polarity': review_polarity,
        'subjectivity': review_subjectivity
    }
    if review_polarity > 0:
        positive_reviews.append(review_sentiment)
    else:
        negative_reviews.append(review_sentiment)

print()
print('Positive Reviews:')
print(positive_reviews)
print()
print('Negative Reviews:')
print(negative_reviews)
print()
