#!flask/bin/python
from __future__ import absolute_import
from .run_parser import run_pars
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/todo/', methods=['GET'])
def get_tasks():
    return run_pars()

if __name__ == '__main__':
    app.run(debug=True)
