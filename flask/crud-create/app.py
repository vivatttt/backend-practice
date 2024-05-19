from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)
import os

from repository import PostsRepository
from validator import validate


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
        )



@app.get('/posts/new')
def new_posts_get():
    posts = errors = []

    return render_template(
        'posts/new.html',
        posts=posts,
        errors=errors
    )

@app.post('/posts')
def posts_post():
    repo = PostsRepository()

    data = request.form.to_dict()
    errors = validate(data)

    if errors:
        return render_template(
            'posts/new.html',
            posts=data,
            errors="Can't be blank"
        ), 422
    repo.save(data)
    flash('Post has been created')

    return redirect(url_for('posts_get'))
