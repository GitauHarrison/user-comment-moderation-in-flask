# Comment Moderation in a Flask Application

One of the challenges that administrators of an application have is the control of the comments that users post. Being able to moderate users' comments is a very important feature of a website. This application shows how you can create a custom comment moderation feature in a Flask application.

![Comment Moderation in Flask](app/static/img/comment_moderation.gif)

## Features

- Comment Moderation
- User Management
- Database Management

## Tools Used

- Flask framework
- Flask Bootstrap (CSS framework)
- Flask-WTF (Forms)
- Flask-SQLAlchemy (Database)
- Flask-Login (User Authentication)
- Flask-Migrate (Database Migration)
- Email Validator (Email Validation)
- Python for programming

## Deployment

- [Heroku](https://comment-moderation-app.herokuapp.com/)

## Testing Deployed Application

1. Post a comment in the [home page](https://comment-moderation-app.herokuapp.com/)
2. [Register for an admin account](https://comment-moderation-app.herokuapp.com/register) if you are new
3. [Login to your admin account](https://comment-moderation-app.herokuapp.com/login) to see all comments
4. [View all comments](https://comment-moderation-app.herokuapp.com/admin/dashboard) in the admin dashboard
5. You can _allow_ or _delete_ the posted comments.
6. Navigate back to the home page to see all "allowed" comments.

## Testing The Application Locally

1. Clone this repo:

```python
git clone git@github.com:GitauHarrison/user-comment-moderation-in-flask.git`
```

2. Change directory to the new repo:

```python
cd user-comment-moderation-in-flask
```

3. Create and activate a virtual environment:

```python
$ mkvirtualenv comment_moderation
```

4. Install dependencies:

```python
(comment_moderation)$ pip3 install -r requirements.txt
```

5. Run the server:

```python
(comment_moderation)$ flask run
```

## Learn 

Flask is very unopinionated. You can pretty much build whatever feature you want. If you would like to know how I was able to integrate comment moderation into this application, check out the  tutorial below:

- [Comment Moderation in Flask](https://github.com/GitauHarrison/notes/blob/master/comment_moderation.md)
