import requests
import json
from urllib.parse import quote


def get_stats_by_event_id(event_id):
    url = f"https://puntapi.com/graphql-horse-racing?operationName=statsByEventId&variables=%7B%22eventId%22%3A%22{event_id}%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22f4b6d61cf81e806e3ec0c666815a539c79de40186d59d4ee2b77397643ad3e03%22%7D%7D"

    payload={}
    headers = {
    'Authorization': 'Bearer none'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)
    data = data['data']['stats']

    return data


def get_full_selection_stats(selection_array):
    sel_string = ""
    for i in selection_array:
        sel_string = sel_string + f"%22{i}%22%2C"
    sel_string = sel_string[:-3]
    url = f"https://puntapi.com/graphql-horse-racing?operationName=fullFormsBySelectionIds&variables=%7B%22selectionIds%22%3A%5B{sel_string}%5D%2C%22limit%22%3A4%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%226d10b9a755f9e84fbb92877daa9a192286a638a44442a60ecc575ee89be74e0c%22%7D%7D"

    payload={}
    headers = {
    'Authorization': 'Bearer none'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    data = data['data']['competitorForms']
    return_data = []
    for i in data:
        horse_data = []
        # print()
        for f in i['forms']:
            if f['isTrial'] == True or f['competitorFormBenchmark'] == None:
                pass
            elif f['isTrial'] == False or f['competitorFormBenchmark'] != None:
                cfb = f['competitorFormBenchmark']
                winner_time_dif = cfb['winnerTimeDifference']
                runner_time_dif = cfb['runnerTimeDifference']
                l200_time_dif = cfb['runnerTimeDifferenceL200']
                l400_time_dif = cfb['runnerTimeDifferenceL400']
                l600_time_dif = cfb['runnerTimeDifferenceL600']
                l200_pos = cfb['runnerRacePositionL200']
                l400_pos = cfb['runnerRacePositionL400']
                l600_pos = cfb['runnerRacePositionL600']
                finish_pos = f['finishPosition']

                race_data = {
                    'winnerTimeDif': winner_time_dif,
                    'runnerTimeDif': runner_time_dif,
                    'l200TimeDif': l200_time_dif,
                    'l400TimeDif': l400_time_dif,
                    'l600TimeDif': l600_time_dif,
                    'l200Pos': l200_pos,
                    'l400Pos': l400_pos,
                    'l600Pos': l600_pos,
                    'finishPos': finish_pos 
                }
                # print(race_data)
                horse_data.append(race_data)
        # print(horse_data)
        
        l200 = 0.00
        l400 = 0.00
        l600 = 0.00

        l6_imp = 0
        l4_imp = 0
        l2_imp = 0

        for h in horse_data:
            try:
                l6_imp = l6_imp + (int(h['l600Pos']) - int(h['finishPos']))
            except Exception:
                l6_imp = l6_imp + 0
            try: 
                l4_imp = l4_imp + (int(h['l400Pos']) - int(h['finishPos']))
            except Exception:
                l4_imp = l4_imp + 0
            try:
                l2_imp = l2_imp + (int(h['l200Pos']) - int(h['finishPos']))
            except Exception:
                l2_imp = l2_imp + 0

            try:
                l200 = l200 + float(h['l200TimeDif'])
            except Exception:
                l200 = l200 + 0.00
            
            try:
                l400 = l400 + float(h['l400TimeDif'])
            except Exception:
                l400 = l400 + 0.00
            
            try:
                l600 = l600 + float(h['l600TimeDif'])
            except Exception:
                l600 = l600 + 0.00

        sorted_data = {
            'selectionId': i['selectionId'],
            'l200PositionImprove': l2_imp,
            'l400PositionImprove': l4_imp,
            'l600PositionImprove': l6_imp,
            'l200TimeImprove': l200,
            'l400TimeImprove': l400,
            'l600TimeImprove': l600,
        }
        # print(sorted_data)
        return_data.append(sorted_data)
    return return_data

