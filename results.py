from data_collection.main import results
from stats.fix_data import bet_results_table
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use a service account
<<<<<<< HEAD
cred = credentials.Certificate('/home/zachgodsell/ar-backend/algoracing.json')
=======
<<<<<<< HEAD
cred = credentials.Certificate('/home/zachgodsell/ar-backend/algoracing.json')
=======
cred = credentials.Certificate('/home/zachgodsell/ar-backend/algoracing.json')
>>>>>>> 3d0be3c68142c932ac5c073ae56dfcc3ae296149
>>>>>>> f79984b5ce4b1a61a11b5ad124c93ac2213f3e5c
firebase_admin.initialize_app(cred)

db = firestore.client()

results(db)
bet_results_table(db)
