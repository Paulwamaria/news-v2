from flask import render_template, url_for, request, redirect
from . import main


@main.route('/')
def index():
    '''
    Home page view
    '''
    title = 'World top news'
    message = 'Welcome to world top news'


    return render_template('index.html',title = title, message = message)
