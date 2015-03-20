'''
Tutorial from https://stormpath.com/blog/build-a-flask-app-in-30-minutes/

By Randall Degges
'''

from datetime import datetime

# Flask imports
from flask import (
  Flask,
  abort,
  flash,
  redirect,
  render_template,
  request,
  url_for
  )

# Imports that allow for easy user appliactions
from flask.ext.stormpath import (
  StormpathError,
  StormpathManager,
  User,
  login_required,
  login_user,
  logout_user,
  user
  )

# Set the application configurations
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'some_really_long_random_string_here'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey-1KUHS5AMKX9K1WE6Y9K85WK8B.properties'
app.config['STORMPATH_APPLICATION'] = 'flaskr'

stormpath_manager = StormpathManager(app)

# Default method that shows the posts
@app.route('/')
def show_posts():

  # Create an empty list of posts
  posts = []

  # Run through the accounts and check the posts from users
  for account in stormpath_manager.application.accounts:
    if account.custom_data.get('posts'):
      posts.extend(account.custom_data['posts'])

  # Sort the posts by date inserted
  posts = sorted(posts, key=lambda k: k['date'], reverse=True)

  return render_template('show_posts.html', posts = posts)

# Method that allows logged in users to add posts
@app.route('/add', methods=['POST'])
@login_required
def add_post():

  # Gives the user a custom post dictionary
  if not user.custom_data.get('posts'):
    user.custom_data['posts'] = []

  # Inserts the data into the posts distionary with date, title, and text
  user.custom_data['posts'].append({
    'date': datetime.utcnow().isoformat(),
    'title': request.form['title'],
    'text': request.form['text'],
  })
  user.save()

  # Tells the user that their post was successfully posted
  flash('New post successfully added.')

  return redirect(url_for('show_posts'))

# Method that attempts to login a user
@app.route('/login', methods = ['GET', 'POST'])
def login():
  error = None

  # Attempt to login using email and password
  if request.method == 'POST':
    try:
      _user = User.from_login(
        request.form['email'],
        request.form['password'],
        )

      # No errors occur and user is logged in
      login_user(_user, remember = True)
      flash('You were logged in.')

      return redirect(url_for('show_posts'))

    except (StormpathError, err):
      error = err.message

  return render_template('login.html', error = error)

# Method that logs out the user
@app.route('/logout')
def logout():

  # Logs the user out
  logout_user()
  flash('You were logged out.')

  return redirect(url_for('show_posts'))

if __name__ == '__main__':
  app.run()
