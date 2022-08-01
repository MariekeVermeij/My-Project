from flask import Flask
import datetime

# Create a Flask app inside `app`
app = Flask(__name__)
hour = datetime.datetime.now().hour
# Assign a function to be called when the path `/` is requested
@app.route('/')
def index(hour):
        return "Good Night"


@app.route('/cow')
def cow():
    return 'Help a Cow to find a friend'

@app.route('/fly')
def fly():
    return 'Whooooo ooooo ... HOW?! - a flying Cow!!'


