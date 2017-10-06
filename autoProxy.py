import os
import requests
from bs4 import BeautifulSoup
import urllib.request

try:
    from PIL import Image, ImageOps
except:
    import Image, ImageOps

def listParse():

    # set .txt file name to variable cubeFile that should be in the same dir, http://www.cubetutor.com is a good place
    # to download a the .txt list of ones cube to put in
    cubeTextFile = "yourFileName.txt"

    with open(cubeTextFile) as f:
        content = f.readlines()

    cardList = [x.strip() for x in content]


    for x in cardList:

        cardName = []
        cardName.extend(x.split())

        cardSearchUrl = "http://magiccards.info/query?q="

        for x in cardName:

            x = x + "+"

            cardSearchUrl += x


        cardSearchUrl += "&v=card&s=cname"

        cardTitle = ''.join(cardName)

        cardScrape(cardSearchUrl, cardTitle)




def cardScrape(cardSearchUrl, cardTitle):

    r = requests.get(cardSearchUrl)
    data = r.text

    soup = BeautifulSoup(data, "lxml")

    x = 0

    for link in soup.find_all('img'):
        image = link.get("src")

        if x == 1:
            print (cardTitle)
            image = "http://magiccards.info" + image
            urllib.request.urlretrieve(image, cardTitle + ".jpg")
            imageName = (cardTitle + ".jpg")
            borderExpand(imageName)

        x += 1



def borderExpand(imageName):

    img = Image.open(imageName)
    img_with_border = ImageOps.expand(img,border=30,fill='black')
    img_with_border.save(imageName)

def main():
    listParse()

if __name__ == "__main__": main()
