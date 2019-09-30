import os
import platform
import requests
from bs4 import BeautifulSoup

class Monkey:
    def dance(self):
        print("Monkey dancing")

def main():
    print (os.name)
    print (platform.system())
    print (platform.release())
    print (platform.architecture())

    page = requests.get("http://google.dk")


    print (page.content)

    soup = BeautifulSoup(page.content, "html.parser")
    print (soup.find_all('a'))

if __name__ == "__main__": main()