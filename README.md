
#  Emotion Predictor (Naive Bayes)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)]()

##  Overview
This project leverages **Naive Bayes** to classify text or speech data into emotions such as **Joy**, **Anger**, **Sadness**, and **Surprise**. It includes data cleaning, TF-IDF feature extraction, model training, evaluation, and a user-friendly web interface powered by Flask.

---

##  Features
-  **Data Cleaning**: Preprocesses raw text or speech transcriptions to prepare for modeling  
-  **Feature Extraction**: Utilizes TF-IDF vectors to capture meaningful patterns  
-  **Model Training**: Trains a Naive Bayes classifier for emotion detection  
-  **Web App**: Flask-based interface (`app.py`, `templates/`, `static/`) for interactive predictions  
-  **Notebook Insights**: `model_training.ipynb` contains exploratory analysis and model evaluation visuals  

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  
- [📬 Contact](#-contact)  

---

##  Installation

```bash
git clone https://github.com/Srinithimahalakshmi/Emotion_predictor.git
cd Emotion_predictor

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### 1. Notebook Exploration & Model Training

Run the notebook for data analysis and model training:

```bash
jupyter notebook model_training.ipynb
```

### 2. Run the Flask Web App

Start the server to make predictions interactively:

```bash
python app.py
```

Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser, enter input, and let it detect your emotion!

### 3. Command-Line Testing

Use `test.py` to classify sample inputs and view predictions via the console.

---

## Project Structure

| File / Folder               | Description                                 |
| --------------------------- | ------------------------------------------- |
| `Emotion_classify_Data.csv` | Dataset for model training                  |
| `model_training.ipynb`      | Notebook with EDA, training, and evaluation |
| `emotion_model_nb.joblib`   | Serialized Naive Bayes model                |
| `app.py`                    | Flask web application                       |
| `templates/` & `static/`    | Frontend HTML/CSS components                |
| `test.py`                   | Script for quick CLI-based testing          |

---

## Results

Report the model’s performance metrics (accuracy, precision, recall, F1-score) from the notebook. Embed visuals like confusion matrices or classification reports to showcase model efficacy.

---

## Contributing

Contributions are warmly welcome! You could help with:

* Improving preprocessing or feature extraction
* Enhancing model performance or adding new algorithms
* Polishing the web UI design
* Expanding documentation or adding sample data

**To contribute**:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make your changes & commit (`git commit -m "Add new feature"`)
4. Push and open a Pull Request

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com]
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

Thank you for checking out this project! If you find it useful, a ⭐ would be greatly appreciated!
