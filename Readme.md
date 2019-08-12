
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
|view neighorhoods    |request the site via link|web page with neighborhoods  |
|login and join hood  |signup & fill profileform| user profile                |
|To search businesses |neighborhood name        |businessess and details      |
|create neighborhood  |click on neighborhood    |new neighborhood             |
|create business      |click on business        |new profile                  |
|create a post        |click on post            |new post                     |
|view hood details    |click on profile picture |posts,info and businesses    |
|change neighborhood  |click channge hood in pro|new neighourhood             |


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

# requrements.txt

* config==0.4.2
* confusable-homoglyphs==3.2.0
* dj-database-url==0.5.0
* Django==1.11
* django-bootstrap3==11.1.0
* django-crispy-forms==1.7.2
* django-heroku==0.3.1
* django-registration==2.4.1
* gunicorn==19.9.0
* Pillow==6.1.0
* psycopg2==2.8.3
* python-decouple==3.1
* pytz==2019.2
* whitenoise==4.1.3

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