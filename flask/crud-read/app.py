from flask import Flask, render_template, request
from repository import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.get('/posts')
def posts():
    page = int(request.args.get('page', 1))

    cur_posts = repo.content()[(page - 1) * 5:page * 5]

    return render_template(
        'posts/index.html',
        posts=cur_posts,
        cur_page=page
    )

@app.get('/posts/<slug>')
def post(slug):

    cur_post = repo.find(slug)
    if not cur_post:
        return 'Page not found', 404
    return render_template(
        'posts/show.html',
        post=cur_post
    )
# END
