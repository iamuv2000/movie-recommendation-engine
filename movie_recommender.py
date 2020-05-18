#Import modules
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_movie_recommendation(movie_user_like, no_of_movies):
    #Read csv
    dataset = pd.read_csv('movie_dataset.csv')

    # Helper functions

    #Get Title from index
    def get_title_from_index(index):
        return dataset[dataset.index == index]['title'].values[0]
    
    #Get Votes from index
    def get_votes_from_index(index):
        return dataset[dataset.index == index]['vote_average'].values[0]

    #Get director from index
    def get_director_from_index(index):
        return dataset[dataset.index == index]['director'].values[0]

    #Get overview from index
    def get_overview_from_index(index):
        return dataset[dataset.index == index]['overview'].values[0]

    #Get index from title
    def get_index_from_title(title):
        title = title.lower()
        dataset['title'] = dataset['title'].str.lower() 
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

    # Get index of movie from title
    try:
        movie_index = get_index_from_title(movie_user_like)
    except:
        print("Movie not found in database")
        return 0


    # Find similar movie in descending order of similarity score
    similar_movie = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movie, key = lambda x:x[1], reverse = True)

    i = 0
    movies = []
    for movie in sorted_similar_movies:
        title = get_title_from_index(movie[0]).title()
        votes = get_votes_from_index(movie[0])
        director = get_director_from_index(movie[0])
        overview = get_overview_from_index(movie[0])
        movieObj = {
            "title" : title,
            "votes" : votes,
            "director" : director,
            "overview" : overview
        }
        print(movieObj)
        movies.append(movieObj)
        i = i + 1
        if i > no_of_movies:
            break
    return movies 

#TODO: Test accuracy with release date
#TODO: Use cosine similarity to auto detect close enough search term
#TODO: Make a frontend