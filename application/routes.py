from flask import render_template, redirect, request, url_for
from application import app, db
from application.forms import LoginForm, RegistrationForm, FeedbackForm
from flask import flash
from flask_sqlalchemy import SQLAlchemy #from sqlalchemy library import class sqlalchemy
from flask_login import current_user, login_user, logout_user, login_required
from application.models import User
from werkzeug.urls import url_parse

@app.route('/') #create an address for the website
@app.route('/home')
@login_required
def home(): #call a function home()
    return render_template('home.html', title='Home Page') #from that function, return home.html and variables

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/feed_back', methods = ['GET', 'POST'] )
def feed_back():
    form = FeedbackForm()
    return render_template('feed_back.html', form = form) 

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

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



@app.route('/mobile_payment', methods = ['GET','POST'])
def mobile_payment():
    return render_template('mobile_payment.html') 


@app.route('/Categories', methods = ['GET', 'POST'])
def categories():
    location = request.form.get('location')
    radius = request.form.get('radius')
    return render_template('Categories.html', location=location, radius=radius)

