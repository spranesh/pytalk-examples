import feedparser

def GetMostRecentArticles(url, n):
  articles = feedparser.parse(url)
  for blog in articles.entries[:n]:
    print blog.title
    print blog.description[:300]
    print
    

GetMostRecentArticles("http://arun.chagantys.org/blog/?feed=rss2", 8)
