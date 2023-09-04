import json

data = {
    "browserType": "chrome",
    "URL": "https://buyme.co.il/"
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)