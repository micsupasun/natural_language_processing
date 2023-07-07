# Project
custom Bert NLP for work on Text Classification and Thai Question Answering

# Problem
adapting the pre-trained BERT model to the specific task at hand. BERT (Bidirectional Encoder Representations from Transformers) is a powerful language representation model pre-trained on large amounts of text data. However, it requires further modifications and fine-tuning to be effectively used for different NLP tasks. Here are the key challenges and solutions when customizing BERT for other tasks

# Solution
we create custom Bert NLP for work in Text Classification and Thai Question Answering.

# Methodology
1. Install Library
2. import pretrained file
3. fill pre-train in AutoTokenizer for cut word depend on our pre-train
4. Preprocessing
5. Fill Mask
6. Text Classification (Wongnai Dataset)
    - install library
    - import dataset
    - generate train and evaluate set
    - train bert nlp
    - predict text classification by bert nlp
7. Text Classification with Custom Dataset (True Voice Intent)
    - import dataset
    - Preprocessing
    - LabelEncoder
    - train_test_split
    - create train test validation set and transfrom them
    - train bert nlp
    - predict text classification by bert nlp
8. Thai Question Answering (Thai QA)
    - Data Preprocessing
    - sepearate word by word tokenization
    - create context text feature
    - create question wordseqqed feature
    - create question wordseqqed feature
    - create answer starts feature
    - train data
    - fine tuning by bert nlp