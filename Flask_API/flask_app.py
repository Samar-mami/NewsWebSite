"""# Create an API"""
from flask import Flask, render_template, jsonify, request
from Crawler.config import username, password, database, collection
from Crawler.loadDataMongodb import connect_mongo_db_collection

app = Flask(__name__)
collection = connect_mongo_db_collection(username, password, database, collection)


@app.route('/', methods=['GET'])
def api_get_all_articles():
    articles = list(collection.find({}, {'_id': 0}))
    return render_template('Template_html.html', articles=articles)
    # return articles


# Get an article by its URL
@app.route('/search', methods=['GET'])
def api_search_articles():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400

    articles = collection.find({'Article_url': {'$regex': url, '$options': 'i'}})
    results = [article for article in articles]
    return render_template('Template_html.html', articles=results)