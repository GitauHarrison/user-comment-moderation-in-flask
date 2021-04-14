# Add Comment Moderation to a Flask Blog

![User Comment Moderation](app/static/images/user_comment_moderation.gif)

If you run a blog, you may desire to have control over what users of your blog post. You want to ensure that the comments featured in any of the blogs posted on your site align with your vision for the blog. Here, I show how this feature can be added to a blog built using Python and the Flask web framework.

## Features

* User registration
* Handling of user login sessions
* Password reset 
* Database management

## Tools Used

* Flask framework
* Python and JavaScript for programming
* Flask SQLAlchemy for creation of database
* Flask migrate to handle database migrations
* Flask bootstrap for styling and mobile responsiveness
* Flask mail to handle password resets
* Flask wtf for form creation
* Flask bcrypt for extra password hashing
* Email validator to ensure user emails are valid
* Python dotenv to load hidden environment variables

## Testing Locally

1. Clone this repo:

```python
$ git clone git@github.com:GitauHarrison/user-comment-moderation-in-flask.git
```

2. Move into the cloned directory:

```python
$ cd user-comment-moderation-in-flask
```

3. Create and activate your virtual environment:

```python
$ mkvirtualenv comment_moderation
```

4. Install project dependencies within yoru virtual environment:

```python
(comment_moderation)$ pip3 install -r requirements.txt
```

5. Start the flask server:

```python
(comment_moderation)$ flask run
```

## Usage

* Post several comments from the home page using dummy credentials

* Click on the _Admin_ page to access all user comments posted on the blog

* You will need to register first, so create a dummy admin account

* Log into the admin account. You should be able to see all user comments

* Click _Delete_ link to delete a user's comment

* Click _Allow_ to allow a user's comment to appear in the home page

* Navigate to the _Home_ page to see all "Allowed" comments