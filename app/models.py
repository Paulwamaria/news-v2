class News:
    '''
    A class to instantiate the news objects and their behaviors
    '''
    all_news_list = []
    def __init__(self,source,author,title,description,url,url_to_image,publishedAt,content):
        self.source = source 
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.publishedAt = publishedAt
        self.content = content

    def save_new(self):
        '''
        A method to save news article to all news list
        '''
        self.all_news_list.append(self)


    def delete_article(self):
        '''
        A method to delete an artile from all news list
        '''
        self.all_news_list.remove(self)


class Source:
    '''
    A class to instantiate the various news sources and their behaviors
    '''
    all_sources = []
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id 
        self.name = name 
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

    def save_source(self):
        '''
        A method to save a new source to the source list 
        '''
        all_sources.append(self)

    def delete_source(self):
        '''
        A method to remove a news source from the source list
        '''
        all_sources.remove(self)

