import requests
import json

if __name__ == '__main__':
  url = 'http://httpbin.org/put'
  payload = { 'nombre':'Eduardo', 'curso': 'python', 'nivel':'intermedio'}
  headers = { 'Content-Type': 'application/json', 'Access-token': '12345678' }
  response = requests.put(url, data=json.dumps(payload), headers=headers)
  print(response.url)
  if response.status_code == 200:
    headers_response = response.headers
    server = headers_response['Server']
    print(server)