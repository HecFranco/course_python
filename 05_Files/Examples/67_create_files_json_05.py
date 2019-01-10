import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
json_file = json.dumps(data, sort_keys=True, indent=4)
# {
#     "people": [
#         {
#             "from": "Nebraska", 
#             "name": "Scott"
#             "website": "stackabuse.com", 
#         }
#     ]
# }