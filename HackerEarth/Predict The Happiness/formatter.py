import sys

g = open('Formatted_Data/train.csv', 'w')
count = 0
with open('Given_Data/train.csv') as f:
    singleData = ""
    current = 10326
    for line in f.readlines():
        line = line[:-1]
        if line[2:7] == str(current+count):
            count += 1
            if singleData != "":
                dataParts = singleData.split(",")
                if dataParts[-1] == "not happy":
                    sentiment = "0"
                else:
                    sentiment = "4"
                review = "".join(dataParts[1:-3]).strip("\"")
                singleData = "\"" + sentiment + "\",\""+ review + "\""
                g.write(singleData+'\n')
            singleData = line
        else:
            singleData += " "+line
    g.write(singleData)
    count += 1
    singleData = ""
g.close()
