"""# Create an API"""
from flask import Flask, render_template, jsonify, request
from loadDataMongodb import connect_mongo_db_collection
from loadDataMongodb import get_credentials_from_env

app = Flask(__name__)
print("Welcome to my Flask API app :) !\n")
# Get the MongoDB credentials to connect to the MongoDB database
username, password, database, collection = get_credentials_from_env()
# Get the MongoDB collection
collection = connect_mongo_db_collection(username, password, database, collection)


#########################################################################################
# First method : get all articles from the MongoDB database
# I am using an HTML template for the output for the sake of this test
# The template format is in the directory "templates"
@app.route('/', methods=['GET'])
def api_get_all_articles():
    articles = list(collection.find({}, {'_id': 0}))
    return render_template('Template_html.html', articles=articles)
    # return articles


#########################################################################################
# Second method : get an article by its URL
# I am using a HTML template for the output for the sake of this test
# The template format is in the directory "templates"
@app.route('/search', methods=['GET'])
def api_search_articles():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400

    articles = collection.find({'Article_url': {'$regex': url, '$options': 'i'}})
    results = [article for article in articles]
    return render_template('Template_html.html', articles=results)
