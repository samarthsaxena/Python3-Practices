import requests
import traceback
import logging

"""IP Address to Country mapping"""


def ip_to_country(ip):
    """
    utility function to find country of the ip address.
    :param ip:
    :return:
    """
    try:
        API = "https://api.ap2country.info/ip?{}"
        response = requests.get(API.format(ip))
        data = response.json()
        return data
    except Exception as e:
        logging.error(traceback.format_exc())


print(ip_to_country("165.45.221.255"))
