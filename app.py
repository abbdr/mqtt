import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
# db = firestore.Client.from_service_account_json("key.json")
import json
key_dict = json.loads(st.secrets["textkey"])
# db = firestore.Client.from_service_account_json(key_dict)
# creds = service_account.Credentials.from_service_account_info(key_dict)
# db = firestore.Client(credentials=creds, project="streamlit-abdul-test-aam")

# Create a reference to the Google post.
# doc_ref = db.collection("posts").document("Google")

# Then get the data at that reference.
# doc = doc_ref.get()

# data  = doc.to_dict()

# Let's see what we got!
# for i in range(1,len(data)+1):
#   st.write(data[f"{i}"])

st.write(key_dict)