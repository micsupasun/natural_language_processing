# Project
document classification with 3 project(word cloud, Latent Dirichlet Allocation, Sentiment Analysis)

# Problem
- Word Cloud:
Problem: Difficulty in identifying the most important or frequent terms in a document or collection of documents.

- Latent Dirichlet Allocation (LDA):
Problem: Challenges in categorizing documents into topics or themes without labeled data.

- Sentiment Analysis:
Problem: Determining the sentiment or emotional tone expressed in text data, such as customer reviews or social media posts.

# Solution
- Word Cloud:
Solution: Generate a word cloud visualization to visually represent the frequency or importance of words in the text, aiding in identifying key themes or topics.

- Latent Dirichlet Allocation (LDA):
Solution: Apply LDA, a probabilistic model, to automatically discover underlying topics in a document corpus, enabling unsupervised document classification based on topic distributions.

- Sentiment Analysis:
Solution: Employ sentiment analysis techniques to classify text into positive, negative, or neutral sentiment categories, enabling automated sentiment classification for decision-making or opinion analysis.

# Methodology
1. Pre-processing
    - Separate individual instances
    - Choose parts of instances
    - import dataset
    - word tokenization
    - cleansing data
2. Word Cloud
    - Create 'Word Cloud' from topics with the specific types
    - regular expression
    - word tokenization
    - import dataset
    - data visulization
3. Latent Dirichlet Allocation(LDA)
    - CountVectorizer
    - LatentDirichletAllocation
    - print top 10 words
4. Sentiment Analysis
    - Use 'polyglot' library since 'PyThaiNLP' has no longer supported sentiment lexicon.s