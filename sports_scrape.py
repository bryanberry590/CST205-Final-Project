from bs4 import BeautifulSoup
from urllib.request import urlopen
import re # this import is for our helper method that cleans the article bodies 
"""
Scrapes ESPN for different sports news

Author: Jeslyn See
"""

# Helper method for cleaning up article bodies we are capturing above (removing unnecessary text/spaces that was attached)
def clean_article(text):
    text = text.strip()                          
    text = re.sub(r'\n+', '\n', text)            # collapses multiple newlines into one
    text = re.sub(r' +', ' ', text)              # collapses multiple spaces into one
    text = re.sub(r'\t', '', text)               # removes tab characters
    return text


# Basketball news article: capturing image url, title of article, and article bodies 
basketball_pg = 'https://www.espn.com/basketball/pba/story/_/id/48626941/jenning-leung-homecoming-spark-shines-tough-macau-black-knights-pba-debut'

basketball_html = urlopen(basketball_pg)

bball_soup = BeautifulSoup(basketball_html.read(), 'lxml')

bball_im = bball_soup.find('source')
bball_title = bball_soup.find('title')
bball_article = bball_soup.find('div', class_='article-body')

# grabbing image url, but it's within source and srcset layers
srcset = bball_im.get('srcset', '')
bball_image_url = srcset.split()[0] 

bball_text_title = bball_title.get_text()
bball_article_text = bball_article.get_text()

# testing captures with prints 
# print(bball_text_title)
# print(bball_article_text)
# print(bball_image_url)


# Football news article: capturing image url, title of article, and article bodies 
football_pg = 'https://www.espn.com/nfl/draft2026/story/_/id/48610584/2026-nfl-draft-ranking-top-100-picks-best-steals-team-fits-trades'

football_html = urlopen(football_pg)

ftball_soup = BeautifulSoup(football_html.read(), 'lxml')

ftball_im = ftball_soup.find('source')
ftball_title = ftball_soup.find('title')
ftball_article = ftball_soup.find('div', class_='article-body')

ftball_text_title = ftball_title.get_text()
ftball_article_text = ftball_article.get_text()

srcset = ftball_im.get('srcset', '')
ftball_image_url = srcset.split()[0]

# print(ftball_text_title)
# print(ftball_image_url)
# print(ftball_article_text)


# Baseball section following the same pattern as above 
baseball_pg = 'https://www.espn.com/mlb/story/_/id/48620433/mlb-2026-panic-meter-struggling-teams-red-sox-mets-phillies-astros'

baseball_html = urlopen(baseball_pg)

bsball_soup = BeautifulSoup(baseball_html.read(), 'lxml')

bsball_im = bsball_soup.find('source')
bsball_title = bsball_soup.find('title')
bsball_article = bsball_soup.find('div', class_='article-body')

# testing captures with prints 
bsball_text_title = bsball_title.get_text()
bsball_article_text = bsball_article.get_text()

srcset = bsball_im.get('srcset', '')
bsball_image_url = srcset.split()[0]

# print(bsball_text_title)
# print(bsball_image_url)
# print(bsball_article_text)


# Tennis info capture here 
tennis_pg = 'https://www.espn.com/tennis/story/_/id/48581261/alcaraz-defend-french-open-title-due-wrist-injury'

tennis_html = urlopen(tennis_pg)

tenn_soup = BeautifulSoup(tennis_html.read(), 'lxml')

tenn_im = tenn_soup.find('source')
tenn_title = tenn_soup.find('title')
tenn_article = tenn_soup.find('div', class_='article-body')

# testing captures with prints 
tenn_text_title = tenn_title.get_text()
tenn_article_text = tenn_article.get_text()

srcset = tenn_im.get('srcset', '')
tenn_image_url = srcset.split()[0]

# print(tenn_text_title)
# print(tenn_image_url)
# print(tenn_article_text)


# WNBA section 
wnba_pg = 'https://www.espn.com/wnba/story/_/id/48623464/wnba-atlanta-dream-2026-angel-reese-playoff-team-title-contender'

wnba_html = urlopen(wnba_pg)

wnba_soup = BeautifulSoup(wnba_html.read(), 'lxml')

wnba_im = wnba_soup.find('source')
wnba_title = wnba_soup.find('title')
wnba_article = wnba_soup.find('div', class_='article-body')

# testing captures with prints 
wnba_text_title = wnba_title.get_text()
wnba_article_text = wnba_article.get_text()

srcset = wnba_im.get('srcset', '')
wnba_image_url = srcset.split()[0]

# print(wnba_text_title)
# print(wnba_image_url)
# print(wnba_article_text)

# clean the capture text 
bball_article_text = clean_article(bball_article_text)
ftball_article_text = clean_article(ftball_article_text)
bsball_article_text = clean_article(bsball_article_text)
tenn_article_text = clean_article(tenn_article_text)
wnba_article_text = clean_article(wnba_article_text)

