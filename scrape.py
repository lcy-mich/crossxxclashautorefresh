from requests import get
from time import time
from json import loads

class CrossXXScraper:
    lastUpdate = 0
    lastUpdateRemaining = 4*60*60
    link = "https://www.freeclash.top/ui/api/clash_subscriptions"
    subsType = {
        "hysteria" : 0,
        "vmess" : 1,
        "ssr" : 2
    }
    subsData = {
        "hysteria" : None,
        "vmess" : None,
        "ssr" : None
    }
    cookies = {"clash_ui_verified" : "djE6MTc4NzQwODIwNw.RR6HG65LrdFhWGBmYAYQpfjn4rwH1uzoEzoXMYh9r4w"}

    def get(self, subType):
        print("getting "+subType)
        self.update(time())
        return self.subsData[subType]
        
    def update(self, currentTime):
        if (currentTime - self.lastUpdate) > self.lastUpdateRemaining:
            print("updating")
            try:
                clash_subs = get(self.link, cookies=self.cookies)
                clash_subs.raise_for_status()
                data = loads(clash_subs.text)["subscriptions"]

                for subType, index in self.subsType.items():
                    url = data[index]["subscription_url"]
                    datum = get(url)
                    datum.raise_for_status()
                    self.subsData[subType] = datum.text

                self.lastUpdate = int(data[1]["subscription_url"].split("/")[6])
            
            except Exception as err:
                print("errored: " + repr(err))
        else:
            print("no need for update")
            