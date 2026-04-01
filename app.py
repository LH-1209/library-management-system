from flask import Flask, render_template
from extensions import db
from api.books import book_api
from api.authors import author_api
from api.publishers import publishers_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(book_api, url_prefix='/books')
app.register_blueprint(author_api, url_prefix='/authors')
app.register_blueprint(publishers_api, url_prefix='/publishers')

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/ui')
def ui():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)