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

@main.route('/technology')
def tec_news():
    '''
    The view to get technology news
    '''
    tech_news = get_news('technology')

    title = 'Technology'
    return render_template('news.html',title=title,news=tech_news)

@main.route('/sports')
def sports_news():
    '''
    The view to get sports news
    '''
    sports_news = get_news('sports')

    title = 'Sports'
    return render_template('news.html',title=title,news=sports_news)

@main.route('/health')
def health_news():
    '''
    The view to get health news
    '''
    health_news = get_news('health')

    title = 'Health'
    return render_template('news.html',title=title,news=health_news)

@main.route('/politics')
def politics_news():
    '''
    The view to get politics news
    '''
    politics_news = get_news('politics')

    title = 'Politics'
    return render_template('news.html',title=title,news=politics_news)

@main.route('/science')
def science_news():
    '''
    The view to get science news
    '''
    science_news = get_news('science')

    title = 'Science'
    return render_template('news.html',title=title,news=science_news)


@main.route('/education')
def education_news():
    '''
    The view to get education news
    '''
    education_news = get_news('education')

    title = 'Education'
    return render_template('news.html',title=title,news=education_news)


@main.route('/entertainment')
def entertainment_news():
    '''
    The view to get entertainment news
    '''
    entertainment_news = get_news('entertainment')

    title = 'Entertainment'
    return render_template('news.html',title=title,news=entertainment_news)

@main.route('/entrepreneureship')
def entrepreneureship_news():
    '''
    The view to get entrepreneureship news
    '''
    politics_news = get_news('entrepreneureship')

    title = 'Entrepreneureship'
    return render_template('news.html',title=title,news=entrepreneureship_news)

@main.route('/food')
def food_news():
    '''
    The view to get politics news
    '''
    food_news = get_news('food')

    title = 'Food'
    return render_template('news.html',title=title,news=food_news)


