api_key = 'AIzaSyBJixTpGuWue17mPX1Ia_O7vUcrcvcOdMs'

# we can connect to the YOUTUBE API using this build function
from os import stat
from googleapiclient.discovery import build
import argparse     # Allows the use of positional arguments. customization of prefix chars. supports variable numbers of parameters for a single option
import unidecode    # standard for workign with wide range of characters. Each symbol has a codepoint
import pandas as pd
import csv


# Future goal, try to find a way to get this API key (just in case if it fails)
# first define the API_key

api_key = 'AIzaSyBJixTpGuWue17mPX1Ia_O7vUcrcvcOdMs'




def channel_snippet(channel_id):
    """Channel Snippet Function

    Args:
        channel_id (string): Unique channel YouTube ID

    Returns:
        dict: title of channel, description of channel, customUrl, publishedAt, Country location
    """
    snippet = yt.channels().list(part = "snippet", id = channel_id).execute()
    return snippet



def uniqueChannelId_scraper(channelName):
    """uniqueChannelId_scraper function
       If we don't have the unique channel ID for this channel use this function.
       This takes in the Channel Name ("David Dobrik") and find the channel ID.
       However, this cost quota price of 100 units!!!!
       (this should not be run everytime. Only run once on channels we never seen before.)

    Args:
        channelName (String): [Channel Name of Youtuber]

    Returns:
        string: unique ID
    """
    snippet = yt.search().list(part = "snippet", q= channelName, type = 'channel').execute()
    extractedID = snippet['items'][0]['id']['channelId']

    return extractedID


def statsGet(stats, countType):
    """getSubsCount function return subscriber count

    Args:
        stats (dict): statistics dictionary

    Returns:
        int: [Subscriber Count]
    """

    
        
    count = stats['items'][0]['statistics'][countType]
    print(f"{countType}: {count}")


    return count



if __name__ == "__main__":
    import sys
    api_key = 'AIzaSyBJixTpGuWue17mPX1Ia_O7vUcrcvcOdMs'

    # Connect YouTube Data V3 API 
    try:
        yt = build('youtube', 'v3', developerKey = api_key)
        print("Connected to YouTube API Successfully")

    except:
        print("YouTube API BUILD has failed. Check API_KEY")
    
    channel_unique_id = ["UCAaZm4GcWqDg8358LIx3kmw"]    #this is the world of boxing
    channel_name = "David Dobrik"   #if channel unique id is unknown




    ### Initializing all the values we will pull out
    titles = []
    like_count = []
    dislike_count = []
    views = []
    urlList = []
    comment_count = []
    videoIds = []
    publishedDate = []
    video_description = []



    # call channel_snippet function
    # channelSnippet = channel_snippet(channel_id= channel_unique_id[0])
    # scraped_channelID = channelSnippet['items'][0]['snippet']['channelId']

    # if we don't have the unique Channel ID of the target
    # uniqueChannelId_scraper(channel_name)

    # statistics pull from the corresponding Unique Channel ID
    stats = yt.channels().list(part='statistics', id=channel_unique_id[0]).execute()
    
    total_subscriberCount = statsGet(stats, countType= "subscriberCount")
    total_viewCount = statsGet(stats, countType="viewCount")
    total_videoCount = statsGet(stats, countType= "videoCount")
  
    #we need the channel video playlist id to get all the videos
    #### Content details ID of the channel ####
    contentDetails = yt.channels().list(part= "contentDetails", id= channel_unique_id[0]).execute()
    videoPlaylistID = contentDetails['items'][0]['contentDetails']['relatedPlaylists']['uploads']


    # Now to extract all the video data#########
    videoList = []
    nextToken = None    # this will allow us to gather more than the limit of 50 searches
    
   
    while True:
        result = yt.playlistItems().list(playlistId= videoPlaylistID, maxResults= 50,
                                     part= 'snippet', pageToken= nextToken).execute()
        videoList += result['items']
        nextToken = result.get('nextPageToken')
        if nextToken is None:
            break
    
    print(f"Total number of videos uploaded: {len(videoList)}")

    # get the list of video ID
    videoIdList = list(map(lambda k:k['snippet']['resourceId']['videoId'], videoList))

    print(f"Check the numbers:\n {len(videoList)} == {len(videoIdList)}")

    info_video = []
    for i in range(0, len(videoIdList), 40):
        tmp = (yt).videos().list(id= ','.join(videoIdList[i:i+40]), part= 'statistics').execute()
        info_video += tmp['items']
    print("check1")
    for count in range(0, len(videoList)):

        titles.append((videoList[i])['snippet']['title'])
        publishedDate.append((videoList[i])['snippet']['publishedAt'])
        video_description.append((videoList[i])['snippet']['description'])
        videoIds.append(videoList[i]['snippet']['resourceId']['videoId'])

        like_count.append(int((info_video[i])['statistics']['likeCount']))
        dislike_count.append(int((info_video[i])['statistics']['dislikeCount']))
        views.append(int((info_video[i])['statistics']['viewCount']))
        comment_count.append(int((info_video[i])['statistics']['commentCount']))
        count += 1

    print("check2")
    print(len(titles))
    print(len(like_count))
    print(len(dislike_count))
    print(len(views))
    
    print(len(comment_count))
    print(len(videoIds))
    print(len(publishedDate))
    print(len(video_description))
    data = {'title':titles, 'videoIDs':videoIds, 'video_description': video_description, 'publishedDate':publishedDate, 'likes':like_count, 'dislikes':dislike_count,'views':views, 'comment': comment_count}
    df = pd.DataFrame(data)
    
    df.to_csv('WorldOfBoxing_Data.csv', index=False)

    data = pd.read_csv('WorldOfBoxing_data.csv')
    data.head()
    data.describe()












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
