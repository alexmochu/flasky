from flask import Flask, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'

if __name__ == '__main__':
    manager.run()