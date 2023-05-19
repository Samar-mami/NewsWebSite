"""Running the news web crawler application"""
from web_crawler import scrap_website
from loadDataMongodb import store_data, get_credentials_from_env


def main():
    """
        entry point to run the website crawler job.
    """
    print("Welcome to my crawler app :) !\n")
    # Get the MongoDB credentials to connect to the MongoDB database
    username, password, database, collection = get_credentials_from_env()
    # Get the data collected from the web scrapping
    df = scrap_website("https://www.theguardian.com")
    # Store the data collected in MongoDB collection
    store_data(df, username, password, database, collection)


if __name__ == '__main__':
    main()
