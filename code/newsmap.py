import requests, json, time

def main():
    print("Searching for articles\n")
    r = requests.get("https://newsapi.org/v2/everything?q=Crypto&apiKey=539c855342ad4d198670f6859e60f978")
    mainContent = r.json()
    for content in mainContent['articles']:
        print(content['title'], end='\r')
        if "crash" in content['description']:
            print("")
        time.sleep(0.01)


print(main())