import requests

# Case 1: Response HTML:
try:
    url="https://www.youtube.com"
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
except:
    print('Error, Review the Code')

# Case 2: Response JSON:
try:
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print(data)
    else:
        print('ERROR en URL')
except:
    print('Error, Review the Code')




