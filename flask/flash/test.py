from flask import Flask, flash, url_for, redirect, get_flashed_messages, render_template

app = Flask(__name__)
# устанавливаем секретный ключ для работы с сессиями
app.secret_key = "secret_key"

@app.post('/foo')
def foo():
    # Добавление флеш-сообщения.
    # Оно станет доступным только на следующий HTTP-запрос.
    # 'success' — тип флеш-сообщения. Используется при выводе для форматирования.
    # Например, можно ввести тип success и отражать его зеленым цветом. На Хекслете такого много.
    flash('This is a message', 'success')
    return redirect('/bar')

@app.get('/bar')
def bar():
    # Извлечение flash-сообщений, которые установлены на предыдущем запросе
    messages = get_flashed_messages(with_categories=True)
    print(messages)  # => [('success', 'This is a message')]
    return render_template(
        'bar.html',
        messages=messages,
    )
