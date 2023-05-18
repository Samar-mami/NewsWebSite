"""Running the news web crawler application"""
# import logging
# import logging.config
from Crawler.web_crawler import scrap_website
from Crawler.loadDataMongodb import store_data
from Crawler.config import username, password, database, collection
from Crawler.flask_API import app


def main():
    """
        entry point to run the website crawler job.
    """
    df = scrap_website("https://www.theguardian.com")
    store_data(df, username, password, database, collection)


if __name__ == '__main__':
    main()
    app.run()