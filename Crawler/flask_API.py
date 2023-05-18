"""# Create an API"""
from flask import Flask, render_template, jsonify
from Crawler.config import username, password, database, collection
from Crawler.loadDataMongodb import connect_mongo_db_collection

app = Flask(__name__)
collection = connect_mongo_db_collection(username, password, database, collection)


@app.route('/', methods=['GET'])
def get_all_articles():
    articles = list(collection.find({}, {'_id': 0}))
    return render_template('Template_html.html', articles=articles)
    # return articles


# Get an article by its URL
@app.route('/<url>', methods=['GET'])
def get_article_by_url(url):
    article = collection.find_one({'Article_url': url}, {'_id': 0})
    if article:
        return render_template('Template_html.html', article=article)
        # return article
    return jsonify({'message': 'Article not found :('})
