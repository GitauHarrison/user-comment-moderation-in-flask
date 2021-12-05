from flask.helpers import url_for
from werkzeug.utils import redirect
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import CommentForm, AdminRegistrationForm, AdminLoginForm
from app.models import UserComment, Admin
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    users = UserComment.query.filter_by(allowed_comment=True).all()
    form = CommentForm()
    if form.validate_on_submit():
        user = UserComment(
            username=form.username.data,
            email=form.email.data,
            content=form.comment.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Your comment has been posted! The admin will review it shortly.')
        return redirect(url_for('index'))
    return render_template(
                           'index.html',
                           form=form,
                           users=users
                           )


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        user = Admin(
            username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user! Login to contunue.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('admin_dashboard'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    users = UserComment.query.all()
    return render_template('admin/dashboard.html', users=users)


@app.route('/admin/delete/<int:id>')
@login_required
def admin_delete(id):
    user = UserComment.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash(f'Comment {id} deleted!')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/allow/<int:id>')
@login_required
def admin_allow(id):
    user = UserComment.query.get_or_404(id)
    user.allowed_comment = True
    db.session.commit()
    flash(f'Comment {id} allowed!')
    return redirect(url_for('admin_dashboard'))
