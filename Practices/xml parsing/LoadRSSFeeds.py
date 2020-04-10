import requests

def loadRSS():
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
    # creating HTTP response object from given url
    resp = requests.get(url)
    print(resp.content.decode('utf-8'))

    # saving the xml file
    with open('topnewsfeed.xml', 'w') as f:
        f.write(resp.content.decode('utf-8'))
    
    



if __name__ == '__main__':
    loadRSS()