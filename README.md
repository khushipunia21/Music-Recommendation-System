# MUSIC RECOMMENDATION SYSTEM

Music Recommendation system recommends music by learning the user's preference.Most suitable songs are sorted for the user after taking into consideration mutiple factors that affect user's choice of music.




## Table of Contents



## Motivation

The project is built during Microsoft Engage Program 2022.
With commercial music streaming service which can be accessed from mobile devices, the availability of digital music currently is abundant and sorting out all this digital music is a very time-consuming. Therefore,  a music recommender system that can search in the music libraries automatically and suggest suitable songs to users is much needed. 
An efficient music recommender system is necessary in the interest of both music service providers and customers. 


## Algorithm

Algorithm 1:

A dataset of songs with values of various features such as 'danceability', 'energy', 'key', 'loudness', 'acousticness', 'instrumentalness', 'liveness', 'valence',etc. was collected. Pre-processing of data was done and using K-Nearest Neighbors algorithm, most similar songs were collected and sorted based on their distance from the input song. Lesser the distance more is the similarity.

![App Screenshot](/screenshots/algo1.jpg)


Algorithm 2: 

It involved analysing the playlist of our user and other users playlist as well in order to find the correlation between different user's music taste. The songs are then picked from most similar users and sorted according to the frequency of play of these songs by these users.

![App Screenshot](/screenshots/algo2.jpg)


Algorithm 3:

The user is allowed to enter a song name and change the values of instrumentalness, danceability and acousticness according to his choice and new set of songs will be predicted keeping in consideration the song input and changed values of different features.

![App Screenshot](/screenshots/algo3.jpg)


## About the Project

### Salient Features

- Get a set of recommended songs similar to the input song name.
- Customize your Music playlist according to your own choice by changing the values of acousticness ,danceability of song and instrumentalness.
- Discover Weekly playlist will be updated every week by analysing the user's choice of songs and other similar users playlist.
- Get a audio preview of the song by clicking on the cover image of track.
- Pause tha audio preview with a double click on the cover image of the track.

### Built with
- Machine Learning: ![alt_text](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
- Frontend: 

## Getting Started

### Prerequisites
- Install Python 3.10.4: https://www.python.org/downloads/

- Install and update Flask using pip:

```bash
  $ pip install -U Flask
```
- Clone the repo

```bash
  $ git clone https://github.com/khushipunia21/Music-Recommendation-System

```

- Start up the server by running python ./app.py

- Visit localhost opened to ecplore the web-application

    
### Navigating through the App

Home Page

![App Screenshot](/screenshots/page1.png)

Page describing features of the App

![App Screenshot](/screenshots/page2.png)

Contact Page

![App Screenshot](/screenshots/page3.png)

Type your favourite song in the search bar and click on search, 10 recommended songs will be displayed. Change the values of the features using the slidebar and click on go to get the new recommendations.

![App Screenshot](/screenshots/page4.png)

The Cover images of the tracks of the recommended songs will be displayed

![App Screenshot](/screenshots/page5.png)

Discover Weekly Playlist Page. Click on explore to get the playlist.

![App Screenshot](/screenshots/page6.png)



## Future Scope

- Modifying recommendations by analysing the pattern of user's music choice at different times of the day.For eg: Analysing type of music listened in the day time,suring night etc.
- Recommending users with similar taste of music and allowing the poeple to conect with each other via tha app.
- Feature of explicit feedback of user could be incorporated in the app.

## Challenges Faced

- Absence of appropriate dataset for creating the hybrid model of recommendation system that can take into consideration mutiple features altogether.
- Due to memory and processing power limitations, I could only experiment with a fraction of whole available dataset. 

## Resources Used

- https://developer.spotify.com/
- https://blog.paperspace.com/deploying-deep-learning-models-flask-web-python/
