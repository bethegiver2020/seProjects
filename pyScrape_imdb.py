from bs4 import BeautifulSoup
import re
from mechanize import Browser

movie = str(input('Movie Name: '))
movie_search = '+'.join(movie.split())

base_url = 'http://www.imdb.com/find?q='
url = base_url+movie_search+'&s=all'

br = Browser()
#br.set_proxies({'http':'http://username:password@proxy:port',
#                    'https':'https://username:password@proxy:port'})
    
                     
br.open(url)
link = br.find_link(url_regex = re.compile(r'/title/tt.*'))
#print(link)
res = br.follow_link(link)
#print(res)
soup = BeautifulSoup(res.read())
des = soup.find('meta',{'name':'description'})['content']
print(des)
