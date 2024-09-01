import requests
import pandas as pd
import pickle

movies_dict = pickle.load(open('movies.pkl', "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', "rb"))


# Fetching posters of movies using movie id
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0dd7942fe285858a3ea68dd9ee4271d0')
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


# Main function that finds 5 similar types of movies based on the content of the movie provided
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_list = {
        "image": [],
        "caption": [],
    }
    for i in movie_list:
        recommended_movies_list['caption'].append(movies.iloc[i[0]].title)
        recommended_movies_list['image'].append(fetch_poster(movies.iloc[i[0]].movie_id))

    return recommended_movies_list
