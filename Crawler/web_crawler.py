# -*- coding: utf-8 -*-
"""NewsWebsiteCrawl.ipynb
##Web Scraping with Python
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime


###################################################################################################
# Get the author of the article : this function takes the URL of the article and returns its author
# It uses BeautifulSoup to search for the key word 'author'
def get_author_article(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    author_tag = soup.find('a', {'data-link-name': 'auto tag link', 'rel': 'author'})
    if author_tag:
        author_name = author_tag.get_text()
        author = author_name
    else:
        author = ''
    return author


###################################################################################################
# Get the text of the article : this function takes the URL of the article and returns its text
# It uses BeautifulSoup to search for the key word 'p' -> paragraph
def get_article_text(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    text = [p.get_text(strip=True) for p in soup.find_all('p')]
    text = ' '.join(text)
    return text


###################################################################################################
# Create a function to get the publication date of the article: this function takes the URL of the article and
# returns its publication date
def get_date_article(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    date_string_test = soup.find('span', class_="dcr-u0h1qy")
    if date_string_test:
        date_string = date_string_test.get_text(strip=True)
        date_string = date_string[:-4]
        date_format = "%a %d %b %Y %H.%M"
        # if ('\xa0' in date_string):
        #  date_string = date_string.replace('\xa0', ' ')
        datetime_object = datetime.strptime(date_string, date_format)
        return datetime_object
    else:
        return datetime(9999, 9, 9, 9, 9)


###################################################################################################
# Create a dataset from scraping a news website : it takes the website url, scrap it with beautifulsoup and returnes
# the article details : headline, text, description, kicker,...
def scrap_website(url):
    response = requests.get(url)
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    # Create an empty list for each element
    headlines = []
    article_urls = []
    descriptions = []
    kickers = []
    authors = []
    publication_dates = []
    article_texts = []
    # Find all article elements
    print('Finding all the articles in the news website the gardian ...')
    articles = soup.find_all('div', class_='fc-item__container')
    # Iterate over the articles and extract desired information
    for article in articles:
        # Extract the article title
        headline_elem = article.find('a', class_='u-faux-block-link__overlay')
        headline = headline_elem.get_text(strip=True) if headline_elem else ""
        headlines.append(headline)
        # Extract the article link
        article_url = article.find('a', class_='u-faux-block-link__overlay')['href']
        article_urls.append(article_url)
        # Extract the article description
        description_elem = article.find('div', class_='fc-item__standfirst')
        description = description_elem.get_text(strip=True) if description_elem else ""
        descriptions.append(description)
        # Extract the article kicker
        kicker_elem = article.find('div', class_='fc-item__kicker')
        kicker = kicker_elem.get_text(strip=True) if kicker_elem else ""
        kickers.append(kicker)
        # Get authors
        author = get_author_article(article_url)
        authors.append(author)
        # Get publication date
        publication_date = get_date_article(article_url)
        publication_dates.append(publication_date)
        # Get article texts
        article_text = get_article_text(article_url)
        article_texts.append(article_text)
    # Create a dataframe from the extracted information
    print('Extracting headlines...')
    print('Extracting urls...')
    print('Extracting the article descriptions...')
    print('Extracting the article kickers...')
    print('Extracting the article authors...')
    print('Extracting the article publication dates...')
    print('Extracting the article texts...')
    df = pd.DataFrame({
        'Headline': headlines,
        'Article_url': article_urls,
        'Description': descriptions,
        'Kicker': kickers,
        'Author': authors,
        'Publication_date': publication_dates,
        'Article_text': article_texts
    })
    # return the final dataframe
    return df
