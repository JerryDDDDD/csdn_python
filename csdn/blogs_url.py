from urllib import request
from bs4 import BeautifulSoup


blog_urls=[]

def getBlogUrl(urls):
    for url in urls:
        html = request.urlopen(url)
        soup = BeautifulSoup(html.read())
        a = soup.select('.article-list .article-item-box h4 a')
        for b in a[0:] :
            if(b.attrs.get('href').__contains__('yoyo_liyy')):
                continue
            blog_urls.append(b.attrs.get('href'))
        return blog_urls
#遍历爬取的博客urls

# getBlogUrl(urls)
# for u in blog_urls:
#     print(u)