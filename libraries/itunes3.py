import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#Prints only the name of the track from the artists inserted
o = response.json()
for result in o["results"]:
    print(result["trackName"])