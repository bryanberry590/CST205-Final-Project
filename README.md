# CST205 Final Project: Anything Dashboard

**Date:** 4/13/26

## Links

- **Repository:** [CST205-Final-Project](https://github.com/bryanberry590/CST205-Final-Project/pulls)
- **Trello Board:** [Team 7616 Final Project Board](https://trello.com/b/m5E2HVdr/team-7616-final-project-board)

## Team Members

- Andrew Ryer
- Tyler Pruitt
- Angel Enriquez
- Jeslyn See
- Bryan Berry

## Overview

This project was developed inside virtual environments. The required packages are:

- PySide6
- Pillow
- beautifulsoup4
- requests

## Installation

Install all required packages with:

```bash
pip install PySide6 Pillow beautifulsoup4 requests
```

## Running the App

Run the `main.py` file using your system's Python command. For example, inside one of our virtual environments, the project ran with:

```bash
python main.py
```

## Future Improvements

- Refined UI design
- Updates to the TCG page
- Further optimizations to image filters for faster performance

## Personal Contributions

### Andrew Ryer
Implemented the Main Page and NASA Image of the Day Page, working on `Main_Page.py` and `Image_Day.py`. Created the UI templates using PySide6. For `Image_Day.py`, added the ability to apply grayscale, negative, and a random (RGB) filter to the image of the day using Pillow. The page web scrapes from NASA.gov.

### Tyler Pruitt
Worked on the TCG page and scraping from TCGPlayer. Since the site was dynamically loaded, initially attempted Selenium but was unable to get it working, so pivoted to the Scryfall API. The page displays a random card as a highlighted image and a list of cards from three different sets.

### Angel Enriquez
For the Live News page, scraped from NPR instead of the originally chosen BBC site. Each article's headline, summary, category, corresponding image, and URL are stored. The UI includes a search bar, order sort, category sort, and selected story view. The page captures the thirty newest articles and displays ten at a time; the others are accessible via category switching or keyword search.

### Jeslyn See
Implemented the Live Sports Dashboard, working on `sports_scrape.py` and `sports_dashboard.py`. Created the UI template and set up web scraping from ESPN for the latest articles in basketball, football, baseball, tennis, and women's basketball. Captured article titles, body text, and image URLs are imported into the sports dashboard file and displayed.

### Bryan Berry
Worked across the entire app, focusing on ensuring all pages functioned correctly and were navigable via buttons. Spent significant time debugging each page. Also contributed to the NASA Photo of the Day page by writing the web scraper code, ensuring it updates whenever NASA refreshes the photo. Stayed flexible to support any part of the project the team needed.