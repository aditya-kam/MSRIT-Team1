import json
import requests


def info_company():
    print()
    url = (
        "https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=96308e6d093002a1a013bc8ba1ece1d9")
    get_info = requests.get(url).text
    get_details = json.loads(get_info)
    for i in get_details:
        print(i["description"])


info_company()
