from application import app
from flask import render_template, request
from application.forms import food
from flask import flash
from flask_sqlalchemy import SQLAlchemy #from sqlalchemy library import class sqlalchemy 

@app.route('/') #create an address for the website
@app.route('/home')
def home(): #call a function home()
    return render_template('home.html') #from that function, return home.html and variables

@app.route('/register')
def register():
    form = food()
    if form.validate_on_submit():
        pass
    return render_template('register.html', form = form)

@app.route('/log_in', methods = ['GET', 'POST'])
def login():
    form = food()
    if form.validate_on_submit():
        flash('Welcome to you our app, hurry go grab your food')
    return render_template('log_in.html', form = form)

@app.route('/log_out', methods = ['GET','POST'])
def logout():
    return render_template('log_out.html')

@app.route('/location', methods = ['GET', 'POST'])
def location():
    username = request.form.get('username')
    return render_template('location.html', username=username)

@app.route('/restaurants', methods = ['GET', 'POST'])
def restaurants():
    campus_food = ['• Panda Express', '• Subway', '• Jamba Juice', "• Steak n' Shake", '• Taco Bell', '• Build Pizza', '• Japanese Fusion', '• Paseo Fresh', '• Starbucks']
    viet = ['• VietNoms', '• Banh Mi Oven', "• Lee's Sandwiches", '• Pho Passion']
    chinese = ['• Panda Express', '• China Chen']
    mex = ['• Taco Bell', '• La Vics', '• Iguanas', '• Chipotle']
    fastfood = ['• Taco Bell', '• Jack in the Box', '• McDonalds', '• Chipotle']
    quick = ['• Gongcha', '• Breaktime', '• Village Market', '• 7Eleven']
    return render_template('restaurants.html', campus_food=campus_food, viet=viet, chinese=chinese, mex=mex, fastfood=fastfood, quick=quick)

@app.route('/select_order', methods = ['GET','POST'])
def select_order():
    return render_template('select_order.html')

@app.route('/feed_back', methods = ['GET','POST'] )
def feed_back():
    form = food()
    if form.validate_on_submit():
        pass
    return render_template('feed_back.html',form = form) 

@app.route('/mobile_payment', methods = ['GET','POST'])
def mobile_payment():
    return render_template('mobile_payment.html') 


@app.route('/Categories', methods = ['GET', 'POST'])
def categories():
    location = request.form.get('location')
    radius = request.form.get('radius')
    return render_template('Categories.html', location=location, radius=radius)

