api_key = 'AIzaSyBJixTpGuWue17mPX1Ia_O7vUcrcvcOdMs'

# we can connect to the YOUTUBE API using this build function
from googleapiclient.discovery import build
import argparse     # Allows the use of positional arguments. customization of prefix chars. supports variable numbers of parameters for a single option
import unidecode    # standard for workign with wide range of characters. Each symbol has a codepoint
import pandas as pd




# Initiate variables
titles = []
PublishTime=[]
videoID = []
channelTitle = []
video_description = []
view_counts = []
like_counts = []
dislike_counts = []
commentcounts = []
favoriteCounts = []
URLs=[]
Audience_Response = []


# Unique id of the world of boxing!
uni_id = "UCAaZm4GcWqDg8358LIx3kmw"
#developer key, we input our api_key
youtube = build('youtube', 'v3', developerKey=api_key)


# Search method: snippet of the Channel description GIVEN the CHANNEL ID
snippets = youtube.search().list(part = "snippet", channelId=uni_id, type="channel").execute()
print(snippets)










# nextPage_token = None
# res = youtube.playlistItems().list(playlistId = uni_id, maxResults = 50, part = 'snippet', pageToken=nextPage_token).execute()

# while 1:
#     res = youtube.playlistItems().list(playlistId = uni_id, maxResults = 50, part = 'snippet', pageToken=nextPage_token).execute()

#     abc += res['items']
#     nextPage_token = res.get('nextPageToken')

#     if nextPage_token is None:
#         break

# print(abc)


# request = youtube.channels().list(
#     part = 'statistics',
#     id = 'UCAaZm4GcWqDg8358LIx3kmw'
# )

# response = request.execute()

# print(response)

# print("Enter id: ")
# x = str(input())
