import requests
import time
from blogs_url import getBlogUrl

urls=[]
#你的CSDN博客页数
for i in range(1,6):
    a = 'https://blog.csdn.net/qq_37745470/article/list/'+str(i)+'?'
    urls.append(a)
# 获取 CSDN 的个人所有博客链接
url = getBlogUrl(urls)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

#访问博客链接函数
def access_csdn_url():
    count =0
    try:  # 正常运行
        for i in range(len(url)):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
                time.sleep(10)
    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(10)

# 循环请求
if __name__ == '__main__':
    while(1):
        access_csdn_url()


