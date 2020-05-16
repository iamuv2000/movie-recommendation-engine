#Import modules
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



#Read csv
dataset = pd.read_csv('movie_dataset.csv')
print(dataset.head())


# Helper functions

#Get Title from index
def get_title_from_index(index):
    return dataset[dataset.index == index]['title'].values[0]

#Get index from title
def get_index_from_title(title):
    return dataset[dataset.title == title]['index'].values[0]


#Select Features
features = ['keywords' , 'cast' , 'genres' , 'director']


# Clean data
for feature in features:
    dataset[feature] = dataset[feature].fillna('')


#Create column in dataframe which combines all the selected features
def combine_features(rows):
    return rows['keywords'] + " " +  rows['cast'] + " " +  rows['genres'] + " " +  rows['director']

dataset["combined_features"] = dataset.apply(combine_features , axis = 1)

# Create count feature from this new combined column
cv = CountVectorizer()

count_matrix = cv.fit_transform(dataset["combined_features"])

# Calculate cosine similarity based on count_matrix
cosine_sim = cosine_similarity(count_matrix)

movie_user_like = 'The Proposal'

# Get index of movie from title
movie_index = get_index_from_title(movie_user_like)


# Find similar movie in descending order of similarity score
similar_movie = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movie, key = lambda x:x[1], reverse = True)

i = 0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i = i+1
    if i > 20:
        break


#TODO: Test accuracy with release date
#TODO: Clean search term (ignore case)
#TODO: Use cosine similarity to auto detect close enough search term
#TODO: Add title not found case
#TODO: Allow variable number of recommendations
#TODO: Make a parent function
#TODO: Make a flask endpoint
#TODO: Make a frontend