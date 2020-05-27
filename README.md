# BlogIt

Simple blogger application. Inspiration: Reddit. 

## Deployed with Heroku
https://protected-earth-03499.herokuapp.com/

## Introduction
This application is my first attempt using the Flask web framework. I made it a goal to use as many Flask modules as I could in order to learn all that Flask has to offer.

Some flask specific modules I used are as follows:
- flask_migrate: database migrations
- flask_bcrypt: password hashing
- flask_login: authorization/authentication
- flask_sqlalchemy: database ORM
- flask_wtf: form creation and validation

I also focused on implementing common Flask design patterns including an application factory, blueprints for modularity, template inheritance, message flashing, and a login decorator.

## Getting Started
  Clone the REPO:

`` git clone git@github.com:Stoovles/BlogIt.git ``

  Install requirements w/ pip:
  
`` pip install -r requirements.txt ``

  Spin up the server locally:
  
`` python run_dev.py ``

## Testing
Cursory testing with unittest. Refer to issues.

Run this in your command line:

``python -m unittest discover tests``


