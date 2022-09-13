import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) #This way you can choose the artist
print(json.dumps(response.json(), indent=2)) #json.dumps prints json txt in a more readable way, and you choose the length of the indentation
