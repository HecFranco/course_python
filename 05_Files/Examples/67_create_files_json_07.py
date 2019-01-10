import json
data = {'item': 'Beer', 'cost':'£4.00'}
jstr = json.dumps(data, ensure_ascii=False, indent=4)
print(jstr)
# {
#     "item": "Beer",
#     "cost": "£4.00"
# }