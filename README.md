# Group 1
[![Build Status](https://travis-ci.com/camiashley/group-project.svg?branch=master)](https://travis-ci.com/camiashley/group-project)

# How to run LocalFoodie App
Run the app by downloading the entire branch, master1.
Using your computer's terminal, install the following files from flask:
  - pip install flask
  - pip install flask-wtf
  - pip install flask-sqlalchemy
  - pip install flask-login
  - pip install flask-migrate
  - pip install googlemaps
  - pip install prettyprint
  - pip install db
  
After these files are installed, run like so: 
 - python run.py

Given the url link of our app, open it on your browser and you will led to login page.
If you do not have an account, register an account and you will be brought to our home page after register.

# 8 Features

1. Login 

User needs to provide username and password for their account, if they already registered.
If not, there will be an error indicating they should register.

2. Logout 

User logs out back to the login page.

3. Register

User provides a username, a password, and e-mail of their account.
After registering, they are brought back to login page to login.

4. Location / Settings

User provides their location and the distance in radius of the restaurant search.
Through these, the app will provide a category selection for places near.

5. Notifications

So the restaurant can notify the user of the food being ready, this page asks the user whether or not it will notify them.

6. Categories

The page shows categories of different styles of food.
This depends on their location.

7. Restaurant Recommendation

After category selection, the user is recommended restaurants under the category they chose.

8. Feedback

The user can provide feedback for the food options provided on the app.

9. User Communication

Through feedback, users can follow one another to check out their feedback for the restaurant and the app.
They can follow each other or unfollow their feed and feedback for the app.

10. Review Order

The app will review the order back to the user before sending the order to the restaurant kitchen.

11. Thanks Page

The website will notify the user that the order has been sent to the restaurant kitchen and thank him/her for using the app.

# Test Cases
For now, test cases have the e-mail and password of a user in the database.

To run the test case, do like so: 
 - pytest -v 

If there is no such user, the test case will send error messages.
The test cases include users that exist and users that do not exist in the database.
Because we have four test cases, four messages will be sent, either with ERROR or a passing message.
If there is an error, this message will be shown: 

  test_user.py::test_new_user ERROR
  
  test_user2.py::test_new_user ERROR
  
  test_user3.py::test_new_user ERROR
  
  test_user4.py::test_new_user ERROR

