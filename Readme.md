
## YOURHOOD

# Created bY

William Mango  12/08/19

# Description

web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts

# User Stories

These are the behaviours/features that the application implements for use by a user.

Users would like to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## BDD

|Behaviour	          |          Input	        |Output                       |
|---------------------|-------------------------|-----------------------------|
|view neighourhoods   |request the site via link|web page with neighbourhoods |
|login and join hood  |signup & fill profileform| user profile                |
|To search businesses |neighbourhood name       |usinessess and details       |
|create neighbourhood |click on neighbourhood   |new project                  |
|create business      |click on business        |new profile                  |
|create business      |click on business        |your profile/projects        |
|view hood details    |click on pprofile picture|posts,info and businesses    |
|change neighbourhood |click channge hood in pro|new neighourhood             |


## SetUp / Installation Requirements

* Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt
* bootstrap3

# Cloning

# In your terminal:

 * $ git clone https://github.com/mangowilliam/yourhood
 * $ cd yourhood

# Running the Application

# Creating the virtual environment

 * $ python3.6 -m venv --without-pip virtual
 * $ source virtual/bin/activate
 * $ curl https://bootstrap.pypa.io/get-pip.py | python

# Installing Django and other Modules

 * $ see Requirements.txt

# To run the application, in your terminal:

 * $ python3.6 manage.py runserver

# Testing the Application

* To run the tests for the class files:

  $ python3.6 manage.py test 

# Technologies Used

* Python3.6
* Django and postgresql
* crispy forms

# deployment

* install all requrements
* create the env file to hide your credentials from users by gitignoring
* add procfile and runtime.txt file
* login to heroku and create project
* deploy the local master branch
* deploy the local Database

# Support and contact details

contact williammango2015@gmail.com for any kind of support.

# Live Link

**[click here](https://github.com/mangowilliam/yourhood)**

# License

**[MIT licence](licence)**
Copyright (c) 2019 **mangowilliam**