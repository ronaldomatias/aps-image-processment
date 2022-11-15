import requests

def comunicateApi(imagePath):
    return requests.post("http://localhost:8080/api/send-message", json = createJson(imagePath))


def createJson(imagePath):
    return {'imagePath': imagePath}