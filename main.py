import modules.functions as modules
import modules.instagrapi_modules as im
import instaloader
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging

username = ""
password = ""

url = 'https://www.instagram.com/p/CON8CN6F-Me/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=='
url2 = "https://www.instagram.com/reel/C0mrDJvPD_m/?igsh=dmxtN3R5cXhvMnRu"

cl = im.login_user(username, password)
path = im.download_instagram_video(url, cl)