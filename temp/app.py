from flask import Flask,render_template, request
import pickle
import sys
# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as se
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,plot_confusion_matrix
warnings.filterwarnings('ignore')
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest,f_regression,f_classif
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsClassifier
from spotify_api import get_urls
import requests
import spotipy
import json
import os
from weekly import *
# model=pickle.loads(open('content.pkl','rb'))
data = pd.read_csv('C:/Users/DELL/Downloads/genres_v2.csv')
    # print(data)
feat=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','song_name','id','genre']
tempo=data[feat]
tempo.dropna(axis=0,inplace=True)
tempo.reset_index(drop=True, inplace=True)
    # print(tempo)
    # input=str(sys.argv[1])
    # print(input[3])
    # Selected Columns
features=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence']
target='id'
    # X & Y
X=tempo[features]
Y=tempo[target]
def EncodeY(Y):
    actual_target=np.sort(pd.unique(Y), axis=-1, kind='mergesort')
    Y=LabelEncoder().fit_transform(Y)
    encoded_target=[xi for xi in range(len(actual_target))]
    return Y
temp=EncodeY(tempo['genre'])
    #temp
X.insert(10,"genre_en",temp)
X=X.values
X_train=X[:19519,:]
X_test=X[19519:,:]
Y_train=Y[:19519]
Y_test=Y[19519:]
def distance(x,x1):
    dis=np.sqrt(sum((x-x1)**2))
    return dis
class KNeighborsClassifier():
    def __init__(self, k=10, dist=distance):
        self.k = k
        self.dist = dist
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
    def recommend(self, querypoint):
        store=[]
        size=self.X_train.shape[0]
        for i in range(size):
            d=self.dist(querypoint,self.X_train[i])
            store.append((d,self.Y_train[i]))
        store=sorted(store)
        store=store[:self.k]
         # store=np.array(store)
        return store
def get_values(input):
    ind=tempo[tempo['song_name']==input].index
    ind=ind[0]
    return X[ind]
model=KNeighborsClassifier()

try:
    AUTH_URL = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': "aba68a7c20a14bd89fea91da58bde342",
        'client_secret': "587a8071c09e446e9d857154ef83c95c",
    })

    auth_response_data = auth_response.json()
except Exception as e:
    print("error in auth")
    print(e)

# save the access token

try:
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }


    BASE_URL = 'https://api.spotify.com/v1/'
except Exception as e:
    print("error getting access token")
    print(e)


app=Flask(__name__)

@app.route('/')
def man():
    return render_template('discover_weekly.html')
    
@app.route('/recommend',methods=['GET','POST'])
def recommend():
    model.fit(X_train,Y_train)
    input=str(request.form["song"])
    ind=tempo[tempo['song_name']==input].index
    ind=ind[0]
    arr=model.recommend(X[ind])
    final=[]
    for i in range(10):
        link_list=get_urls(str(arr[i][1]))
        final.append(link_list)
    return render_template('result.html',data=final)

@app.route('/weekly_recom',methods=['GET','POST'])
def weekly_recom():
    my_id="b80344d063b5ccb3212f76538f3d9e43d87dca9e"
    madeforu=weekly_rec(my_id)
    final=[]
    for i in range(20):
        link_list=get_urls(str(madeforu[i]))
        final.append(link_list)
    return render_template('discover_weekly.html',data=final)

if __name__=="__main__":
    app.run(debug=True)