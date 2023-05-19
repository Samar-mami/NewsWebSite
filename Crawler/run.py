"""Running the news web crawler application"""
# import logging
# import logging.config
from web_crawler import scrap_website
from loadDataMongodb import store_data, get_credentials_from_env


#from config import username, password, database, collection


def main():
    """
        entry point to run the website crawler job.
    """
    username, password, database, collection = get_credentials_from_env()
    df = scrap_website("https://www.theguardian.com")
    store_data(df, username, password, database, collection)


if __name__ == '__main__':
    main()
