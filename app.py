import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict',methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)