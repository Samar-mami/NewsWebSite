"""# Create an API"""
from bs4 import BeautifulSoup
import requests


######################################################################
# These are API functions to help you work with my Flask app
# This function takes a HTML format and convert my HTML template to a json format
# It takes the API response and returns a json format of it
def convert_html_json(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table body
    table_body = soup.find('tbody')

    # Extract the rows from the table body
    rows = table_body.find_all('tr')

    # Initialize a list to store the extracted data
    data = []

    # Iterate over each row and extract the fields
    for row in rows:
        columns = row.find_all('td')
        headline = columns[0].text.strip()
        description = columns[1].text.strip()
        author = columns[2].text.strip()
        article_text = columns[3].text.strip()
        kicker = columns[4].text.strip()
        publication_date = columns[5].text.strip()
        article_url = columns[6].find('a')['href']

        # Create a dictionary for the extracted fields
        article_data = {
            'headline': headline,
            'description': description,
            'author': author,
            'article_text': article_text,
            'kicker': kicker,
            'publication_date': publication_date,
            'article_url': article_url
        }

        # Add the dictionary to the data list
        data.append(article_data)
    return data


##################################################################################
# This functions returns all the articles collected by the API in a json format
def get_all_articles():
    url = 'http://127.0.0.1:5000'  # Update with your API endpoint
    response = requests.get(url)
    if response.status_code == 200:
        data = convert_html_json(response)
        return data
    else:
        print('Error: Failed to retrieve data from the API')
        return None


##################################################################################
# This functions returns the article by its url collected by the API in a json format
# It takes the url as a parameter
def get_article_by_url(url):
    host = 'http://127.0.0.1:5000/search?url=' + url  # Update with your API endpoint
    response = requests.get(host)
    if response.status_code == 200:
        data = convert_html_json(response)
        return data
    else:
        print('Error: Failed to retrieve data from the API')
        return None
