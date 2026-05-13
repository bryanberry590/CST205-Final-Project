# CST205-Final-Project
# ANYTHING DASHBOARD
# 4/13/26

REPO LINK: https://github.com/bryanberry590/CST205-Final-Project/pulls
TRELLO LINK: https://trello.com/b/m5E2HVdr/team-7616-final-project-board

CREATED BY:
    Andrew Ryer
    Tyler Pruitt 
    Angel Enriquez
    Jeslyn See
    Bryan Berry


We developed this project inside of our virtual environments. The packages that this project uses are:
PySide6
Pillow
beautifulsoup4
requests

These packages can be installed with the following command:
pip install PySide6 Pillow beautifulsoup4 requests

To run the app, you just need to run the main.py file with whatever python command your computer uses. For example, inside one of our virtual environments, the project ran with the command 'python main.py'.

Future changes could be UI design, updating the TCG page, and further optimizations to the image filters to run quicker.

Personal Contributions:

    Andrew Ryer - I worked on the implementation of the Main Page and NASA Image of the Day Page. worked on the files Main_Page.py and Image_Day.py. I created the UI template for these pages (Using Pyside6). Also, for Image_Day.py I added the ability to apply gray scale, negative, and a random (RGB) filter to the image of the day (using pillow). Image_Day.py web scrapes from NASA.gov. 

    Tyler Pruitt - I worked on the tcg page and scraping from tcgplayer, since it was dynamically loaded I tried using selenium. Unfortunately, I was unable to get selenium to work, so I pivoted to using the scryfall api. I have it take a random card as a highlighted image, and a list of cards from 3 different sets to display.

    Angel Enriquez - For the Live News page, I scraped from NPR rather than my originally picked website, BBC. I was able to get it working properly after switching sites. I scraped each individual article and stored the headline, summary, category, corresponding image, and article URL. For the UI I had a search bar, order sort, category sort, and selected story. The page captures the thirty newest articles and displays ten of them at a time, you can see the other ones by switching to other categories and searching for the specific headlines or any keywords.

    Jeslyn See - I worked on the implementation of the Live Sports Dashboard. I worked on the files sports_scrape.py and sports_dashboard.py. I created the UI template for it, then set up the web scraping by scraping the ESPN website for the latest article on these categories: basketball, football, baseball, tennis, and women's basketball. After I captured the information from ESPN, I imported the article title, body text, and image URL in the sports dashboard file. I displayed all the captured information there.

    Bryan Berry - I worked all over the app. The main focus was ensuring that all pages functioned correctly and could be clicked to with the use of buttons. I also spent a lot of time on each page ensuring they were bug free. I also assisted with the Nasa photo of the day page by writing the web scraper code for that. I ensured that it worked properly and updated whenever Nasa updates the photo of the day. I also stayed open to contributing to any part of the project that my team needed me on.
