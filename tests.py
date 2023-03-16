import json

with open("dict_for_anekdot.json",encoding="utf-8") as file:
    dict_for_anekdots = json.load(file)

search_id = "1382678123"

if search_id in dict_for_anekdots:
    print("Есть")
else:
    print("Длбавляем")