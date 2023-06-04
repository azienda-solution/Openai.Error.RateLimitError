
import os
import os.path
import linecache
import re
import time
from ast import literal_eval
import openai
from openai.error import RateLimitError



import codecs
sys.setrecursionlimit(10000) 

def Imagecreate():
    openai.api_key = api_key# Remplacez par votre clé API OpenAI
    response = openai.Image.create(prompt="un elephant qui saute", n=1, size="1024x1024")

    image_url = response["data"][0]["url"]
input(image_url)
