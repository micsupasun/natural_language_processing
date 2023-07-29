# Project
visualization, text representation, and prediction text classification in the Twitter application about Coronavirus.

# Problem
The problem in this project is related to natural language processing (NLP) and text classification. The main challenges involved in this project include:

Data Cleaning: The raw data collected from sources like Twitter might contain various elements that must be cleaned and preprocessed before modeling. These elements include stopwords (commonly occurring words that do not add much meaning), hashtags, emojis, special characters, Removed punctuations, links, mentions, special characters, etc.

Text Classification: The goal will likely be to classify text data into different categories or labels using machine learning or deep learning models. In this case, the models used for prediction are BERT (Bidirectional Encoder Representations from Transformers) and Roberta (A variant of BERT).

Model Selection and Training: Selecting the appropriate pre-trained language model (BERT or Roberta) and fine-tuning it on the cleaned data for the specific classification task.

Data Imbalance: Handling class imbalance in the dataset, where certain categories may have significantly more or fewer samples than others.

Performance Metrics: Choosing the right performance metrics to evaluate the model's performance, such as accuracy, precision, recall, F1-score, etc.

# Solution
we can clean Twitter text and predict the Transformer model with Bert and Roberta.

# Methodology
1. Visualization
    - Statistics
    - class distribution
    - Number of characters
    - Number of words in a tweet
    - Average word length in a tweet
    - WordCloud
    - Number of Punctuations
    - Common Words
    - Hashtags
    - Mentions
    - N-grams(Unigrams, Bi grams, Tri-grams)
2. Text Representation
    - clean data and tokenization
    - One-Hot Encoding
    - Bag of words
    - Bag of N-Grams
    - TF-IDF
    - Word2vec Word Embeddings
    - Glove Word Embeddings
    - FastText Word Embeddings
3. prediction
    - Exploratory Data Analysis
    - Clean Data in a text (clean emojis, punctuations, links, mentions, hashtags, special characters, multiple spaces)
    - use Bert to find not English words and delete not English words in train and test
    - convert 5 labels(Positive, Negative, Neutral, Extremely Positive, Extremely Negative) to 3 labels(Positive, Negative, Neutral)
    - Class Balancing by RandomOverSampler
    - train model with Naive Bayes Classifier
    - train model with BERT
    - train model with Roberta
    - visualization result with a confusion matrix, classification report, accuracy, f1-score
