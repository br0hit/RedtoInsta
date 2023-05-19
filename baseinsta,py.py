
import requests

media_file = "testimg.jpg"
caption = "This is my Instagram post!"
access_token = "IGQVJVOWxFcDU1Tm9TZAEd3eGlXaWdzUEg4dmlLa3kzSFdLNlN6bWdzYXZAiemYwblZAsX0pTbEtaRHFyR2wzTG50SXJaWVhuYTllak1Ha2dBRzJwZAEZARazhZAVkpkVTJiWHNlZAFBWVVZAOek9qa3FxNlFQZAgZDZD"

url = f"https://graph.instagram.com/me/media?caption={caption}&access_token={access_token}"

files = {
    "media": open(media_file, "rb")
}

response = requests.post(url, files=files)

if response.status_code == 200:
    print("Media uploaded successfully!")
else:
    print("Failed to upload media.")