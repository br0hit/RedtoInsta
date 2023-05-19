from instabot import Bot
import os
import shutil


def clean_up():
    dir = "config"
    remove_me = "test2.jpg"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it because in 2021 it makes problems with new uploads
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("test2.jpg")
        os.rename(remove_me, src)


def upload_post():
    bot = Bot()

    bot.login(username="brohit_reddy", password="Harshu@0103")
    bot.upload_photo("test2.jpg", caption="Bot testing")


if __name__ == '__main__':
    clean_up()
    upload_post()