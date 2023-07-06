# Project
named entity recognition in English and Thai word

# Problem
Develop a system that can automatically identify and classify named entities in English and Thai texts. Named entities refer to specific entities such as person names, organization names, locations, dates, and other proper nouns. In English, named entity recognition (NER) is a well-studied problem, and various techniques have been developed to address it. However, the Thai language poses challenges due to its unique characteristics, such as having no explicit word boundaries and complex word segmentation rules.

# Solution
- Data Preprocessing: Processing the raw text data to handle language-specific challenges, such as word segmentation in Thai and tokenization in English.
- Feature Extraction: Extracting relevant features from the text, such as word embeddings, part-of-speech tags, and context information, to represent each word in the input text.
- Model Selection: Choosing an appropriate machine learning or deep learning model for named entity recognition. This includes the Bert NLP model

# Methodology
1. NLTK
- import library
- create sentence
- predict the function of words in a sentence
2. SPACY
- import library
- create sentence
- predict the function and start and end of words in a sentence
3. BERT NLP
- install transformers
- import library
- create sentence
- tokenization and pre-train with Bert
- predict the function and start and end and a score of words in a sentence
4. PythaiNLP(predict Thai language)
- install pythainlp
- import library
- create sentence
- use Pythainlp to predict named entity recognition in Thai word