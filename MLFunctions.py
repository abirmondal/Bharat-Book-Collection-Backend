import pickle

def getBookbyISBN(isbn):
    fileOpen = open('./pickle files/popular_ratings.pkl', "rb")
    data = pickle.load(fileOpen)
    return data[data['ISBN'] == isbn].to_dict(orient="records")

def getTopBooks(start = 0, end = 9):
    fileOpen = open('./pickle files/popular_ratings.pkl', "rb")
    data = pickle.load(fileOpen)
    return data.iloc[start:end].to_dict(orient="records")
