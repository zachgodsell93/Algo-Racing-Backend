import json
import requests


# This gets meetings for a given date range
def get_event(event_id):
    url = f"https://puntapi.com/graphql-horse-racing?operationName=eventById&variables=%7B%22eventId%22%3A%22{event_id}%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22d8d5896130db45725834006dfffe08ed23dc6f298323063d64a5d2c355b7c3e9%22%7D%7D"

    payload={}
    headers = {
    'Authorization': 'Bearer none'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)

    data = data['data']['event']
    
    return data

