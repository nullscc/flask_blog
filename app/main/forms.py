# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Email, Regexp
from ..models import User, Tag
from flask_pagedown.fields import PageDownField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

def get_tags():
    return Tag.query.all()

class PostForm(FlaskForm):
    title = StringField(u'标题', validators=[Required()])
    inhomepage = BooleanField(u'是否在首页显示', default=True)
    permalink = StringField(u'固定链接', validators=[Required()])
    tags = QuerySelectMultipleField(u'标签', validators=[Required()], query_factory=get_tags, get_label='name')
    body = PageDownField(u"正文", validators=[Required()])
    submit = SubmitField(u'发布')

class CommentForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64), Email()])
    nickname = StringField(u'昵称', validators=[Required()])
    body = StringField(u'评论内容', validators=[Required()])
    submit = SubmitField(u'发表')

class TagForm(FlaskForm):
    name = StringField(u'标签名称', validators=[Required()])
    submit = SubmitField(u'增加')

class TagDelForm(FlaskForm):
    tags = QuerySelectMultipleField(u'已有标签', query_factory=get_tags, get_label='name', validators=[Required()])
    submit = SubmitField(u'删除')

class TagRenameForm(FlaskForm):
    srcname = QuerySelectField(u'源标签名', query_factory=get_tags, get_label='name')
    desname = StringField(u'目的标签名', validators=[Required()])
    submit = SubmitField(u'改名')