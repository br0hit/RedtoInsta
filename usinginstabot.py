from instabot import Bot
from decouple import config
import os 
import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])


insta = Bot()

insta.login(username = 'brohit_reddy',  password = 'Harshu@0103')
# insta.upload_photo(photo = "test2.jpg",caption= "botworking")

file = "funny/images/23546_Gifted.jpg"
insta.upload_photo(file, caption="bitch bot working")
