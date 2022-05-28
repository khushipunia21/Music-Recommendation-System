import pandas as pd
from heapq import nlargest
from spotify_api import *
my_id="b80344d063b5ccb3212f76538f3d9e43d87dca9e"

def weekly_rec(inp_id):
    df=pd.read_csv('/dataset/Book1.csv')
    #Recommending playlist for the user : 
    #Calculating playlist of user
    id=inp_id
    playlist=[]
    store={}
    for i in range(840):
        temp_id=df['user_id'][i]
        if(temp_id==id):
            playlist.append(df['song_id'][i])
        else:
            if(df['song_id'][i] in playlist):
                if(store.get(temp_id) is not None):
                    store[temp_id]=store[temp_id]+df['count'][i]
                else:
                    store[temp_id]=df['count'][i]

    #5 most similar users
    res = nlargest(5, store, key = store.get)

    #calculating counts of all songs
    recommend_count={}
    for i in range(840):
        temp_id=df['user_id'][i]
        temp_song=df['song_id'][i]
        if(temp_id==id):
            continue
        else:
            if(temp_song in playlist):
                continue
            else:
                if(recommend_count.get(temp_song) is not None):
                    recommend_count[temp_song]=recommend_count[temp_song]+df["count"][i]
                else:
                    recommend_count[temp_song]=df["count"][i]

    #sorting for best choices
    recommended=nlargest(20,recommend_count, key=recommend_count.get)
    return recommended
