### pastebin Scraper by metriics ###
# this just gets the 8 most recent pastes
# only 8 since it uses the Public Pastes list on the right side of the page
# if you try using pastebin.com/archive to get more recent pastes, your ip can get banned
# (i know from experience! Note: it only bans you ip from the archive page. You can still use pastebin as normal.)


from bs4 import BeautifulSoup
from selenium import webdriver
#import pandas as pd  # for exporting data to csv later on maybe
from time import sleep

class Paste:
    def __init__(self, li):
        self.li = li
        self.name = ""
        self.link = ""
        self.time = ""
        self.syntax = ""
        self.body = "" # unused for now, can possible get later by getting page source from link ad getting string from Raw Data object on page

    def __str__(self):
        string = "Name: " + self.name + "\n" + "Link: " + self.link + "\n" + "Syntax: " + self.syntax + "\n" + "Time: " + self.time + "\n"
        return string
    
    def autoSet(self):
        self.name = self.li.a.string
        self.link = "pastebin.com" + self.li.a['href']
        if str.split(self.li.span.string)[1] == '|':
            self.syntax = str.split(self.li.span.string)[0]
            self.time = str.split(self.li.span.string)[2] + " " + str.split(self.li.span.string)[3] + " " + str.split(self.li.span.string)[4]
        else:
            self.syntax = "Unknown"
            self.time = self.li.span.string


driver = webdriver.Chrome("C:/Windows/chromedriver.exe") # start browser
driver.get('https://pastebin.com')  # get page

### this is a disgusting workaround the the "Checking your browser..." cloudflare page. If we don't do this we can't get the list.
print("got page, sleeping...")
sleep(5)                            # this is dangerous because its possible that cloudflare browser check takes longer than 5 seconds. 
driver.get('https://pastebin.com')  # get page again after cloudflare redirect (we have no cookie storage for now so we need to do this)
print("got page.")
###

content = driver.page_source # page source
soup = BeautifulSoup(content) # beautify source

pastes = []

table = soup.find('ul', attrs={'class':'right_menu'}) # find table, this is the Public Pastes table you see on the right side of the page
table = table.findAll('li') # get items in table. These are the individual list items. 

listLen = table.__len__() # get number of items in table

for i in range(0, listLen): # create list of Paste objects
    temp = Paste(table[i])
    temp.autoSet()
    pastes.append(temp)

for Paste in pastes: # print all Paste objects
    print(Paste)
    uIn = input()
    if uIn != "":
        break


input() # wait for user input before quitting

driver.quit()
driver.stop_client()
exit()