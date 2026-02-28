reviews = [
    "This movie was good",
    "Very bad acting",
    "Amazing storyline",
    "The film was boring",
    "Excellent direction",
    "Worst movie ever",
    "Loved the music",
    "Terrible screenplay",
    "Good performances",
    "Bad editing",
    "Fantastic visuals",
    "Not good at all",
    "Superb experience",
    "Poor dialogue",
    "Really good movie"]

# Initialize Counters
positive_count = 0 
negative_count = 0
neutral_count = 0


# Classification Logic
for review in reviews:
    review = review.lower()

    if "good" in review or "amazing" in review or "excellent" in review or "loved" in review or "fantastic" in review or "superb" in review:
        positive_count += 1
   
    elif "bad" in review or "worst" in review or "boring" in review or "terrible" in review or "poor" in review:
        negative_count += 1
    
    else:
        neutral_count += 1


total_reviews = len(reviews)

positive_percentage = (positive_count / total_reviews) * 100

print("Total Reviews:", len(reviews))
print("Positive Reviews:", positive_count)
print("Negative Reviews:", negative_count)
print("Neutral Reviews:", neutral_count)
print("Positive Percentage:", round(positive_percentage, 2), "%")