# Group 1
[![Build Status](https://travis-ci.com/camiashley/group-project.svg?branch=master)](https://travis-ci.com/camiashley/group-project)

# How to run LocalFoodie App
Run the app by downloading the entire branch.
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

2. Logout 

3. Register

4. Location

5. Categories

6. Restaurant Recommendation

7. Feedback

8. Mobile Payment / Review Order

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

