from lxml import html
import requests
from bs4 import BeautifulSoup
import re
import win32api

url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'

page = requests.get(url)

soup =  BeautifulSoup(page.text, 'html.parser')
try:
        # cricket_score = soup.find_all('div',class_='HEZHfd')[:2]
        cricket_score = soup.find('div',class_='SOsZve').strings
        score = ' '.join(list(cricket_score))
        print(score)
        win32api.MessageBox(0,score, 'Cricket Score', 0x00001000) 
       # print(len(cricket_score),type(cricket_score))
except Exception as e:
        print(e)
        cricket_score = soup.find('div',class_='qCne4e').strings
        print(' '.join(list(cricket_score)))


