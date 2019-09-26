from flask import flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/category-choices')
def choices():
    return render_template('choices.html')


@app.route('/list-of-restaurants')
def restaurants():
    return render_template('restaurants.html')



@app.route('/checkout')
def checkout():
    return render_template('checkout.html')



if __name__ == '__main__':
    app.run();
