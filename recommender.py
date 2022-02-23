"""
contains various implementations for recommending movies
"""

import pandas as pd
from utils import movies, ratings


# recommender_systems_intro_filled.ipynb
def recommend_random(query, ratings, k=10):
    """
    Recommends a list of k random movie ids
    """
    return [1, 20, 34, 25]


if __name__=='__main__':
    # list of liked movies
    query = [1, 34, 56, 21]
    print(recommend_random(query, movies))
