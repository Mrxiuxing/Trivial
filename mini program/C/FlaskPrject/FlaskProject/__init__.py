from flask import Flask
from flask_bootstrap import Bootstrap
from FlaskProject.extension import init_ext
from FlaskProject.setting import envs
from FlaskProject.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库
    init_ext(app=app)

    # 初始化路由
    init_blue(app=app)

    # 初始化Bootstrap
    bootstrap = Bootstrap(app)

    return app
