import json
data = {'item': 'Beer', 'cost':'£4.00'}
jstr = json.dumps(data, indent=4)
print(jstr)
# {
#     "item": "Beer",
#     "cost": "\u00a34.00"
# }