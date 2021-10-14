import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import *

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    u'name': u'Los Angeles ',
    u'state': u'CA',
    u'country': u'USA'
}

db.collection('persons').document('names').set(data)