
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if not firebase_admin._apps:
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('private_key.json')
    # Initialize the app with a service account, granting admin privileges
    connection = firebase_admin.initialize_app(cred, 
    {
        'databaseURL': "https://demo1-757af-default-rtdb.firebaseio.com/"
    })

ref = db.reference('demo1')
result = ref.get()
finalResult = result[list(result)[-1]]

encoder = json.JSONEncoder()
jsonOutput = encoder.encode(finalResult)
OutputFile = open('FinalJSON.json','w')
OutputFile.close()