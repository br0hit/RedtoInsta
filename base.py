# import prawcore
import praw
import requests
import os

reddit = praw.Reddit(
    # username="WeedDistributor",
    # password="Harshu@0103",
    client_id='Kq7VHz9Af77lJbc-EiPPIg',
    client_secret='X6mgb9Y78eX8nEvtCc4K5Tamb1-BOw',
    user_agent='script:RedtoInsta:v1.0 (by /u/WeedDistributor)',
)

# try:
#     print(reddit.user.me())
# except praw.exceptions.APIException as e:
#     print(f"Authentication error: {e}")


# subreddit_name = 'MadeMeSmile'  # Replace with the name of the subreddit you want to fetch posts from
post_limit = 10  # Number of top posts you want to retrieve

# subreddit = reddit.subreddit(subreddit_name)
# top_posts = subreddit.top(limit=post_limit)

# for post in top_posts:
#     # Process or print the details of each post
#     print(f"Title: {post.title}")
#     print(f"URL: {post.url}")
#     print(f"Score: {post.score}")
#     print("----")
    
# List of subreddits to download from
subreddit_names = ['memes', 'funny', 'dankmemes']

# Iterate through each subreddit
for subreddit_name in subreddit_names:
  # Retrieve the last 25 videos and images from the subreddit
  subreddit = reddit.subreddit(subreddit_name)
  posts = subreddit.hot(limit=post_limit)

  # Create the folders for the subreddit if it doesn't already exist
  video_path = f'{subreddit_name}/videos/'
  post_path = f'{subreddit_name}/images/'
  if not os.path.exists(video_path): os.makedirs(video_path)
  if not os.path.exists(post_path): os.makedirs(post_path)

  # Download and save the videos and images
  for post in posts:
    url = post.url
    title = post.title
    upvotes = post.ups

    # Modify the title to make it a valid file name
    if not os.path.isabs(title):
      title = title.replace(' ', '_')
      title = title.replace('/', '_')
      title = title.replace('\\', '_')
      title = title.replace(':', '_')
      title = title.replace('*', '_')
      title = title.replace('?', '_')
      title = title.replace('"', '_')
      title = title.replace('<', '_')
      title = title.replace('>', '_')
      title = title.replace('|', '_')
      
    # Check the file extension to determine if it's an image or a video
    if url.endswith('.jpg') or url.endswith('.png'):
      response = requests.get(url)
      # Specify the path to the file in the folder
      file_path = os.path.join(post_path, f'{upvotes}_{title}.jpg')
      # Save the file to the specified path
      open(file_path, 'wb').write(response.content)

    if post.is_video:
      video_url = post.media['reddit_video']['fallback_url']
      response = requests.get(video_url)

      # Specify the path to the file in the folder
      file_path = os.path.join(video_path, f'{upvotes}_{title}.mp4')
      # Save the file to the specified path
      open(file_path, 'wb').write(response.content) 
      
      
      
      
# Now we will be uploading the posts to instagram : 

# instagram token to weeddisstributor : IGQVJVbHFlNG5GbFdEMVZA6X0pPUjRTMl84bFZANSWJXUkE5akZAiVW1OOXJxNUdoMTF6dmhwbzBYODFJUVR6V19YY2RBQ0hkRFNmQVNkLWM3UkhBaFZArdThLN0lUZAFZAFTHRRbVpmNXdmcmJzcmtSelB2dQZDZD
#                                       IGQVJVOWxFcDU1Tm9TZAEd3eGlXaWdzUEg4dmlLa3kzSFdLNlN6bWdzYXZAiemYwblZAsX0pTbEtaRHFyR2wzTG50SXJaWVhuYTllak1Ha2dBRzJwZAEZARazhZAVkpkVTJiWHNlZAFBWVVZAOek9qa3FxNlFQZAgZDZD


