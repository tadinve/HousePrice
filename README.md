# House Price Predictor on Heroku

Hosted on [Heroku]

This is a simple Flask app that will predict the house price using sci-kit Learn.

## Steps

### 1) Create a new virtual environment and install requirements:

  - git clone https://github.com/tadinve/HousePrice
  - virtualenv --python=python3.6 venv
  - source venv/bin/activate
  - pip install -r requirements.txt

### 2) Test the environment
  - python controller.py # it will load the model and start a web-server.
  - Visit http://127.0.0.1:5000/ with your browser and test
  -
  - Explore the "controller.py" file. Can you figure out what it does?
  - Explore the rest of the code. Can you figure out what the other files do?

### 3) Deploy to Heroku! (requires heroku install & signup)
  - heroku create
  - git add .
  - git commit -m "initial commit"
  - git push heroku master
  - #test on your local browser.
