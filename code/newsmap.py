import requests
import json

def main():
    mainApi = requests.get("https://newsapi.org/")
    print(mainApi.content)

print(main())