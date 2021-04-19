from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from app.models import Admin, Comment, Article2
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


# ======================
# ADMIN MANAGEMENT HOME
# ======================


@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', title='Admin')


@app.route('/admin/article_1', methods=['GET', 'POST'])
def admin_article_1():
    form = CommentForm()
    page = request.args.get('page', 1, type=int)
    user_comments = Comment.query.order_by(
        Comment.timestamp.desc()).paginate(
            page, app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('admin_article_1',
                       _anchor='comments',
                       page=user_comments.next_num) \
        if user_comments.has_next else None
    prev_url = url_for('admin_article_1',
                       _anchor='comments',
                       page=user_comments.prev_num) \
        if user_comments.has_prev else None
    all_user_comments = len(Comment.query.all())
    return render_template('admin_review_articles/admin_article1.html',
                           title='Article 1',
                           user_comments=user_comments.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           all_user_comments=all_user_comments,
                           form=form
                           )


@app.route('/admin/article_2', methods=['GET', 'POST'])
def admin_article_2():
    form = CommentForm()
    page = request.args.get('page', 1, type=int)
    user_comments = Article2.query.order_by(
        Article2.timestamp.desc()).paginate(
            page, app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('admin_article_2',
                       _anchor='comments',
                       page=user_comments.next_num) \
        if user_comments.has_next else None
    prev_url = url_for('admin_article_2',
                       _anchor='comments',
                       page=user_comments.prev_num) \
        if user_comments.has_prev else None
    all_user_comments = len(Article2.query.all())
    return render_template('admin_review_articles/admin_article2.html',
                           title='Article 2',
                           user_comments=user_comments.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           all_user_comments=all_user_comments,
                           form=form
                           )


# ---------------------
# Delete comments
# ---------------------


@app.route('/delete-user-comment/article1/user/<id>')
def delete_user_comment_article_1(id):
    user = Comment.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have deleted article1 comment made by '
          f'{user.username}, id {user.id}')
    return redirect(url_for('admin_article_1'))


@app.route('/delete-user-comment/article2/user/<id>')
def delete_user_comment_article_2(id):
    user = Article2.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have deleted article2 comment made by '
          f'{user.username}, id {user.id}')
    return redirect(url_for('admin_article_2'))


# ---------------------
# Allow comments
# ---------------------


@app.route('/allow-user-comment/article1/user/<id>')
def allow_user_comment_article_1(id):
    user = Comment.query.get(id)
    print(user)
    user.allowed_comment = 1
    db.session.add(user)
    db.session.commit()
    flash('You have allowed article1 comment from '
          f'{user.username}, id {user.id}')
    return redirect(url_for('admin_article_1'))


@app.route('/allow-user-comment/article2/user/<id>')
def allow_user_comment_article_2(id):
    user = Article2.query.get(id)
    print(user)
    user.allowed_comment = 1
    db.session.add(user)
    db.session.commit()
    flash('You have allowed article2 comment from '
          f'{user.username}, id {user.id}')
    return redirect(url_for('admin_article_2'))

# ---------------------
# Update articles pages
# ---------------------

# ========================
# END OF ADMIN MANAGEMENT
# ========================


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


# ---------------
# Article 1
# ---------------

@app.route('/article_1', methods=['GET', 'POST'])
def article_1():
    form = CommentForm()
    if form.validate_on_submit():
        user = Comment(username=form.username.data,
                       email=form.email.data,
                       comment=form.comment.data)
        db.session.add(user)
        db.session.commit()
        flash('You will receive an email confirmation '
              'when your comment is live')
        return redirect(url_for('article_1'))
    allowed_user_comments = Comment.query.filter_by(allowed_comment=1).all()
    total_comments_allowed = len(allowed_user_comments)
    return render_template('public_articles/article1.html',
                           title='Article 2',
                           form=form,
                           allowed_user_comments=allowed_user_comments,
                           total_comments_allowed=total_comments_allowed
                           )


# ---------------
# Article 2
# ---------------

@app.route('/article_2', methods=['GET', 'POST'])
def article_2():
    form = CommentForm()
    if form.validate_on_submit():
        user = Article2(username=form.username.data,
                        email=form.email.data,
                        comment=form.comment.data)
        db.session.add(user)
        db.session.commit()
        flash('You will receive an email confirmation '
              'when your comment is live')
        return redirect(url_for('article_2'))
    allowed_user_comments = Article2.query.filter_by(allowed_comment=1).all()
    total_comments_allowed = len(allowed_user_comments)
    return render_template('public_articles/article1.html',
                           title='Article 2',
                           form=form,
                           allowed_user_comments=allowed_user_comments,
                           total_comments_allowed=total_comments_allowed
                           )
