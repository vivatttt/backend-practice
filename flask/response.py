from flask import Flask, make_response, render_template

app = Flask(__name__)


@app.route('/json/')
def json():
    return {'json': 42} # Возвращает тип application/json

@app.route('/html/')
def html():
    return render_template('index.html') # Возвращает тип text/html

@app.route('/foo')
def foo():
    response = make_response('foo foo \n be be') # тело ответа
        
    response.headers['X-Parachutes'] = 'parachutes are cool' # Устанавливаем заголовок
    response.mimetype = 'text/plain' # Меняем тип ответа
    response.status_code = 418 # Задаем статус
    response.set_cookie('foo', 'bar') # Устанавливаем cookie

    return response