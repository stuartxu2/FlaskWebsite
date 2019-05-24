from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd


app = flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return '<h1>hello World!</h1>'


if __name__== '__main__':
    app.run(host='0.0.0.0', port = 3333, debug = True)
