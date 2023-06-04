
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

def rediger_article(sujet, number):
    openai.api_key = api_key# Remplacez par votre clé API OpenAI
    prompt = f"Bonjour, Peux-tu rédiger un article sur la profession {sujet} dans ce domaine.\n\n"

    while True:
        try:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=600,
                n=1,
                stop=None,
                temperature=0.7,
                top_p=0.9,
                frequency_penalty=0.2,
                presence_penalty=0.2
            )

            if 'choices' in response and len(response['choices']) > 0:
                article = response['choices'][0]['text'] 
                return article
            else:
                return None

                
        except RateLimitError as e:
            if e.status == 429:  # Erreur de taux limite (ratelimit)
                retry_after = e.retry_after
                print(f"Rate limit exceeded. Retrying in {retry_after} seconds.")
                time.sleep(retry_after)
                print("Erreur de taux limite. Attente de 1 minute...")
                append_new_line(r'ERREUR-IA.txt', str(number)+" "+str(e))
                time.sleep(60)  # Attendre 1 minutes (60 secondes)
            else:
                append_new_line(r'ERREUR-IA.txt', str(number+" UNE AUTRE ")+" "+str(e))
                raise e
 
description = rediger_article("Developper IA ", (1))
input(description)
