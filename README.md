# 📰 Fake News Detection using Machine Learning

## 📌 Project Overview

The Fake News Detection System is an Artificial Intelligence and Machine Learning project developed to classify news articles as **Real** or **Fake** using Natural Language Processing (NLP) techniques. With the rapid spread of misinformation through digital platforms, detecting fake news has become an important challenge. This project aims to automate the identification of misleading news content by analyzing textual information and applying machine learning algorithms.

The project utilizes text preprocessing techniques, TF-IDF vectorization, and multiple classification models to determine the authenticity of news articles. The performance of different machine learning models is evaluated using various metrics such as Accuracy, Precision, Recall, and F1-Score.

---

## 🎯 Objectives

* To preprocess and clean textual news data.
* To transform text into numerical features using TF-IDF Vectorization.
* To build and evaluate multiple machine learning models for fake news classification.
* To compare model performances using standard evaluation metrics.
* To deploy the best-performing model for predicting unseen news articles.

---

## 📂 Dataset

The dataset used in this project consists of two CSV files:

* **Fake.csv** – Contains fake news articles.
* **True.csv** – Contains genuine news articles.

The dataset was obtained from Kaggle and balanced before model training.

### Dataset Features

| Feature | Description                          |
| ------- | ------------------------------------ |
| title   | Title of the news article            |
| text    | Main content of the article          |
| subject | News category                        |
| date    | Publication date                     |
| label   | Target variable (0 = Fake, 1 = Real) |

---

## 🛠 Technologies Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib

---

## ⚙ Methodology

### 1. Data Collection

The Fake and Real News datasets were imported and combined into a single dataset.

### 2. Data Preprocessing

The following preprocessing steps were performed:

* Converted text to lowercase.
* Removed URLs.
* Removed HTML tags.
* Removed punctuation marks.
* Removed numerical values.
* Removed extra white spaces.

### 3. Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency) Vectorization was used to convert textual data into numerical representations suitable for machine learning algorithms.

### 4. Train-Test Split

The dataset was divided into training and testing sets using an 80:20 ratio.

### 5. Model Building

The following machine learning models were implemented:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

### 6. Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## 📊 Results

| Model               | Accuracy  | Precision | Recall   | F1-Score |
| ------------------- | --------- | --------- | -------- | -------- |
| Logistic Regression | 98% – 99% | High      | High     | High     |
| Decision Tree       | 88% – 93% | Moderate  | Moderate | Moderate |
| Random Forest       | 92% – 96% | High      | High     | High     |

**Logistic Regression achieved the best overall performance and was selected as the final model for deployment.**

---

## 📈 Visualizations Included

* Distribution of Fake and Real News
* News Article Length Distribution
* Confusion Matrix
* Classification Metrics Comparison
* Model Performance Comparison Graph

---

## 💾 Model Deployment

The best-performing model (Logistic Regression) and the TF-IDF vectorizer were serialized using Joblib.

Generated files:

* `model.pkl`
* `vectorizer.pkl`

These files can be integrated into a Streamlit web application for real-time predictions.

---

## 🚀 How to Run the Project

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd Fake-News-Detection
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Open the Jupyter Notebook.

```bash
jupyter notebook
```

5. Run all notebook cells sequentially.

---

## 📁 Project Structure

```text
Fake-News-Detection/
│
├── Fake.csv
├── True.csv
├── Fakenews_detection.ipynb
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## 🔮 Future Enhancements

* Develop a Streamlit-based user interface.
* Integrate advanced NLP models such as BERT and RoBERTa.
* Enable real-time news verification through API integration.
* Expand the dataset to improve model generalization.

---

## Conclusion

This project demonstrates the application of Machine Learning and Natural Language Processing techniques in addressing the growing issue of fake news dissemination. By comparing multiple classification algorithms, Logistic Regression was identified as the most effective model for detecting fake news with high accuracy and reliability. The developed system provides a practical approach for automated news verification and can be further enhanced using deep learning methodologies.

---

### Author

**Achyuth Kumar**

B.Tech – Computer Science and Engineering (Data Analytics)

Vellore Institute of Technology, Amaravati
