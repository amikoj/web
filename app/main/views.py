from flask import render_template,session,redirect,url_for
#导入蓝本 main
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/contact.html')
def contact():
    return render_template('contact.html')