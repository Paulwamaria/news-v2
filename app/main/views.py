from flask import render_template, url_for, request, redirect
from . import main
from ..request import get_news

@main.route('/')
def index():
    '''
    Home page view
    '''
    title = 'World top news'
    message = 'Welcome to world top news'

    news_articles = get_news('business')

    return render_template('index.html',title = title, message = message,business_news = news_articles)
