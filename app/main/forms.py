# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Email, Regexp
from ..models import User
from flask_pagedown.fields import PageDownField

class PostForm(FlaskForm):
    title = StringField(u'标题', validators=[Required()])
    permalink = StringField(u'固定链接', validators=[Required()])
    tag = StringField(u'标签', validators=[Required()])
    body = PageDownField(u"正文", validators=[Required()])
    submit = SubmitField(u'发布')

class CommentForm(FlaskForm):
    body = StringField(u'', validators=[Required()])
    submit = SubmitField(u'发表')

