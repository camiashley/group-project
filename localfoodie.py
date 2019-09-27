from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    list_of_steps = ['1. Set your location', '2. Select your category of food',
        '3. Select your restaurant', '4. Select your food', '5. Order and pay']
    return render_template('index.html', list_of_steps=list_of_steps)
    
def login():
    return render_template('login.html')

def categories():
    return render_template('categories.html')

def restaurants():
    return render_template('restaurants.html')

def selection():   
    return render_template('selection.html')

def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run();
