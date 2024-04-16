from flask import Flask, render_template



users = [
  {
    'id': 4,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@gmail.com',
  },
  {
    'id': 5,
    'first_name': 'German',
    'last_name': 'Dawg',
    'email': 'gdwg@gmail.com',
  }
  
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
def find_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None

@app.route('/users/<id>')
def user(id):
    cur_user = find_user(int(id))
    if not cur_user:
        return 'Page not found', 404
    return render_template(
        'users/show.html',
        user=cur_user
    )
@app.route('/users')
def return_users():
    return render_template(
        'users/index.html',
        users=users
    )
# END
