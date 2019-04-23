# Web Scrapping using Python.


# import libraries
import urllib.request as url
from bs4 import BeautifulSoup

# specify the url
# ICC Chamipons Trophy 2017 India Vs South Africa Match From Cricbuzz.com 
quote_page = 'http://www.cricbuzz.com/live-cricket-scores/16710/ind-vs-rsa-11th-match-group-b-icc-champions-trophy-2017'

# query the website and return the html to the variable ‘page’
page = url.urlopen(quote_page)


# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# get the Mini Score
status_box = soup.find('div', attrs={'class': 'cb-min-bat-rw'}).find('span', attrs={'class': 'cb-font-20'})

status = status_box.text.strip() # strip() is used to remove starting and trailing
print(status)

# get the Current Run Rate
crr_box = soup.find('div', attrs={'class': 'cb-min-bat-rw'}).find('span', attrs={'class': 'cb-font-12'})
crr = crr_box.text.strip()
print (crr)
