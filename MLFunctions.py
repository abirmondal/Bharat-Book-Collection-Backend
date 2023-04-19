import pickle
import pandas as pd
import numpy as np

def getTopBooks(page = 1, perPage = 9):
    start_limit = (page - 1) * perPage
    end_limit = start_limit + perPage
    data = pd.read_pickle('./pickle files/popular_ratings.pkl')
    return data.iloc[start_limit:end_limit].to_dict(orient="records")

def getBookDetAndRecommend(isbn, perPage = 5):
    fileOpen = open('./pickle files/pt.pkl', "rb")
    pt = pickle.load(fileOpen)
    fileOpen = open('./pickle files/similarity_scores.pkl', "rb")
    similarity_scores = pickle.load(fileOpen)
    fileOpen = open('./pickle files/similarity_scores.pkl', "rb")
    similarity_scores = pickle.load(fileOpen)
    books = pd.read_pickle('./pickle files/book_with_ratings.pkl')

    data = {}
    data['Book-Details'] = books[books['ISBN'] == isbn].to_dict(orient="records")
    data['Book-Recommendation'] = []
    if len(data['Book-Details']) == 0:
        return data
    title = data['Book-Details'][0]['Book-Title']
    index = np.where(pt.index==title)[0]
    if len(index) == 0:
        return data
    else:
        index = index[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:(perPage+1)]

    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        temp_df_min = temp_df[['ISBN', 'Book-Title', 'Book-Author','Image-URL-L', 'Number of Ratings','Average Ratings']]
        data['Book-Recommendation'].append(temp_df_min.to_dict(orient="records"))

    return data
