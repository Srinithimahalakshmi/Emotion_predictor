# Emotion Predictor

A user-friendly web app that uses a **Naive Bayes** classifier with **TF‑IDF** feature extraction to detect emotions—like joy, anger, sadness, and surprise—from text or speech input.

---

##  Project Overview

The Emotion Predictor analyzes input data (text or speech converted to text) and classifies it into emotion categories using natural language processing and machine learning.

---

##  Repository Structure

```
├── Emotion_classify_Data.csv   # Dataset for training and evaluation
├── model_training.ipynb        # Data cleaning, TF‑IDF vectorization, model training & validation
├── emotion_model_nb.joblib     # Trained Naive Bayes model
├── app.py                      # Flask (or Streamlit) web app interface
├── test.py                     # Script for offline testing/predictions
├── templates/                  # HTML templates for the web frontend
└── static/                     # CSS/JS/images used in the frontend
```

---

##  Features

- **Data Processing**: Cleaning and preparing text data.
- **Feature Engineering**: TF‑IDF vectorization for type‑aware feature extraction.
- **Model Training**: Training a Naive Bayes classifier and evaluating performance.
- **Web App Interface**: Input text through a UI and receive emotion predictions in real-time.
- **Offline Testing**: Use `test.py` for command-line prediction without launching the web app.

---

##  Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Srinithimahalakshmi/Emotion_predictor.git
   cd Emotion_predictor
   ```

2. **Set up a virtual environment and install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Optional: Train or retrain the model**

   ```bash
   jupyter notebook model_training.ipynb
   ```

4. **Run the web application**

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000` (or depending on your framework).

6. For quick CLI tests:

   ```bash
   python test.py "I feel amazing today!"
   ```

---

##  Usage

- **Web App**: Paste or type in text/speech input, submit, and get the emotion prediction.
- **Offline CLI**: Run `test.py` with your text to see immediate output.

---

##  Dependencies

- Python 3.x
- pandas
- scikit-learn
- joblib
- Flask (or Streamlit)
- Jupyter Notebook (for development)

---

##  License

MIT License — see the [LICENSE](LICENSE) file for details.

---

##  Contact

Created by **[@Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)**. Feel free to open issues or pull requests for improvements!
