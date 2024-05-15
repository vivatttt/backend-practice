from flask import Flask, redirect, render_template, request
# BEGIN (write your solution here)
from validator import validate
# END
import os

from data import Repository


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
        )


# BEGIN (write your solution here)
@app.post('/courses')
def courses():
    course = {
        'paid' : request.form.get('paid', ''),
        'title' : request.form.get('title', '')
    }

    if not validate(course):
        return render_template(
            'courses/new.html',
            data=course,
            error="Can't be blank"
        ), 422
    repo.save(course)
    return redirect('/courses', 302)


@app.route('/courses/new', methods=['post', 'get'])
def course_new():

    course = {
        'paid' : '',
        'title' : ''
    }

    error = {}

    return render_template(
        'courses/new.html',
        data=course,
        error=error
    )
# END
