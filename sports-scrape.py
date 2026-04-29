from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
example web scraping below
"""

# following steps in lecture slide
wiki_pg = 'https://www.marvel.com/characters/cyclops-scott-summers'

wiki_html = urlopen(wiki_pg)

soup = BeautifulSoup(wiki_html.read(), 'lxml')

im = soup.find('img')

print(im)

marvel_pg = 'https://www.gq.com/story/every-x-men-movie-definitively-ranked'
marvel_html = urlopen(marvel_pg)
soup1 = BeautifulSoup(marvel_html.read(), 'lxml')
scraped_para = soup1.find('p') # text we grab from webpage is already in html tags
# searched up how to turn html into text for below line -> probably need text to display using strings in GUI
text = scraped_para.get_text()
print(scraped_para)