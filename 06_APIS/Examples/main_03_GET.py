import requests

if __name__ == '__main__':
  url = 'http://httpbin.org/get?nombre=eduardo&curso=python'
  response = requests.get(url)
  # print(response)
  if response.status_code == 200:
    content = response.content
    print(content)