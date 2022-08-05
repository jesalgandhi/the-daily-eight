import newspaper
import nltk

def fetchTodayNews(number_of_articles):
    nltk.download('punkt')
    ap_news = newspaper.build('https://reuters.com/', memoize_articles=False)
    articles = {}
    for i in range(0, number_of_articles):
        article = ap_news.articles[i]
        article.download()
        article.parse()
        article.nlp()
        summary = article.summary.replace("read more", " ").replace("Register now for FREE unlimited access to Reuters.com Register", " ")
        
        articles[i] = [article.title, summary, article.images]
    return articles