import json
import requests


# This gets meetings for a given date range
def get_meetings(start_date, end_date):
    url = f"https://puntapi.com/graphql-horse-racing?operationName=meetingsIndexByStartEndDate&variables=%7B%22startDate%22%3A%22{start_date}%22%2C%22endDate%22%3A%22{end_date}%22%2C%22limit%22%3A100%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e5513fd50760a04b2d4292a0c3c2431754b1db0dda4d326b064942d0307fdd3e%22%7D%7D"

    payload={}
    headers = {
    'Authorization': 'Bearer none'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)
    try:
        data = data['data']['meetingsGrouped']
        for i in range(0,5):
            try:
                if data[i]['group'] == 'Australia':
                    meetings = data[i]['meetings']

                else:
                    pass
            except Exception as e:
                pass
    except Exception:
        pass
    return meetings

