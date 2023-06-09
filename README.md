# News website crawler project
## Description

The News Website Crawler is a Python-based project that allows users to scrape and collect news articles from the website https://www.theguaridan.com. 
It is designed to streamline the process of gathering news data from the website "the guardian" for analysis, research, or any other purpose.
The crawler utilizes web scraping techniques to extract relevant information such as article titles, authors, publication dates, content, and URLs the news website. It navigates through the website's pages, follows links, and retrieves the desired data, all while adhering to the website's terms of service and respecting ethical considerations.

## Installation

Prerequisites
- Docker Desktop
- Docker account


## Project structure

The python project is constructed like the following:
News website crawler
- **Crawler:** crawls the website and stores data to MongoDB
  - web_crawler.py
  - loadDataMongodb.py
  - run.py
 
- **Flask_API:** creates an API to get all articles or get an article by url from MongoDB
  - flask_app.py
  - api_functions.py
  - loadDataMongodb.py
 
- **Dockerfile:** generates the first docker image "samarmami18/web-crawler"
- **DockerfileFlask:** generates the second docker image "samamrmami18/api_test"



## Execution steps

1. Install Docker Desktop 
https://docs.docker.com/desktop/install/windows-install/

2. Create an account on Docker if you don't have one already

3. I have two docker images:
 - The first dokcer image **samarmami18/web-crawler** is for an application that crawls the online news website https://www.theguardian.com/ using a crawler framework (BeautifulSoup in my case) to collect the articles (headline, description, text, ...) and stores the results in a MongoDB database.
 - The second docker image **samarmami18/api_test** is for a Flask application that exposes an API to get articles data from the MongoDB.

Pull the two docker images for my project. To do so, run these commands in you cmd terminal:

`docker pull samarmami18/web-crawler:v2`

`docker pull samarmami18/api_test:v2`

This will get you the image in your docker space.

4. You need to run the docker image to generate containers thus run the application.

- Execute the first container if you want to fill the MongoDB database with the articles of the day (This procedure could have been automated with Kubernetes for a daily execution for example)

`docker run samarmami18/web-crawler:v2`

- Execute the second container to run the API application. This will give you an endpoint : http://127.0.0.1:5000 to access data in two ways:

  - Data rendred in HTML formal : on this base url http://127.0.0.1:5000 for the sake of the test.
  - Data in json format : to get data in json format, the _api_functions.py_ script was written for you (see the section API documentation)

`docker run -p 5000:5000 samarmami18/api_test:v2`


You can see the containers name with this command:

`docker ps -a`


## API documentation
 
Welcome to the News Website API documentation. This API allows you to retrieve articles from news website www.thegardian.com. Please follow the guidelines below to access the available endpoints and parameters.
#### Base URL
The base URL for accessing the News Website API is: http://127.0.0.1:5000
This is a local url (in practice, it should be a defined endpoint)

#### 1. Get all the articles
Retrieves a list of the articles crawled in the news website.

- ***Endpoint:*** "/"

- ***HTTP Method:*** GET

- ***Example:*** get_all_articles()
-> in api_functions.py uses the base url to return all articles in json format.



#### 2. Get an article by its url
Retrieves an article crawled in the news website by its url.

- ***Endpoint:*** "/search?url={url}"

- ***HTTP Method:*** GET

- ***Parameters:*** url-> the url of the article

- ***Example:*** get_article_by_url(url) 
-> in api_functions.py, takes a url parameter and uses the endpoint above to return the article by its url in json format.



## Notes

I have created a .env file which contains the environment variables (for my case, it's the MongoDB credentials) which I use to connect to my MongoDB collection to store the data collected from the website or to collect the data stored in MongoDB with my API.

If you want to create your own docker image, you need to :
- Pull my github project
- Add a .env file to the project under the NewsWebSite to store your own MongoDB credentials in this format:

_MONGODB_USERNAME=your_username_

_MONGODB_PASSWORD=your_password_

_MONGODB_DB=your_db_

_MONGODB_COLLECTION=your_collection_


## Solution limitations

#### Development
- Implement unit testing
- Implement Logging and Monitoring
- Error Handling
- Use scheduler to trigger scraping periodically.

#### Security
- Add API Authentication
- Add API rate limiting
- Implement Access control and limit access to the database (use a private network, Firewall, security rules, access lists, …)

#### Deployment
- Scalability: adjust ressources based on rules and metrics (Auto scaling on cloud)
- Caching: Use Redis or a caching layer with the database to give most asked data in API


## Solution improvements

- Improve the above limitations : Error Handling, logging, caching, security,...
- Build full cloud architecture : low cost and fully managed
- Add more API functionalities to access articles by Headline, Author,...
- Add a semantic search layer in the API : Use NLP models to generate semantic understanding of articles and enable retrieval of most similar articles to a query.


## Solution imagined architecture 
![Solution architecture](WebCrawlerArchi.png)


