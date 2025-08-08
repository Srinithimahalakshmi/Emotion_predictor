# test_input.py

import joblib

# Load model
model = joblib.load("emotion_model_nb.joblib")

# Sample input
sample_comments = [
    "I can't believe this happened!",
    "Wow, what a beautiful day!",
    "I'm scared to even try again."
]

# Predict
predicted_emotions = model.predict(sample_comments)

# Output results
for comment, emotion in zip(sample_comments, predicted_emotions):
    print(f"Comment: {comment}\nPredicted Emotion: {emotion}\n")
