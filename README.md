# 📰 Fake News Detection – Pinnacle Labs Internship (Task 1)

This project implements a **Fake News Detection Web App** using **Logistic Regression** with **TF-IDF features**.  
The model achieves **91% accuracy** on the evaluation split.  

The app provides a simple interface where users can enter a news title and article content, and instantly get a prediction on whether the news is **Fake** or **Real**.

---

## 🚀 Features
- ✅ Logistic Regression Classifier trained on combined `title + text` content.  
- ✅ TF-IDF Vectorization for effective text representation.  
- ✅ Streamlit Web App for real-time predictions and user-friendly interaction.  
- ✅ Accuracy: ~91% on held-out evaluation data.  

---

## 📂 Project Structure
```
├── app.py                # Streamlit application
├── model.ipynb           # Training & evaluation notebook
├── dataset/
│   └── news.csv          # Dataset with title, text, label
├── models/
│   ├── model.pkl         # Trained Logistic Regression model
│   └── vectorizer.pkl    # TF-IDF vectorizer
└── README.md             # Project documentation
```

---

## ⚙️ Getting Started

### 🔧 Environment
- **Python 3.9+** recommended  
- Key libraries:  
  - `pandas`  
  - `scikit-learn`  
  - `streamlit`  
  - `pickle`  

### 📦 Install dependencies
```bash
pip install streamlit scikit-learn pandas
```

### 🏋️‍♂️ Train and export artifacts (Optional)
Run the `model.ipynb` notebook to:  
- Load dataset  
- Preprocess text  
- Train **Logistic Regression** with **TF-IDF**  
- Export trained `model.pkl` and `vectorizer.pkl` to the `models/` folder  

### ▶️ Run the app
Update paths in `app.py` if needed, then start the app with:
```bash
streamlit run app.py
```

---

## 💻 Usage
1. Enter a **news title** and/or the **article text**.  
2. Click **Predict**.  
3. The app will display whether the news is **Fake** or **Real**.  

---

## 📊 Model Details
- **Vectorizer:** `TfidfVectorizer` on combined *title + text*.  
- **Classifier:** `LogisticRegression(max_iter=1000)`  
- **Reported Accuracy:** 91% on evaluation split.  

---




## 🔮 Future Improvements
- 📝 Implement advanced **text preprocessing** (stopwords, punctuation removal, n-grams).  
- ⚖️ Balance dataset and report detailed metrics (Precision, Recall, F1, Confusion Matrix).  
- ⚡ Use `st.cache_resource` and **relative paths** for better portability.  
- 🤖 Explore advanced ML/NLP models (SVM, Random Forest, Transformers like BERT).  
- 🌐 Deploy app on **Streamlit Cloud**, **Heroku**, or **AWS** for public access.  

---

## 🙌 Credits
Developed as part of **Pinnacle Labs Internship – Task 1**.  

---
