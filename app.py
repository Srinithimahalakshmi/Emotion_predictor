from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("emotion_model_nb.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    comment = ""
    if request.method == "POST":
        comment = request.form["comment"]
        prediction = model.predict([comment])[0]
    return render_template("index.html", prediction=prediction, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
