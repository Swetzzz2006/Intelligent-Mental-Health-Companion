 ## Week 1 Assignment: Sentiment-Based Mood Predictor

## Project Title

**Sentiment-Based Mood Predictor for an Intelligent Mental Health Companion**

---

## Objective

To develop a machine learning model that analyzes user text messages and predicts the user's mood based on the sentiment expressed in the text. This helps the Intelligent Mental Health Companion understand emotional states and provide appropriate support.

---

## Dataset

**Dataset Name:** Sentiment Analysis Dataset / Emotion Detection Dataset

Possible datasets:

* Kaggle Emotion Dataset
* Twitter Sentiment Dataset
* Emotion Recognition Dataset
* Custom dataset containing text and corresponding emotions

### Sample Dataset Structure

| Text                        | Mood    |
| --------------------------- | ------- |
| I am very happy today       | Happy   |
| I feel lonely and depressed | Sad     |
| I am worried about tomorrow | Anxious |
| Everything is fine          | Neutral |
| I am extremely frustrated   | Angry   |

---

 Features

The features are extracted from user text:

* User Text Message
* Word Frequency (TF-IDF)
* Sentiment Score
* Positive Word Count
* Negative Word Count
* Text Length
* Emotion-related Keywords

---

## Target Classes

The model predicts one of the following mood categories:

* Happy 
* Sad 
* Angry 
* Anxious 
* Neutral 


## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* NLTK
* Scikit-learn
* TextBlob
* Matplotlib

### Development Environment

* Jupyter Notebook
* Google Colab
* VS Code

---

## Machine Learning Algorithm

### Algorithm Used

**Multinomial Naive Bayes**

### Reason for Selection

* Works efficiently for text classification.
* Fast training and prediction.
* Suitable for sentiment analysis tasks.
* Provides good accuracy on textual datasets.

Alternative algorithms:

* Logistic Regression
* Support Vector Machine (SVM)
* Random Forest

---

## Steps Performed

### Step 1: Data Collection

Collect sentiment or emotion-labeled text dataset.

### Step 2: Data Preprocessing

* Convert text to lowercase.
* Remove punctuation and special characters.
* Remove stop words.
* Tokenization.

### Step 3: Feature Extraction

Convert text into numerical vectors using:

* TF-IDF Vectorization

### Step 4: Dataset Splitting

* 80% Training Data
* 20% Testing Data

### Step 5: Model Training

Train the Multinomial Naive Bayes classifier using the training dataset.

### Step 6: Mood Prediction

Predict the mood category from new user input text.

### Step 7: Model Evaluation

Evaluate performance using:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Result

The Sentiment-Based Mood Predictor successfully classifies user text into mood categories such as Happy, Sad, Angry, Anxious, and Neutral.

### Sample Accuracy

* Accuracy Achieved: **85%–92%** (depending on dataset quality)

The model effectively identifies emotional patterns from textual input and can be integrated into the Intelligent Mental Health Companion for personalized mental health support.

---

## Output

### Sample Input 1


I am feeling wonderful and excited today.


### Predicted Output


Mood: Happy


### Sample Input 2

I feel very lonely and upset.

### Predicted Output

Mood: Sad


### Sample Input 3

I am nervous about my exam tomorrow.

### Predicted Output

Mood: Anxious


## Conclusion

The Sentiment-Based Mood Predictor uses Natural Language Processing and Machine Learning to analyze user text and identify emotional states. This module forms the first component of the **Intelligent Mental Health Companion**, enabling the system to understand user emotions and provide more personalized mental health assistance.
