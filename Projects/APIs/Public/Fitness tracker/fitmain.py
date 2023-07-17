import requests
import datetime as dt
import os
APP_ID = os.environ["APP_ID"].lower()
APP_KEY ='354ac52f2f1defca3c6a0426d352b786'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}
query =input("Describe your workout")
parameters = {
    "query": query,
    'gender': 'male',
    'weight_kg': '70',
    'height_cm': '180',
    'age': '18',
}
endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

sent = requests.post(endpoint, json=parameters, headers=headers)
data = sent.json()
print(data['exercises'][0]['name'])

sheetify_url = 'https://api.sheety.co/2b0abfaa449748150f97e506773072dc/myWorkouts/workouts'
time = dt.datetime.now()
for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": time.strftime("%d/%m/%y"),
            "time": time.now().hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


sent_sheet = requests.post(sheetify_url, json=sheet_inputs)
print(sent_sheet.text)
