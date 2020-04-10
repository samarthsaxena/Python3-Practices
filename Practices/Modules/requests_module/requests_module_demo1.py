import requests
from pip._vendor.distlib.compat import raw_input


def make_req_to(url):
    """
    Make a request to URL and return the response
    :param url:
    :return:
    """
    print("Making req to ",url)
    data = requests.get(url)
    print(data)
    return data.json()




def urls_list():
    """
    Assemble the requested urls and return the list of urls
    :return:
    """
    urls = raw_input("Enter URLs to make requests").split(" ")
    print("input strings are: ",urls)
    return urls



def main():
    urls = urls_list()
    print(urls)
    for url in urls:
        data_from_url = make_req_to(url)
        print(data_from_url)
        # with open("URLS_Data.out","a") as url_data:
        #     url_data.write("**************Begin for : {}***********************".format(url))
        #     url_data.write(data_from_url)
        #     url_data.write("*********************************End of response************************** ")


if __name__ == '__main__':
    main()





