
#  Emotion Predictor (Naive Bayes)

##  Overview
A text-based emotion classification system powered by a **Naive Bayes** classifier. It transforms user input—whether text or speech transcription—into one of several emotions such as **Joy**, **Anger**, **Sadness**, or **Surprise**, using TF-IDF vectorization and a clean, interactive interface.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Emotion_predictor.git
cd Emotion_predictor

python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### Notebook Exploration & Training

Run the notebook to perform data cleaning, feature extraction via TF-IDF, training, and evaluation:

```bash
jupyter notebook model_training.ipynb
```

### Launch Web Interface

Start the Flask application to test predictions interactively:

```bash
python app.py
```

Then visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser, input text, and let the model infer your emotion!

### Quick CLI Testing

Use the `test.py` script to classify sample phrases like so:

```bash
python test.py "I just got my dream job!"
```

---

## Project Structure

```
Emotion_predictor/
├── Emotion_classify_Data.csv     # Dataset with labeled emotion samples
├── model_training.ipynb          # Notebook for model training & evaluation
├── emotion_model_nb.joblib       # Saved Naive Bayes emotion classifier
├── app.py                         # Flask app for interactive predictions
├── test.py                        # CLI script for quick emotion detection
├── templates/
│   └── index.html                # Web UI template
├── static/
│   └── style.css                 # Stylesheet for the web interface
├── requirements.txt              # Project dependencies
└── README.md                     # Documentation (this file)
```

---

## Results

* Display model performance metrics such as **Accuracy**, **Precision**, **Recall**, and **F1-Score**.
* Include visuals like a **confusion matrix**, classification reports, or bar charts—embedded within the notebook or linked from the `results/` folder.

---

## Contributing

Contributions are highly encouraged! You can help by:

* Enhancing data preprocessing or expanding the dataset
* Experimenting with different models (e.g., SVM, Log-Regression, or Neural Networks)
* Adding detailed evaluation metrics or visualizations
* Improving the frontend UI or adding accessibility features

**To contribute:**

1. Fork this repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add <feature>"`
4. Push and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If this project helped you, please consider giving it a star!*

