"""Running the news web crawler application"""
# import logging
# import logging.config

from Crawler.crawler import scrap_website
from Crawler.loadDataMongodb import store_data


def main():
    """
        entry point to run the website crawler job.
    """
    df = scrap_website("https://www.theguardian.com")
    store_data(df)


if __name__ == '__main__':
    main()
