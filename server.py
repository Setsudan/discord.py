from flask import Flask
from threading import Thread

#? Pour laisser le bot en ligne 24/7 avec Replit
#* Pas nécéssaire mais une des options que l'on a choisi de rajouter

app = Flask('')

@app.route('/')
def home():
    return "Ce site garde un bot en vie"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()