from flask import Flask, jsonify, request
from data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return "<a href='/companies'>Companies</a>"


@app.route('/companies')
def return_companies():
    page = request.args.get('page', -1, type=int)
    per = request.args.get('per', -1, type=int)
    if page == -1 or per == -1:
        return jsonify(companies[0:5])
    return jsonify(companies[(page - 1) * per:page * per])

