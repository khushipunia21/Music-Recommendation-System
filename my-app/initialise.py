from flask import Flask,render_template, request
import pickle
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,plot_confusion_matrix
warnings.filterwarnings('ignore')
import requests
import spotipy
import json
import os

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