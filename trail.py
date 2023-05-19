import praw
import requests
import os

# Replace client_id, client_secret and folder_path with your own values
client_id = 'Kq7VHz9Af77lJbc-EiPPIg'
client_secret = 'X6mgb9Y78eX8nEvtCc4K5Tamb1-BOw'

# Use the Reddit API to authenticate the client and obtain an access token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
headers = {'User-Agent': 'my_app/1.0'}
data = {'grant_type': 'client_credentials'}
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
access_token = response.json()['access_token']

# Use the access token to authenticate the client
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='my_app/1.0', access_token=access_token)


print(reddit.user.me())