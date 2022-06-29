import datetime
from math import nan
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
import math


def bet_results_table(db):
    today = datetime.datetime.now()
    yesterday = (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (today + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    today = today.strftime("%Y-%m-%d")
    dates = [yesterday, today, tomorrow]

    for i in dates:
                
        event_ref = db.collection('event')
        event_docs = event_ref.where('meetingDate', '==', i).stream()
        events = []
        for doc in event_docs:
            events.append(doc.to_dict())

        bet_ref = db.collection('bets')
        bet_docs = bet_ref.where('date', '==', i).stream()
        bets = []
        for doc in bet_docs:
            data = doc.to_dict()
            d = [x for x in events if x['id'] == data['eventId']]
            item = d[0]
            sel = [x for x in item['selections'] if x['id'] == data['selection']]
            sel = sel[0]
            sel['bet'] = data
            res = dict((k, item[k]) for k in ['meetingDate', 'meetingName', 'id', 'meetingId', 'eventNumber', 'isAbandoned', 'startTime'] if k in item)
            res['selection'] = sel
            res['selection']['bet']['placeBet']['payout'] = res['selection']['bet']['placeBet']['odds']*res['selection']['bet']['placeBet']['units']
            res['selection']['bet']['winBet']['payout'] = res['selection']['bet']['winBet']['odds']*res['selection']['bet']['winBet']['units']




            if np.isnan(res['selection']['bet']['winBet']['payout']) == True:
                res['selection']['bet']['winBet']['payout'] = 0
            else:
                pass
            
            if np.isnan(res['selection']['bet']['placeBet']['payout']) == True:
                res['selection']['bet']['placeBet']['payout'] = 0
            else:
                pass

            
            
            if np.isnan(res['selection']['bet']['winBet']['units']) == True:
                res['selection']['bet']['winBet']['units'] = 0
            else:
                pass
            
            if np.isnan(res['selection']['bet']['placeBet']['units']) == True:
                res['selection']['bet']['placeBet']['units'] = 0
            else:
                pass




            win_payout = res['selection']['bet']['winBet']['payout']
            place_payout = res['selection']['bet']['placeBet']['payout']
            win_units = res['selection']['bet']['winBet']['units']
            place_units = res['selection']['bet']['placeBet']['units']


            result = res['selection']['result']

            if result != None:
                if result['finishPosition'] == 1:
                    total_payout = (win_payout + place_payout) -(win_units + place_units)
                elif result['finishPosition'] >= 2 and result['finishPosition'] <= 3:
                    total_payout = place_payout - (win_units + place_units)
                elif result['finishPosition'] < 0:
                    total_payout = 0
                else:
                    total_payout = 0 - win_units - place_units

            else:
                total_payout = None        
            res['totalPayout'] = total_payout
            bets.append(res)
            full_ref = db.collection('bettingResults').document(res['selection']['id'])
            full_ref.set(res)

        print(len(bets))


# bet_results_table()


def bet_results_table_historic(db):
   
    event_ref = db.collection('event')
    event_docs = event_ref.stream()
    events = []
    for doc in event_docs:
        events.append(doc.to_dict())

    bet_ref = db.collection('bets')
    bet_docs = bet_ref.stream()
    bets = []
    for doc in bet_docs:
        data = doc.to_dict()
        d = [x for x in events if x['id'] == data['eventId']]
        item = d[0]
        sel = [x for x in item['selections'] if x['id'] == data['selection']]
        sel = sel[0]
        sel['bet'] = data
        res = dict((k, item[k]) for k in ['meetingDate', 'meetingName', 'id', 'meetingId', 'eventNumber', 'isAbandoned', 'startTime'] if k in item)
        res['selection'] = sel
        res['selection']['bet']['placeBet']['payout'] = res['selection']['bet']['placeBet']['odds']*res['selection']['bet']['placeBet']['units']
        res['selection']['bet']['winBet']['payout'] = res['selection']['bet']['winBet']['odds']*res['selection']['bet']['winBet']['units']




        if np.isnan(res['selection']['bet']['winBet']['payout']) == True:
            res['selection']['bet']['winBet']['payout'] = 0
        else:
            pass
        
        if np.isnan(res['selection']['bet']['placeBet']['payout']) == True:
            res['selection']['bet']['placeBet']['payout'] = 0
        else:
            pass

        
        
        if np.isnan(res['selection']['bet']['winBet']['units']) == True:
            res['selection']['bet']['winBet']['units'] = 0
        else:
            pass
        
        if np.isnan(res['selection']['bet']['placeBet']['units']) == True:
            res['selection']['bet']['placeBet']['units'] = 0
        else:
            pass




        win_payout = res['selection']['bet']['winBet']['payout']
        place_payout = res['selection']['bet']['placeBet']['payout']
        win_units = res['selection']['bet']['winBet']['units']
        place_units = res['selection']['bet']['placeBet']['units']


        result = res['selection']['result']

        if result != None:
            if result['finishPosition'] == 1:
                total_payout = (win_payout + place_payout) -(win_units + place_units)
            elif result['finishPosition'] >= 2 and result['finishPosition'] <= 3:
                total_payout = place_payout - (win_units + place_units)
            elif result['finishPosition'] < 0:
                total_payout = 0
            else:
                total_payout = 0 - win_units - place_units

        else:
            total_payout = None        
        res['totalPayout'] = total_payout
        bets.append(res)
        full_ref = db.collection('bettingResults').document(res['selection']['id'])
        full_ref.set(res)

    print(len(bets))
