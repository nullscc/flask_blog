 # -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')

class RegistrationForm(FlaskForm):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64), Email()])
    username = StringField(u'昵称', validators=[
    Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, '
    'numbers, dots or underscores')])
    password = PasswordField(u'密码', validators=[
    Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField(u'再次确认密码', validators=[Required()])
    submit = SubmitField(u'注册')
    def validate_email(self, field):        #以validate_开头的函数和常规的验证函数一起被自动调用
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')