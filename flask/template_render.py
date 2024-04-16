from flask import Flask, render_template

app = Flask(__name__)

@app.route('/courses/')
def courses():

    courses_list = [
        {
            'id' : 1,
            'name' : 'Backend'
        },
        {
            'id' : 2,
            'name' : 'Frontend'
        },
        {
            'id' : 31,
            'name' : 'ML'
        }
    ]

    return render_template(
        'courses/view.html',
        courses = courses_list
    )