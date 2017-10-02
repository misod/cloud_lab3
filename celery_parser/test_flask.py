#!flask/bin/python
from flask import Flask, jsonify
from run_parser import *

app = Flask(__name__)


@app.route('/todo/', methods=['GET'])
def get_tasks():
    return run_pars()

if __name__ == '__main__':
    app.run(debug=True)
