import requests
import json
query = input("What type of news you are interested in ??")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-02&sortBy=publishedAt&apiKey=02ddb7124aee421b83fbde0380684f19"
req = requests.get(url)
news = json.loads(req.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------------------------------------------------------")

