from googleapiclient.discovery import build
import pandas as pd
youTubeApiKey="AIzaSyCSmIV7_6zRHsQO5i5tur57BEMjFp5PWSE"
youtube=build('youtube','v3',developerKey=youTubeApiKey)
snippets = youtube.search().list(part="snippet", type="channel", q="nptelhrd").execute()

channelId=snippets['items'][0]['snippet']['channelId']

stats=youtube.channels().list(part="statistics",id=channelId).execute()

content=youtube.channels().list(id=channelId,part='contentDetails').execute()

UploadId=content['items'][0]['contentDetails']['relatedPlaylists']['uploads']

status = youtube.channels().list(id = channelId, part = 'status').execute()

channelSections = youtube.channelSections().list(channelId = channelId, part = 'snippet').execute()

allVideos = []

nextPage_token = None

res = youtube.playlistItems().list(playlistId = UploadId,maxResults = 50,part = 'snippet',pageToken = nextPage_token).execute()

while 1:
  res = youtube.playlistItems().list(playlistId = UploadId,maxResults = 50,part = 'snippet',pageToken = nextPage_token).execute()

  allVideos += res['items']
  #print(len(allVideos))
  nextPage_token = res.get('nextPageToken')
  if len(allVideos)>1000:
      break
  if nextPage_token is  None:
    break
  

video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], allVideos))

print(len(allVideos))
stats = []
for i in range(0, len(video_ids), 40):
  res = (youtube).videos().list(id=','.join(video_ids[i:i+40]),part='statistics').execute()
  stats += res['items']



title=[ ]
liked=[ ]
disliked=[ ]
views=[ ]
url=[ ]
comment=[ ]
videoid = []
publishedDate = []
video_description = []


for i in range(0,1000):
  print(i)
  i += 1
  if 'likeCount' in (stats[i])['statistics'] and 'dislikeCount' in (stats[i])['statistics'] and 'commentCount' in (stats[i])['statistics'] :
    title.append((allVideos[i])['snippet']['title'])
    publishedDate.append((allVideos[i])['snippet']['publishedAt'])
    video_description.append((allVideos[i])['snippet']['description'])
    liked.append(int((stats[i])['statistics']['likeCount']))
    disliked.append(int((stats[i])['statistics']['dislikeCount']))
    views.append(int((stats[i])['statistics']['viewCount']))
    comment.append(int((stats[i])['statistics']['commentCount']))
    videoid.append(allVideos[i]['snippet']['resourceId']['videoId'])

  

data={'title':title,'videoIDS':videoid,'video_description':video_description,'publishedDate':publishedDate,'likes':liked,'dislikes':disliked,'views':views,'comment':comment}
df=pd.DataFrame(data)
df.to_csv('ExtractedData.csv',index = False)

df['title'].iloc[0]