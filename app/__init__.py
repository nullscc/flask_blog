 # -*- coding: utf-8 -*-     
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

from flask_pagedown import PageDown
# 把PageDown集成到Flask_WTF表单中

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# 设为 'strong' 时， Flask-Login 会记录客户端 IP 地址和浏览器的用户代理信息， 如果发现异动就登出用户。

login_manager.login_view = 'auth.login'
# login_view 属性设置登录页面的端点。

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # 注册蓝本时使用的 url_prefix 是可选参数。如果使用了这个参数，注册后蓝本中定义的所有路由都会加上指定的前缀， 即这个例子中的 /auth。

    return app