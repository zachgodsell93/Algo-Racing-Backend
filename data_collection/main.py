from data_collection.meetings import get_meetings
from data_collection.events import get_event
from data_collection.selection_stats import get_stats_by_event_id, get_full_selection_stats
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from stats.get_stats import selection_ratings

def all_races(db):
    today = datetime.datetime.now()
    ran = [1, 1, 1, 1]
    print(today.strftime("%Y-%m-%d"))
    for i in ran:
        today += datetime.timedelta(days=i)
        td = today.strftime("%Y-%m-%d")


        doc_ref = db.collection('meetings').document(td)

        d = get_meetings(start_date=td, end_date=td)


        try:
            for i in range(0,len(d)):
                doc_ref.collection(u'meetings').document(d[i]['id']).set(d[i])

            for i in d:
                events = i['events']
                meeting_id = i['id']
                meeting_date = i['meetingDateLocal']
                meeting_name = i['name']

                print(meeting_name)

                for i in events:
                    doc_ref = db.collection('event').document(i['id'])
                    print(f"R.{i['eventNumber']}")
                    id = i['id']
                    try:
                        d = get_event(id)
                        d['meetingId'] = meeting_id
                        d['meetingName'] = meeting_name
                        d['meetingDate'] = meeting_date
                        doc_ref.set(d) 
                    except Exception:
                        pass
                    try:
                        stats = get_stats_by_event_id(i['id'])
                        sel_ids = []
                        for i in stats:
                            i['customRatings'] = selection_ratings(i)
                            stat_ref = db.collection('selectionStats').document(i['selectionId'])
                            stat_ref.set(i)
                            sel_ids.append(i['selectionId'])
                        full_stats = get_full_selection_stats(sel_ids)
                        for i in full_stats:
                            full_ref = db.collection('fullStats').document(i['selectionId'])
                            full_ref.set(i)
                    except Exception:
                        pass
        except Exception:
            pass


def todays_races(db):
    today = datetime.datetime.now()
    td = today.strftime("%Y-%m-%d")


    doc_ref = db.collection('meetings').document(td)

    d = get_meetings(start_date=td, end_date=td)

    for i in d:
        doc_ref.collection(u'meetings').document(i['id']).set(i)

    # for i in d:
        events = i['events']
        meeting_id = i['id']
        meeting_date = i['meetingDateLocal']
        meeting_name = i['name']

        print(meeting_name)
        
        for i in events:
            doc_ref = db.collection('event').document(i['id'])
            id = i['id']
            try:
                d = get_event(id)
                d['meetingId'] = meeting_id
                d['meetingName'] = meeting_name
                d['meetingDate'] = meeting_date
                doc_ref.set(d) 
            except Exception:
                pass
            
            stats = get_stats_by_event_id(i['id'])
            sel_ids = []
            for i in stats:
                i['customRatings'] = selection_ratings(i)
                stat_ref = db.collection('selectionStats').document(i['selectionId'])
                stat_ref.set(i)
                sel_ids.append(i['selectionId'])
            full_stats = get_full_selection_stats(sel_ids)
            for i in full_stats:
                full_ref = db.collection('fullStats').document(i['selectionId'])
                full_ref.set(i)


            
def results(db):
    today = datetime.datetime.now()
    td = today.strftime("%Y-%m-%d")


    doc_ref = db.collection('meetings').document(td)

    d = get_meetings(start_date=td, end_date=td)

    for i in d:
        doc_ref.collection(u'meetings').document(i['id']).set(i)

    # for i in d:
        events = i['events']
        meeting_id = i['id']
        meeting_date = i['meetingDateLocal']
        meeting_name = i['name']

        print(meeting_name)
        
        for i in events:
            doc_ref = db.collection('event').document(i['id'])
            id = i['id']
            try:
                d = get_event(id)
                d['meetingId'] = meeting_id
                d['meetingName'] = meeting_name
                d['meetingDate'] = meeting_date
                doc_ref.set(d) 
            except Exception:
                pass
            
            stats = get_stats_by_event_id(i['id'])
            # sel_ids = []
            for i in stats:
                i['customRatings'] = selection_ratings(i)
                stat_ref = db.collection('selectionStats').document(i['selectionId'])
                stat_ref.set(i)
                # sel_ids.append(i['selectionId'])
            # full_stats = get_full_selection_stats(sel_ids)
            # for i in full_stats:
            #     full_ref = db.collection('fullStats').document(i['selectionId'])
            #     full_ref.set(i)


            
