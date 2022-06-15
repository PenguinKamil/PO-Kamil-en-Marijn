from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from the depths of Uk!'


app.run(host='0.0.0.0', port=81, true)