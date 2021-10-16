import requests
import bs4
from datetime import datetime

curr_date = str(datetime.now()).split()[0]

#The release date is a parameter in the HTTP request with the following format:
#release_date=from_date,till_date
#Commas are required to separate multiple value for a single parameter
#Since I want movies of all time, from_date is left blank, till_date is put as current date
URL="http://www.imdb.com/search/title?release_date=," + curr_date

r = requests.get(URL)
  
soup = bs4.BeautifulSoup(r.content, 'html5lib')
  
table = soup.find_all('div', attrs = {'class' : 'lister-item-content'})
for i, content in enumerate(table):

     movie_name = content.h3.a.text
     rating = content.find('span', attrs = {'class' : {'rating-rating'}}).span.text
     
     actors = content.find('p', attrs = {'class' : ''})
     actors = [name.text for name in actors.find_all('a')]
     
     print("{}. {} ({}) - Ft. ".format(i+1, movie_name, rating), end='')
     print(*actors, sep=', ')
