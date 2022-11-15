import requests

def comunicateApi(imagePath, date):
    return requests.post("http://localhost:8080/api/send-message", json = createJson(imagePath, date))


def createJson(imagePath, date):
    return {'imagePath': imagePath, 'date' : date}