from flask import render_template, url_for, request, redirect
from . import main
from ..request import get_news, get_sources,get_top_headlines

@main.route('/')
def index():
    '''
    Home page view
    '''
    title = 'World top news'
    message = 'Welcome to world top news'

    business_articles = get_news('business')
    news_sources = get_sources()
    top_headlines = get_top_headlines("technology")

    search_term = request.args.get('search_query')
    print("*"*20,search_term)
    
    if search_term:
        return redirect(url_for('.search',search_term = search_term))
    else:
        return render_template('index.html',title = title, message = message,business_articles = business_articles, news_sources = news_sources,top_headlines=top_headlines)

@main.route('/sources')
def sources():
    '''
    Sources view page
    '''
    title='news sources'

    sources_list = get_sources()

    return render_template('source.html',title=title,sources = sources_list)

@main.route('/search/<search_term>')
def search(search_term):
    '''
    A view to the searched results
    '''
    searched_news = get_news(search_term)
    message = 'Found the following articles '

    return render_template('search.html',news_articles = searched_news)