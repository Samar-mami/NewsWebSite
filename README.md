# NewsWebSite
# News website crawler project
Description
The News Website Crawler is a Python-based project that allows users to scrape and collect news articles from v the website www.thegaridan.com. 
It is designed to streamline the process of gathering news data from multiple sources for analysis, research, or any other purpose.
The crawler utilizes web scraping techniques to extract relevant information such as article titles, authors, publication dates, content, and URLs the news website. It navigates through the website's pages, follows links, and retrieves the desired data, all while adhering to the website's terms of service and respecting ethical considerations.

Installation
Prerequisites

Steps
1. Install Docker Desktop 
https://docs.docker.com/desktop/install/windows-install/

2. Create an account on Docker if you don't have one already

3. Pull the two docker images for my project "samarmami18/web-crawler" and "samarmami18/api_test".
To do so, run this command in you cmd terminal:
`docker pull samarmami18/web-crawler`
docker pull samarmami18/api_test
This will generate a container for each image.
You can see the container name with this command:
docker ps -a

4. Once succeeded, you should now run the container for each docker image executing these commands:
docker run 
