from datetime import datetime

def getDateNow():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")