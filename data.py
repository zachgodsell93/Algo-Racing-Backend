from data_collection.main import todays_races, all_races
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use a service account

cred = credentials.Certificate('/home/zachgodsell/ar-backend/algoracing.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

print('Collecting all data')
all_races(db)
print('Completed succesfully')