# CST 205 Design Doc

# Topics to be used from class:

- PysideQT, image scaling/sizing, Data Visualization, API calling, web scraping  
- Class References \- Hw3, Lab18

# Project:

1. **Web scraping data collection/sorting:**  
1. \#1 Live news dashboard \-\> scrape news sites and display color-coded info/analysis  
2. \#2 Live sports dashboard \-\> scrape sports sites and display different info/analysis  
3. Pokemon dashboard \-\> scrape websites to display Pokémon card prices, and if we can access it, add the ability to view a price graph based on recent price changes.  
4. TCG dashboard \-\> scrape websites to view recent prices/data related to multiple trading card games. Could do this instead of the Pokémon idea above, since this would cover that.

**What are we going to build?**

| What is the mission of your product? What is the purpose of your product?  What is the need? What is your solution? | The mission of this product is to create a centralized dashboard to view live data for multiple interests through web scraping. |
| :---- | :---- |
| Who is your target audience? Who will your users be? How will your product serve these people? | People who want to be kept updated on specific topics in a short time(news, sports, collectibles, etc.). |
| What are the design features? What kind of features will this product have to meet the needs of the audience? | The product aims to be simplistic and user-friendly with the ability to view and sort live data based on any provided criteria from websites/api’s that relate to each specific interest. |
| What is the user onboarding flow?  What will the users see when they open your application? What are the steps that users will go through to use your product?   | When the user opens  This product will contain a home page with buttons for each of the different topics that have live data. The buttons will/could be Live News, Live Sports, Collectible Prices, etc.Each of these buttons will lead to a page in the app that displays the most recent data from the specified area of interest. If possible, we will add the ability to sort the data (dependent on websites/api’s). |

**Additional questions**

# 1\. Which Python libraries do you plan to use?

- Pysideqt, requests, urllib, beautifulsoup, lxml

# 2\. APIs and How You’ll Use Them: If you plan to use any APIs (like Spotify, etc.), list them here and describe how you’ll use them.

- We have no plans to use an API to start with, but that may change as the project progresses depending on how things go

# 3\. How will you break down the work? Who will work on what?

- We will break down the work with individual tasks. We will have a to-do list, and each member will assign themselves a task for the week. 	

4\. What are the milestones for the project? 

1. Display/Buttons for Home Page  
2. Web scrap from Live News outlets / Display wanted data  
3. Web scrap from Sports News outlets / Display wanted data  
4. Web scrap from Other sources if time allows (collectibles, etc.) / Display wanted data  
5. Polish UI and web flow  
- General Tasks: UI Mockups, Designing the front end, backend setup for web scraping, setting up communication between the front-end and backend, adding extra features if there is time left, finalizing the project.

# 5\. What will the most challenging part be? What do you expect to be the hardest part, and how will you approach it?

- We expect the most challenging part of the project will be communicating everyone's roles and goals for each milestone. We will use resources like trello to keep everyone on the same page for tasks that need to be done for the week.