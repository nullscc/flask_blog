# -*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request, make_response, abort, current_app
from . import main
from .forms import PostForm, CommentForm, TagForm, TagDelForm
from ..email import send_email
from .. import db
from ..models import User, Post, Comment, Tag
from flask_login import login_required, login_user, current_user, logout_user
from ..decorators import admin_required

@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)

@main.route('/<permalink>', methods=['GET', 'POST'])
def post(permalink):
    post = Post.query.filter_by(permalink=permalink).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post, email=form.email.data, nickname=form.nickname.data)
        db.session.add(comment)
        flash(u'您的评论已被发表')
        return redirect(url_for('.post', permalink=permalink))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // \
            current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
        page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('post.html', post=post, form=form,
                           comments=comments, pagination=pagination)

@main.route('/new-post', methods=['GET', 'POST'])
@admin_required
def new_post():
    form = PostForm()    
    if form.validate_on_submit():
        post = Post(body=form.body.data, permalink=form.permalink.data, title=form.title.data)
        for tag in form.tags.data:
            post.tags.append(tag)
        db.session.add(post)
        flash(u'发布文章成功！！！')
        return redirect(url_for('.index'))
    return render_template('new_post.html', form=form)

@main.route('/edit/<permalink>', methods=['GET', 'POST'])
@admin_required
def edit(permalink):
    post = Post.query.filter_by(permalink=permalink).first()
    form = PostForm()
    if form.validate_on_submit():
        post.permalink = form.permalink.data
        post.title = form.title.data
        post.body = form.body.data
        post.tags = form.tags.data
        db.session.add(post)
        flash(u'文章编辑成功')
        return redirect(url_for('.post', permalink=post.permalink))
    form.permalink.data = post.permalink
    form.title.data = post.title
    form.tags.data = post.tags.all()
    form.body.data = post.body    
    return render_template('edit_post.html', form=form)

@main.route('/tag-manager', methods=['GET', 'POST'])
@admin_required
def tag_manager():
    tagform = TagForm()
    tagdelform = TagDelForm()
    if tagform.validate_on_submit():
        if Tag.query.filter_by(name=tagform.name.data).first():
            flash(u'标签已存在')
            return redirect(url_for('.tag_manager'))
        tag = Tag(name=tagform.name.data)
        db.session.add(tag)
        db.session.commit()
        flash(u'标签添加成功')
        return redirect(url_for('.tag_manager'))
    if tagdelform.validate_on_submit():
        for tag in tagdelform.tags.data:
            db.session.delete(tag)
        db.session.commit()
        flash(u'标签删除成功')
        return redirect(url_for('.tag_manager'))
    return render_template('tag_manager.html', form=tagform, delform=tagdelform)


@main.route('/tags/<name>', methods=['GET', 'POST'])
def tag(name):
    tag = Tag.query.filter_by(name=name).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = tag.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=10,
        error_out=False)
    page_posts = pagination.items
    print(len(page_posts))
    return render_template('index.html',
        pagination=pagination, posts=page_posts)

@main.route('/del-post/<permalink>', methods=['GET', 'POST'])
@admin_required
def del_post(permalink):
    post = Post.query.filter_by(permalink=permalink).first()
    for comment in post.comments:
        db.session.delete(comment)
    db.session.delete(post)
    flash(u'删除文章成功！！！')
    return redirect(url_for('.index'))