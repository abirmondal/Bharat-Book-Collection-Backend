import pickle

def getBookbyISBN(isbn):
    fileOpen = open('./pickle files/popular_ratings.pkl', "rb")
    data = pickle.load(fileOpen)
    return data[data['ISBN'] == isbn].to_dict(orient="records")

