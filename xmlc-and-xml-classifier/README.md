# Objective
the objective of this assignment is to get practical experience in designing, implementing, running and scientifically evaluating your own XML classifier. The dataset will be a collection of two very large-scale resources of scientific papers in economics and medicine. Each `document’ in this dataset represents a record from a large document corpus. You can also use further datasets of your choice.


# Step of work
This is step of work in this project
1. Import Library
2. Import 2 datasets are Pebmed and Econbiz
3. Data preprocessing
4. clean the data with Capital to small character
5. clean the data with Stop word(delete useless word in,the,a,is,for)
6. clean the data with Lemmatization which is the process of converting a word with a list of words in a dictionary, proper grammatical analysis of the language to transform and conjugate words to eliminate inflection of words such as gender, tense, sound, mood, number, etc. Most will cut the footer. Leave only the basic form, which is a word in the dictionary called Lemma. For example, saw with Stemming works best with s, but with Lemmatization can work see or saw, depending on whether it is a Noun or Verb. After that we will do Stemming. It cuts the end of the word coarsely with a simple pattern, which works quite well. For most, but not all, English words, stemming reduces form.
7. clean the data with stem (fix same mean such as good better best)
8. clean the data with stem regular expression(Removes numbers, Removes single characters, Removes multiple spaces)
9. Tokenize the title sample for checking stopwords
10. clean label to numpy
11. one hot encoding label with MultiLabelBinarizer
12. train test split
13. train multiple models and mutiple datasets
14. metric performance with accuracy and confusion matrix 


# Result
This project use 10 models to train model including

1. Logistic Regression

2. Random Forest

3. Naive Bayes

4. Decision Tree

5. K-nearest neighbors

6. SVC

7. XGBoost

8. SGD

9. Multilayer Perceptron

10. Extra Trees

and 2 datasets: Pebmed and Econbiz
The most accuracy is CNN in pebmed dataset and naive bayes in econbiz dataset