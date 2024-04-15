from flask import Flask, request

'''
export FLASK_APP=example:app - устанавливает переменную окружения FLASK_APP. Теперь при запуске flask-приложения app будет искать в example
python -m flask routes - вывод всех маршрутов в приложении
'''

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    return 'Hello from GET /users'
