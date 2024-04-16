from flask import Flask, request, make_response

app = Flask(__name__)

# http://127.0.0.1:8000/users/?page=12&per=5

@app.route('/users')
def users():
    print(request.args)
    page = request.args.get('page', 1)
    per = request.args.get('per', 10, type=int)

    response = make_response(f'Okay!\nper is {per}\npage is {page}\n')
    response.status_code = 200
    return response