import random

adsAndClicks = {}

with open("train.csv") as f:
    for line in f:
        details = line.split(",")
        adId = details[0]
        if adId == "ID":
            continue
        clicks = int(details[-1])
        if adId in adsAndClicks:
            adsAndClicks[adId] += clicks
        else:
            adsAndClicks[adId] = clicks

print "ID,click"
with open("test.csv") as queriesFile:
    for line in queriesFile:
        details = line.split(",")
        adId = details[0]
        if adId == "ID":
            continue
        print adId+","+str(random.randint(30,70)/100.0)
