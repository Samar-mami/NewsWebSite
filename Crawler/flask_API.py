


"""# Create an API"""

app = Flask(__name__)
collection = connect_mongo_db_collection('samarmami18','fjkTmLTPUsiQyTnL','Data_engineering_test','WebSiteNews')
run_with_ngrok(app)
#Home page
# @app.route('/')
# def home_page():
#     print('Welcome to my news website crawler,  to view the articles please add articles in the bar')
# Get all articles
@app.route('/', methods=['GET'])
def get_all_articles():
    articles = list(collection.find({}, {'_id': 0}))
    return render_template('Template_html.html', articles=articles)
# Get an article by its URL
@app.route('/<url>', methods=['GET'])
def get_article_by_url(url):
    article = collection.find_one({'Article_url': url}, {'_id': 0})
    if article:
      #return render_template('Template_html.html', article = article)
      return article
      #return article
    return jsonify({'message': 'Article not found :('})

if __name__ == '__main__':
  app.run()

