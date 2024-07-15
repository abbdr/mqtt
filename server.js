// import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
// import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-database.js";

import { initializeApp } from 'firebase/app';
import { getDatabase, ref, update, onValue, push } from 'firebase/database';

const firebaseConfig = {
  apiKey: "AIzaSyAxsDOcCjZfFpvpn392rXtVdH2WyOzmVIs",
  authDomain: "streamlit-abdul-test-aam.firebaseapp.com",
  databaseURL: "https://streamlit-abdul-test-aam-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "streamlit-abdul-test-aam",
  storageBucket: "streamlit-abdul-test-aam.appspot.com",
  messagingSenderId: "530196732093",
  appId: "1:530196732093:web:3e350521707608f1c53fd4",
  measurementId: "G-3E68DB2HDM",
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase();
let reference = ref(db, 'aam-db/');

import * as mqtt from 'mqtt';

const protocol = 'wss';
const host = 'broker.emqx.io';
const port = '8084';
const path = '/mqtt';
const clientId = `mqtt_${Math.random().toString(16).slice(3)}_${Math.random().toString(16).slice(3)}_${Math.random().toString(16).slice(3)}`;

const connectUrl = `${protocol}://${host}:${port}${path}`;

const client = mqtt.connect(connectUrl, {
  clientId,
  clean: true,
  connectTimeout: 4000,
  reconnectPeriod: 1000,
});

const topic = 'alarm_anti_maling';

client.on('connect', () => {
  console.log('Connected');
  client.subscribe([topic], () => {
    console.log(`Subscribe to topic '${topic}'`);
  })
});

client.on('message', (topic, payload) => {
  let msg = payload.toString();
  msg = msg.toUpperCase();
  const d = new Date();
  const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  let day = weekday[d.getDay()];
  let time = new Date().toLocaleString('en-US', {
    timeZone: 'Asia/Jakarta',
  });
  time = time.replaceAll(',','&ensp;');
  msg = msg + ': &emsp;' + day + ', &ensp;' + time;
  console.log(msg);

  reference = ref(db, 'aam-db/', time);

  push(reference,{
    msg : msg
  });

});

