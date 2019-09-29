from flask import Flask, request
from flask import render_template

# uncomment line below once you have created the
# TopCities class inside the form.py file
#from form import TopCities

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/')
def index():
    list_of_steps = ['1. Set your location', '2. Select your category of food',
        '3. Select your restaurant', '4. Select your food', '5. Order and pay']
    return render_template('home.html', list_of_steps=list_of_steps)

@app.route('/_show_name', methods=['POST'])
def testpage():
    var1 = request.form.get('HTML_input_user')
    print(var1)
    return render_template('home.html', Get_input_city=var1)
@app.route('/login')
def login():
    form = LoginForm()
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
    app.run(debug = True)