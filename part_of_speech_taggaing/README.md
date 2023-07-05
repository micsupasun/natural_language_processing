# Project
part of speech tagging in English and Thai words

# Problem
Define part of speech tagging. The following features can be used:
- Is the first letter capitalized?
- Is it the first word in the sentence?
- Is it the last word?
- What is the prefix of the word?
- What is the suffix of the word?
- Is the complete word capitalized
- What is the previous word?
- What is the next word?
- Is it numeric?
- Is it alphaunumeric?
- Is there a hyphen in the word?

# Solution
we can find all duty of part of speech word

# Methodology
1. Import Library
2. Import Dataset
3. Machine Learning with CRF
- create features
- clean data
- train test split
4. Deep Learning
- clean data
- train test split
- train data with the LSTM model
5. NLTK
- work tokenize
- part of speech tagging words
6. PythaiNLP(predict for Thai words)
- word tokenize
- part of speech tagging words