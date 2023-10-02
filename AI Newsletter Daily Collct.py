#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from imap_tools import MailBox, AND
from bs4 import BeautifulSoup

from datetime import datetime
from datetime import timezone, tzinfo

df = pd.read_csv('all_companies1.csv')

server = 'imap.gmail.com'
user = 'aicompanycollection@gmail.com'
password = 'cnagmsywemxwynaa'

last_updates = df.groupby(['Source']).max().date

links = []
titles = []
desc = []
dates = []
source = []

with MailBox(server).login(user, password) as mailbox:
    for msg in mailbox.fetch(criteria=AND(from_='hi@mail.theresanaiforthat.com')):
        if (msg.date > pd.to_datetime(last_updates["There's an AI for that"])):
            #print(msg.date, msg.subject, len(msg.text or msg.html))
            #print(msg.text)
            message = msg.html
            txt = msg.text
            soup = BeautifulSoup(message, 'html.parser')
            a = soup.find_all('li')



            for i in soup.find_all('li'):
                links.append(i.a['href'])
                titles.append(i.i.text)
                text = i.text.split('\n')
                desc.append(text[-1].strip()[2:])
                source.append("There's an AI for that")


                #print(text[-1].strip()[2:])
                dates.append(msg.date)
theresAn = pd.DataFrame({'Titles':titles, 'Links':links, 'Descriptions':desc, 'date':dates, 'Source':source})



links = []
titles = []
desc = []
dates = []
source = []

with MailBox(server).login(user, password) as mailbox:
    for msg in mailbox.fetch(criteria=AND(from_='theresanaiforthat@mail.beehiiv.com')):
        if (msg.date > pd.to_datetime(last_updates["There's an AI for that"])):
            #print(msg.date, msg.subject, len(msg.text or msg.html))
            #print(msg.text)
            message = msg.html
            txt = msg.text
            soup = BeautifulSoup(message, 'html.parser')
            a = soup.find_all('li')


            for i in soup.find_all('li'):
                links.append(i.a['href'])
                titles.append(i.i.text)
                text = i.text.split('\n')
                desc.append(text[-1].strip()[2:])
                source.append("There's an AI for that")

                print(text[-1].strip()[2:])
                dates.append(msg.date)
AIforthat = pd.DataFrame({'Titles':titles, 'Links':links, 'Descriptions':desc, 'date':dates, 'Source':source})



links = []
titles = []
desc = []
dates = []
source = []

with MailBox(server).login(user, password) as mailbox:
    for msg in mailbox.fetch(criteria=AND(from_ = 'superhuman@mail.joinsuperhuman.ai')):
        print(msg.date)
        if(msg.date > pd.to_datetime(last_updates['Superhuman'])):
            message = msg.html
            txt = msg.text
            #print(msg.uid)
            soup = BeautifulSoup(message, 'html.parser')
            a = soup.find_all('table')
            count=0
            for i in a: 
                if (i.text[:43] == '5 AI Tools to Supercharge Your Productivity'):
                    c = i.find_all('p')
                    cou = 0
                    for i in c: 
                        cou += 1
                        if (i.a != None):
                            if (cou != 5):
                                links.append(i.a['href'])
                                desc.append((i.find_all('span')[-1].text).strip(':'))
                                titles.append(i.find_all('span')[0].text)
                                dates.append(msg.date)
                                source.append('Superhuman')

                    #print(len(links))
                    #print(titles)
                    #print(desc)
                count+=1
            print('\n')
superhuman = pd.DataFrame({'Titles':titles, 'Links':links, 'Descriptions':desc, "date":dates, 'Source': source})
        


superhuman.to_csv('all_companies1.csv', index=False, mode= 'a', header = False)
theresAn.to_csv('all_companies1.csv', index=False, mode= 'a', header = False)
AIforthat.to_csv('all_companies1.csv', index=False, mode= 'a', header = False)

this = pd.read_csv('all_companies1.csv')
