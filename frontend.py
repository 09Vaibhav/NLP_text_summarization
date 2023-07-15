import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open('frontPg.html', 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run()