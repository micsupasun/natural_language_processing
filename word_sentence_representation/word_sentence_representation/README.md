# Project
all types of word sentence representation

# Problem
create sentence and separate word in sentence with One hot encoding(bag of words), Count Vectorizer, TF-IDF, Word Embedding, Word2Vec

# Solution
we can separate word in sentence with One hot encoding(bag of words), Count Vectorizer, TF-IDF, Word Embedding, Word2Vec

# Methodology
1. One hot encoding with Pythainlp (for Thai words)
- install library
- create sentence
- word tokenization
- list unique word
- map id and unique word with a dictionary
- generate one hot encoding in a sentence

2. One hot encoding with pandas
- install library
- import library
- create sentences
- separate all the words in a sentence
- temp all the words and sentences in a data frame
- generate one hot encoding with getting dummies in pandas

3. One-Hot Encoding with SCIKIT-LEARN
- install library
- import library
- create sentences
- word tokenization
- one hot encoding with MultiLabelBinarizer

4. Count Vectorizer
- import CountVectorizer
- create sentence
- transform and get a feature
- create one hot encoding and add frequency

5. TF-IDF
- import TfidfVectorizer
- create sentence
- transform and get a feature
- generate TF-IDF in each sentence

6. Word Embedding
- create sentences
- Co-Occurrence matrix by Numpy to a data frame
- use Co-Occurrence matrix by linear algebra
- plot 3D matrix for acceptable relation word in a sentence

7. Word2Vec
- Install library
- Install Dataset
- Import Library
- pre-processing
    - word_tokenize
    - set parameter for training word2vec
- train model
    - train word2vec by Gensim library
    - build vocab
- predict most similar from a defined word
- visualization
    - define word
    - find the id for map id and word
    - reduce 100 dimensions to 2-3 dimension
    - split word and prepare for a plot in index and vector
    - visualization two dimension
- predict a similar score in 2 word