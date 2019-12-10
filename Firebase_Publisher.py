from firebase import Firebase

config = {
  "apiKey": "AIzaSyCToVfJB1CIaxVbzp9FN82561Di4cIsXLg",
  "authDomain": "smarthomeautomation-1aa7c.firebaseapp.com",
  "databaseURL": "https://smarthomeautomation-1aa7c.firebaseio.com/",
  "storageBucket": "smarthomeautomation-1aa7c.appspot.com"
}

def publish(temp, humidity):
    print("Publising to firebase!")
    
    firebase = Firebase(config)
    db=firebase.database()
    data={"temperature":temp, "humidity":humidity}
    db.child("dht").push(data)