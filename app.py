import streamlit as st
from recommend import movies, recommend
# Set the page configuration
st.set_page_config(page_title="Movie Gallery", layout="wide")

page_bg_img = '''
<style>
.main-header {
    font-size: 48px;
    color: #FF6347;
    text-align: center;
    font-family: 'Arial Black', sans-serif;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px #000000;
}

.sub-header {
    font-size: 24px;
    color: #4682B4;
    text-align: center;
    margin-bottom: 20px;
    font-family: 'Arial', sans-serif;
    text-shadow: 2px 2px 4px #000000;
}

.description {
    font-size: 18px;
    color: #FFD700;
    text-align: center;
    margin-bottom: 50px;
    font-family: 'Verdana', sans-serif;
    text-shadow: 1px 1px 2px #000000;
}

.caption {
    font-size: 14px !important;
    color: #FFFFFF;
    word-wrap: break-word !important;
    white-space: normal !important;
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-weight: bold;
    text-shadow: 1px 1px 2px #000000;
}

.movie-column {
    padding: 10px;
}

.footer {
    font-size: 16px;
    color: #808080;
    text-align: center;
    margin-top: 50px;
    font-family: 'Roboto', sans-serif;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Display header and subheader
st.markdown('<div class="main-header">Welcome to the Movie Gallery</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Find Your Favorite Movies</div>', unsafe_allow_html=True)

# # Add a brief description
# st.markdown('<div class="description">Browse through some of the most iconic movies and discover your next watch. '
#             'Click on any movie to learn more!</div>', unsafe_allow_html=True)


# Select-box for movie selection
selected_movie_name = st.selectbox(
    "Choose a movie",
    movies['title'].values,
    index=None,
    placeholder="Select an option..."
)

# Button for recommendation
clicked = st.button("Recommend")

if clicked and (selected_movie_name==None):
    st.write("Please select a movie.")
elif clicked:
    my_recommendations = recommend(selected_movie_name)
    col = st.columns(5, gap="large")
    for i in range(0, 5):
        with col[i]:
            st.image(my_recommendations['image'][i], use_column_width=True)
            st.markdown(f"<div class='caption'>{my_recommendations['caption'][i]}</div>",
                        unsafe_allow_html=True)

# Add a footer or a call to action
st.markdown(
    """
    <div class="footer">
        Thank you for visiting the Movie Gallery. Come back soon for more updates!
    </div>
    """,
    unsafe_allow_html=True
)
