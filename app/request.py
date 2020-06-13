import urllib.request,json
from .models import News,Source


api_key = None
news_source_base_url = None
news_articles_base_url = None
top_headline_base_url = None

def configure_request(app):
    global api_key, news_articles_base_url, news_source_base_url,top_headline_base_url

    api_key=app.config['NEWS_API_KEY']
    news_source_base_url=app.config['NEWS_SOURCES_BASE_URL']
    news_articles_base_url=app.config['ARTICLES_BASE_URL']
    top_headline_base_url=app.config["TOP_HEADLINE_BASE_URL"]


def process_result(list):
    '''
    A function that process raw input into the required objects

    Args:
        News list: A list of dictionaries
    Return:
        News results: A list of articles objects
    '''

    news_results = []
    for article in list:
        source = article.get('source')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        url_to_image= article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if url_to_image:
            article_object = News(source,author,title,description,url,url_to_image,publishedAt,content)
            news_results.append(article_object)

    return news_results

def get_news(search_term):
    '''
    The function that will get all news from the news api in json format
    '''
    get_news_url = news_articles_base_url.format(search_term,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()

        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_result_list = get_news_response['articles']
            news_results = process_result(news_result_list)


        return news_results

def get_sources():
    '''
    A function that will help us get the news sources from the news api
    '''
    get_sources_url = news_source_base_url.format(api_key) 

    with

