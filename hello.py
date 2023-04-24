from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_for_url():
    print(url_for('hello'))
    print(url_for('user_page', name='besthope'))
    print(url_for('test_for_url'))
    print(url_for('test_for_url', num = 2))
    return 'Test Page'