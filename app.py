import streamlit as st
import pickle
import pandas as pd
import requests

# Add translucent background poster like Netflix
background_image_url = "https://image.tmdb.org/t/p/w1280/8YFL5QQVPy3AgrEQxNYVSgiPEbe.jpg"  # Replace with any poster you like




def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c13ed5e6017f2395b6ed72aba4422d25&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    reccomended_movies_posters = []

    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        reccomended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,reccomended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity =pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
"📺 Your next favorite movie is just a search away...",
    movies['title'].values)

if st.button("Recommend"):
    names,posters= recommend(selected_movie_name)

    col1, col2, col3 , col4 , col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])



