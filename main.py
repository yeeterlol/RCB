import requests
import random
import string
import threading
import time

# Delay, used to prevent rate limits
delay = 0.5
# Credit to https://github.com/MrDiamond64/realm-code-gen/ for the headers!
header = {
  		"accept":     "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US",
		"cache-control": "max-age=0",
		"connection": "keep-alive",
		"dnt": "1",
		"host": "open.minecraft.net",
		"sec-fetch-dest": "document",
		"sec-fetch-mode": "navigate",
		"sec-fetch-site": "none",
		"sec-fetch-user": "?1",
		"TE": "trailers",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}

def SendRequest():
  global delay, header
  while True:
        # Generating our realm code
        letters = string.ascii_letters
        generated = ''.join(random.choice(letters) for i in range(11)) 
        link = f"https://open.minecraft.net/pocket/realms/invite/{generated}"
        r = requests.get(link, headers=header)
        # Checks status code
        if r.status_code == 404:
          print(f"Invalid | {link}")
        elif r.status_code == 200:
            print(f"Valid | {link}")
        elif r.status_code == 403:
            print("You got ratelimited, increasing delay...")
            delay += 0.5
        time.sleep(delay)



threads = []

for i in range (5):
  t = threading.Thread(target=SendRequest)
  t.daemon = True
  threads.append(t)

for i in range(5):
  threads[i].start()

for i in range(5):
  threads[i].join()
