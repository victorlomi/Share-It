from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from sqlalchemy import desc
from app.main import bp
from app import db
import requests
from app.models import User, Post, Comment
from app.main import forms

@bp.route('/')
def index():
    # get the quote of the day
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    response = requests.get(url).json()

    # get all the posts for displaying
    posts = Post.query.order_by(desc(Post.timestamp)).all()
    return render_template('index.html', posts=posts, User=User, quote=response)

@bp.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)

@bp.route('/add-post', methods=['GET', 'POST'])
def add_post():
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))

    form = forms.AddForm()

    if form.validate_on_submit():
        post = Post(author=current_user, title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_post.html', form=form)

@bp.route('/user/<user>')
def user(user):
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(username=user).first()
    pitches = Pitch.query.filter_by(author=user).all()
    return render_template('user.html', user=user, pitches=pitches)

@bp.route('/comments/<post>')
def comments(post):
    comments = Comment.query.filter_by(post=Post.query.get(post)).all()
    return render_template('comments.html', post=Post.query.get(post), comments=comments)

@bp.route('/add-comment/<post>', methods=['GET', 'POST'])
def add_comment(post):
    # go to login in page if user is not logged in
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))

    form = forms.AddCommentForm()

    if form.validate_on_submit():
        comment = Comment(post=Post.query.get(post), body=form.body.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.comments', post=post))

    return render_template('add_comment.html', form=form)
