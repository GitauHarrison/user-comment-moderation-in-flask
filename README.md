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

## Project Design

* [Comment Moderation App Design Using Figma](https://www.figma.com/proto/M6vfs6SOptVVh1WgmGgQxa/Comment-Moderation-Demo?node-id=1%3A2&scaling=min-zoom&page-id=0%3A1)

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
$ mkvirtualenv comment_moderation # I am using virtualenvwrapper
```

4. Install project dependencies within your active virtual environment:

```python
(comment_moderation)$ pip3 install -r requirements.txt
```

5. Start the flask server:

```python
(comment_moderation)$ flask run
```

## Usage Locally

* Post several comments from the [_Home_](http://127.0.0.1:5000/home) page using dummy credentials

* Click on the [_Admin_](http://127.0.0.1:5000/login?next=%2Fadmin) page to access all user comments posted on the blog

* You will need to [register](http://127.0.0.1:5000/register) first, so create a dummy admin account

* [Log](http://127.0.0.1:5000/login?next=%2Fadmin) into the new admin account. You should be able to see all user comments

* Click _Delete_ link to delete a user's comment

* Click _Allow_ to allow a user's comment to appear in the [_Home_](http://127.0.0.1:5000/home) page

* Navigate to the [_Home_](http://127.0.0.1:5000/home) page to see all "Allowed" comments