import requests

def eroor_page(text):
    status = requests.get('http://127.0.0.1:800/')
    print(status.status_code)

eroor_page("sdg")