# -*- coding: utf-8 -*-
import time
import random
import string
import gspread

from datetime import datetime

now = datetime.now()
from oauth2client.service_account import ServiceAccountCredentials
import fbchat

client = fbchat.Client("colonel-secretary@outlook.com", "skr010527")
colonelid = 100000325120614
sent = client.send(colonelid, "***********************")
sent = client.send(colonelid, "Messenger API Connected")
print ("Messenger API Connected")
scope = ['https://spreadsheets.google.com/feeds']
state = '0'
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
worksheet = sh.worksheet("Account")
sent = client.send(colonelid, "Google API Connected")
print ("Google API Connected")
sent = client.send(colonelid, 'Greeting Master')
# Login with your Google account

# define hi or hello
greeting_w = ['Hello', 'Hi ', 'Greeting', 'สวัสดี','hello', 'hi ', 'greetings', 'sup', 'whats up','re you here']
greeting_f = ['May i help you please ?', 'Yes ?', 'Ya Anything you want ?', 'Anything ? ya ?', 'Greeting yes ?','Always here']
backasgre_w = ['Thx','Thank','ขอบคุณ','appreciate','ขอบใจ']
backasgre_f = ['Your welcome','With Pleasure :)','with Appreciated','Ya','Okay ^^','Welcome','Never mind :)']

simq_ask = ['ho are you','hat do you do','ho is your boss','ho am i','ell me a joke','ell me some joke']
simq_ans = ['I am Chloe The Secretary of Colonel','I am Chloe The Secretary of Colonel ^^ Helping My Master & you guys','My Boss or my master is Colonel','Some Human in this world','Joke ? google it :)','Ahh Nope']

bank_ask = ['eport account','ccount report','om engr account','pdate account','heck amout account','heck amout in account']
bank_ans = ['Okay i will update account for you','Yes, wait a second','Let me check account','Here we go','Alright here is it','Ya this one ^^']

tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you','Yes, wait a second','Let me work on it','Here we go','Alright here is it','Ya this one ^^']
# Class def
class EchoBot(fbchat.Client):
    def __init__(self, email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)  # mark delivered
        self.markAsRead(author_id)  # mark read
        message = message.decode("utf-8")
        print("%s said: %s" % (author_id, message))
        status = 0
        # if you are not the author, echo
        if str(author_id) != str(self.uid):
            #self.send(author_id,message)
            if status == 0:
                for tmp in tellasc_cmd:
                    if tmp in message:
                        going = tmp.replace('tell all associate','')
                        stringtosend = "Message From Colonel : "
                        stringtosend += str(going)
                        self.send(author_id,random.choice(tellasc_ans));
                        #self.send(100002210119100,"Message From Colonel : " + going) #Aomsin
                        #self.send(100001717587402,"Message From Colonel : " + going) #Beer
                        #self.send(100000337186822,"Message From Colonel : " + going) #Pond
                        self.send(colonelid,stringtosend) #me
                        status = 1
            if status == 0:
                for tmp in greeting_w:
                    if tmp in message:
                        self.send(author_id,random.choice(greeting_f));
                        status = 1
            if status == 0:
                if "Get Interest Now" in message:
                    self.send(author_id,random.choice(bank_ans));
                    sent = client.send(colonelid, "AI has Awaken and Collecting Interest")
                    print("AI has Awaken and Collecting Interest")
                    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
                    gc = gspread.authorize(credentials)
                    sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
                    worksheet = sh.worksheet("Account")
                    cell = worksheet.acell('U31').value
                    cell = cell.encode("utf-8")
                    monthcell = now.month
                    monthcell += 9
                    #onthcell += 10
                    for row in range(2, 31):  # Must be 31 in col or last parameter
                        peruser = 0
                        for col in range(8, 20):
                            tmp = worksheet.cell(row, col).value
                            print(tmp)
                            if (tmp == '0'):
                                peruser += 1
                        # print("Done Per loop")
                        # print (peruser)
                        if peruser >= 2 and worksheet.cell(row, monthcell).value == '':
                            interest = int(worksheet.cell(row, 22).value)
                            interest += 1
                            # print (interest)
                            worksheet.update_cell(row, 22, interest)
                        if worksheet.cell(row, monthcell).value == '':
                            worksheet.update_cell(row, monthcell, 0)
                        if row == 8:
                            print("Skip Safe")
                            continue
                    status = 1
            if status == 0:
                for tmp in backasgre_w:
                    if tmp in message:
                        self.send(author_id,random.choice(backasgre_f));
                        status = 1
            if status == 0:
                for tmp in simq_ask:
                    if tmp in message:
                        position = simq_ask.index(tmp)
                        self.send(author_id,simq_ans[position]);
                        status = 1
            if status == 0:
                for tmp in bank_ask:
                    if tmp in message:
                        self.send(author_id,random.choice(bank_ans));
                        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
                        gc = gspread.authorize(credentials)
                        sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
                        worksheet = sh.worksheet("Account")
                        cell = worksheet.acell('U31').value
                        sendstr = "Current Amount in Account : "
                        sendstr = sendstr+ str(cell)
                        self.send(author_id,sendstr)
                        status = 1

            if status == 0:
                self.send(author_id,"Sorry I don't know that");


bot = EchoBot("colonel-secretary@outlook.com", "skr010527")
while (True):
    # print('loop begin')
    now = datetime.now()
    # statuschk = ''
    if now.date == 16 and now.hour == 0 and now.minute == 0 and (now.second >= 1 or now.second <= 2):  # Get Interest
        # if(1):
        sent = client.send(colonelid, "AI has Awaken and Collecting Interest")
        print("AI has Awaken and Collecting Interest")
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
        worksheet = sh.worksheet("Account")
        cell = worksheet.acell('U31').value
        cell = cell.encode("utf-8")
        monthcell = now.month
        monthcell += 9
        # monthcell += 10
        for row in range(2, 31):  # Must be 31 in col or last parameter
            peruser = 0
            for col in range(8, 20):
                tmp = worksheet.cell(row, col).value
                print(tmp)
                if (tmp == '0'):
                    peruser += 1
            # print("Done Per loop")
            # print (peruser)
            if peruser >= 2 and worksheet.cell(row, monthcell).value == '':
                interest = int(worksheet.cell(row, 22).value)
                interest += 1
                # print (interest)
                worksheet.update_cell(row, 22, interest)
            if worksheet.cell(row, monthcell).value == '':
                worksheet.update_cell(row, monthcell, 0)
            if row == 8:
                print("Skip Safe")
                continue
    else:
        bot.listen()
