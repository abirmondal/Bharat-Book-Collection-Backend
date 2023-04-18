import pickle
import pandas as pd
import numpy as np

def getBookbyISBN(isbn):
    data = pd.read_pickle('./pickle files/book_with_ratings.pkl')
    return data[data['ISBN'] == isbn].to_dict(orient="records")

def getTopBooks(page = 1, perPage = 9):
    start_limit = (page - 1) * perPage
    end_limit = start_limit + perPage
    data = pd.read_pickle('./pickle files/popular_ratings.pkl')
    return data.iloc[start_limit:end_limit].to_dict(orient="records")

def getRecommendationByTitle(title):
    fileOpen = open('./pickle files/pt.pkl', "rb")
    pt = pickle.load(fileOpen)
    fileOpen = open('./pickle files/similarity_scores.pkl', "rb")
    similarity_scores = pickle.load(fileOpen)
    fileOpen = open('./pickle files/similarity_scores.pkl', "rb")
    similarity_scores = pickle.load(fileOpen)
    books = pd.read_pickle('./pickle files/book_with_ratings.pkl')

    data = []
    index = np.where(pt.index==title)[0]
    if len(index) == 0:
        return data
    else:
        index = index[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:4]

    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        data.append(temp_df.to_dict(orient="records"))

    return data
