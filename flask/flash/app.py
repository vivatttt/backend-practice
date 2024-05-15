from flask import (
    Flask,
    flash,
    get_flashed_messages,
    render_template,
    redirect,
    url_for
)
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# BEGIN (write your solution here)
@app.post('/courses')
def courses():
    flash('Course Added', 'success')
    return redirect('/')

@app.get('/')
def main():
    messages = get_flashed_messages(with_categories=True)

    return render_template(
        'index.html',
        messages=messages
    )

# END
