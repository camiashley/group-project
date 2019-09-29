from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    list_of_steps = ['1. Set your location', '2. Select your category of food',
        '3. Select your restaurant', '4. Select your food', '5. Order and pay']
    return render_template('index.html', list_of_steps=list_of_steps)
    
@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    username = request.form.get('username')
    return render_template('settings.html', username=username)

@app.route('/categories', methods = ['GET', 'POST'])
def categories():
    location = request.form.get('location')
    radius = request.form.get('radius')
    return render_template('categories.html', location=location, radius=radius)

@app.route('/restaurants', methods = ['GET', 'POST'])
def restaurants():
    campus_food = ['• Panda Express', '• Subway', '• Jamba Juice', "• Steak n' Shake", '• Taco Bell', '• Build Pizza', '• Japanese Fusion', '• Paseo Fresh', '• Starbucks']
    viet = ['• VietNoms', '• Banh Mi Oven', "• Lee's Sandwiches", '• Pho Passion']
    chinese = ['• Panda Express', '• China Chen']
    mex = ['• Taco Bell', '• La Vics', '• Iguanas', '• Chipotle']
    fastfood = ['• Taco Bell', '• Jack in the Box', '• McDonalds', '• Chipotle']
    quick = ['• Gongcha', '• Breaktime', '• Village Market', '• 7Eleven']
    return render_template('restaurants.html', campus_food=campus_food, viet=viet, chinese=chinese, mex=mex, fastfood=fastfood, quick=quick)

def selection():
    return render_template('selection.html')

def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run();
