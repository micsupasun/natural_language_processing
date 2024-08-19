# Text retrieval system Project

## Objective
The objective of the project is to design a text retrieval system that can recommend movies or shows based on their descriptions. The system will be trained using a dataset of movie/show descriptions and will identify the top three most similar titles to a given input description from a test set.

## Step
1. Import Library
2. Import File
3. Data Preprocessing
- Capital to small
- Stop word
- Lemmatization
- Stemming
- Regular Expression
4. Data Visualization
5. TF-IDF with inverted file algorithm
6. model
- SVM model
- CNN model
7. Similarity Computation
- Cosine Similarity
- Retrieve Top 3 Matches

## Result
1. The text retrieval system will output the top 3 most similar movies/shows for each description in the test.csv file.
2. The system's performance will be evaluated and discussed in the presentation, along with the challenges faced and the improvements made during the development process.

## Documentation
1. train.csv: Contains the training data with columns for title and description. This file will be used to train the text retrieval system.
2. test.csv: Contains the test data with columns for title and description. This file will be used to evaluate the system's performance.
3. text_retrieval_system.ipynb: A Jupyter notebook containing the Python code implementing the text retrieval system. It includes all steps from data loading, preprocessing, and TF-IDF calculation to similarity computation and retrieval of results.