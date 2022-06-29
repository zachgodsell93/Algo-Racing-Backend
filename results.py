from data_collection.main import results
from stats.fix_data import bet_results_table
from stats.fix_data import bet_results_table_historic
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use a service account
cred = credentials.Certificate('/home/zachgodsell/ar-backend/algoracing.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

results(db)
bet_results_table(db)
bet_results_table_historic(db)