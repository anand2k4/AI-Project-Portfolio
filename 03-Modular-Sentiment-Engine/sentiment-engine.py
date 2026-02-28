#                        Classification Function
def classify_review(review):
    review = review.lower()

    positive_keywords = ["good", "amazing", "excellent", "loved", "fantastic", "superb"]
    negative_keywords = ["bad", "worst", "boring", "terrible", "poor"]

    for word in positive_keywords:
        if word in review:
            return "Positive"

    for word in negative_keywords:
        if word in review:
            return "Negative"

    return "Neutral"

#                             Dateset
reviews = [
    "This movie was good",
    "Very bad acting",
    "Amazing storyline",
    "The film was boring",
    "Excellent direction",
    "Worst movie ever",
    "Loved the music",
    "Terrible screenplay",
    "Average film",
    "Superb experience"
]
#                          Analysis Engine
positive_count = 0
negative_count = 0
neutral_count = 0

for review in reviews:
    result = classify_review(review)

    if result == "Positive":
        positive_count += 1
    elif result == "Negative":
        negative_count += 1
    else:
        neutral_count += 1

    print(f"Review: {review}")
    print(f"Sentiment: {result}")
    print("-------------------")

#                          Summary Report
total = len(reviews)

print("===== Summary Report =====")
print("Total Reviews:", total)
print("Positive:", positive_count)
print("Negative:", negative_count)
print("Neutral:", neutral_count)

positive_percentage = (positive_count / total) * 100
print("Positive Percentage:", round(positive_percentage, 2), "%")
