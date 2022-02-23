''' 
testing test
'''

import pandas as pd
from recommender import recommend_random

# testing the recommend_random function to check length equals 10
def test_recommender():
    """
    testing recommender
    """
    movies = pd.read_csv('./data/movies.csv')
    recommendations = recommend_random(movies=movies,k=10)
    assert len(recommendations)==10
