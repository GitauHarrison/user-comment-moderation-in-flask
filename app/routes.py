from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from app.models import Admin, Comment
from app.forms import LoginForm, RegisterForm, CommentForm
from flask_login import login_required
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = CommentForm()
    if form.validate_on_submit():
        user = Comment(username=form.username.data,
                       email=form.email.data,
                       comment=form.comment.data)
        db.session.add(user)
        db.session.commit()
        flash('You will receive an email confirmation '
              'when your comment is live')
        return redirect(url_for('home'))
    allowed_user_comments = Comment.query.filter_by(allowed_comment=1).all()
    total_comments_allowed = len(allowed_user_comments)
    return render_template('home.html',
                           title='Home',
                           form=form,
                           allowed_user_comments=allowed_user_comments,
                           total_comments_allowed=total_comments_allowed
                           )


@app.route('/admin')
@login_required
def admin():
    form = CommentForm()
    page = request.args.get('page', 1, type=int)
    user_comments = Comment.query.order_by(
        Comment.timestamp.desc()).paginate(
            page, app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('admin',
                       _anchor='comments',
                       page=user_comments.next_num) \
        if user_comments.has_next else None
    prev_url = url_for('admin',
                       _anchor='comments',
                       page=user_comments.prev_num) \
        if user_comments.has_prev else None
    all_user_comments = len(Comment.query.all())
    return render_template('admin.html',
                           title='Admin',
                           user_comments=user_comments.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           all_user_comments=all_user_comments,
                           form=form
                           )


@app.route('/delete-user-comment/<id>')
def delete_user_comment(id):
    user_list = Comment.query.order_by(
        Comment.timestamp.desc()
    )
    for user_comment in user_list:
        db.session.delete(user_comment)
        db.session.commit()
        flash('You have deleted the comment made by '
              f'{user_comment.username}, id {user_comment.id}')
        return redirect(url_for('admin'))


@app.route('/allow-user-comment/<id>')
def allow_user_comment(id):
    user = Comment.query.filter_by(allowed_comment=0).first()
    print(user)
    user.allowed_comment = 1
    db.session.add(user)
    db.session.commit()
    flash(f'You have allowed the comment from {user.username}, id {user.id}')
    return redirect(url_for('admin'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Admin(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered admin!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
