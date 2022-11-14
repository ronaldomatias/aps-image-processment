import requests

def comunicateApi():
    return requests.get("http://localhost:8080/send-message")
