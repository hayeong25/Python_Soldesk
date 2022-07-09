from urllib.request import urlopen

api = "https://api.imify.ngne"

url = api + "?" + "format=json"

values = {"format": "json"}


res = urlopen(url).read().decode("UTF-8")
print(res)
