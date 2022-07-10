# import flask dependency

from flask import Flask

# create New FLask App Instance
# an 'instance' is a general term in programming to refer to a singular version of something.
# we will create a new flask instance called app

app = Flask(__name__)

# the (__name__) variable denotes the name of the current function. This can be used to determine if our code is being
# run from the command loine or if it has been imported into another piece of code.
# variables with underscores before and after them are called magic methods in Python.

# create a flask route

@app.route('/')

# the forward slash denotes that we want to put our data at the root of our routes.
# the forward slash is commonly known as the highest level of hiercarchy in any computer system

# create a function called hello_world()

@app.route('/')
def hello_world():
    return 'Hello world'