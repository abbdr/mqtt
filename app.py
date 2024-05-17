import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
import library.client as mqtt_client

import random
from datetime import datetime
import pytz


# utcmoment_naive = datetime.utcnow()
# utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
ct = datetime.now().astimezone(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S")
# ct = pytz.timezone("Asia/Jakarta").localize(datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

# Authenticate to Firestore with the JSON account key.
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-abdul-test-aam")
# Create a reference to the Google post.
doc_ref = db.collection("posts").document("Google")


# mqtt
broker = 'broker.emqx.io'
port = 1883
topic = "alarm_anti_maling"
# Generate a Client ID with the subscribe prefix.
client_id = f'abdul-subscribe-test-python-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'
# message = []
num = 1
data = []

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global num, data, doc_ref, doc
        message = f"{msg.payload.decode().upper()} &emsp; at `{ct}` "
        # update operation (add new key value)
        doc_ref.update({f'{num}': message})
        num += 1

        print(message)
        st.markdown(message)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    global num, data, doc_ref, doc
    client = connect_mqtt()
    subscribe(client)
    if 'file' not in st.session_state:
        # Then get the data at that reference.
        doc = doc_ref.get()
        data  = doc.to_dict()
        # Let's see what we got!
        for i in range(1,len(data)+1):
          st.write(data[f"{i}"])
          num += 1
        st.session_state.file = 0
    client.loop_forever()


if __name__ == '__main__':
    run()