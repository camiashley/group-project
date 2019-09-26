from flask import flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/home')
def home():



@app.route('/login')
def login():



@app.route('/category-choices')
def choices():


@app.route('/list-of-restaurants')
def restaurants():



@app.route('/checkout')
def checkout():



if __name__ == '__main__':
    app.run();
