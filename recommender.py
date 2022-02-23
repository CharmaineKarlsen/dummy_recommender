"""
contains function for recommending random movies
"""

def recommend_random(movies, k=10):
    """
    Recommends a list of k random movie ids
    """
    return movies['title'].sample(k).to_list()
