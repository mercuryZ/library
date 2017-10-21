# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

# 1.程序初始化
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

# 2.写路由 视图函数
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# 3.启动服务器
if __name__ == '__main__':
    manager.run()