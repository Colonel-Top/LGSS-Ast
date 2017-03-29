# -*- coding: utf-8 -*-
import time
import random
import string
import gspread
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
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

bot_status = 0
bot_mode = 0
# define hi or hello
greeting_w = ['Hello', 'Hi ', 'Greeting', 'สวัสดี','hello', 'hi ', 'greetings', 'sup', 'whats up','re you here']
greeting_f = ['May i help you please ?', 'Yes ?', 'Ya Anything you want ?', 'Anything ? ya ?', 'Greeting yes ?','Always here']
backasgre_w = ['Thx','Thank','ขอบคุณ','appreciate','ขอบใจ']
backasgre_f = ['Your welcome','With Pleasure :)','with Appreciated','Ya','Okay ^^','Welcome','Never mind :)']
menu_cmd = ['pen menu','pen Menu','เปิดเมนู','เรียกเมนู','show function','Show function','Show Menu','show menu','Show menu']
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
        #message = message.decode("utf-8")
        print("%s said: %s" % (author_id, message))
        status = 0
        global bot_mode
        global bot_status
        # if you are not the author, echo
        if str(author_id) != str(self.uid):
            #self.send(author_id,message)
            #self.send(author_id, bot_mode)
            #self.send(author_id,bot_status)
            #self.send(author_id,status)
            #self.send(author_id,"-")
            if bot_mode == 1 and bot_status == 1 and status == 0:
                try:
                    gdate = message[0:10]
                    content = message[10:]
                    fo = open(gdate, "a")
                    fo.write(content+"\n")
                    fo.close()
                    self.send(author_id,'เพิ่มตารางงาน,นัดหมายเรียบร้อยค่ะ')
                except:
                    self.send(author_id,'การเพิ่มตารางเวลาล้มเหลว')
                bot_mode = 0
                bot_status = 0
                status = 1
            if bot_mode == 2 and bot_status == 1 and status == 0:
                try:
                    linetoremove = int(message[0])

                    self.send(author_id,linetoremove)
                    gdate = (now.strftime("%d-%m-%Y"))
                    self.send(author_id,gdate)
                    f = open(gdate,"r+")
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != linetoremove:
                            f.write(i)
                    f.truncate()
                    f.close()
                except Exception as e:
                    self.send(author_id, e)
                    self.send(author_id,'การลบตารางเวลาล้มเหลว')
                bot_mode = 0
                bot_status = 0
                status = 1
            if bot_status == 1 and status == 0:
                if 'a' in message:
                    bot_mode = 1
                    self.send(author_id,'a.เพิ่มงาน,ตารางเวลานัดหมายได้\nกรุณาใช้รูปแบบดังต่อไปนี้ 31-12-2017:เนื้อหางาน')
                    status = 1
                if 'A' in message:
                    bot_mode = 1
                    self.send(author_id,'a.เพิ่มงาน,ตารางเวลานัดหมายได้\nกรุณาใช้รูปแบบดังต่อไปนี้ 31-12-2017:เนื้อหางาน')
                    status = 1
                if 'b' in message:
                    try:
                        self.send(author_id,'รายการตารางงานและการนัดหมายวันนี้')
                        gdate = (now.strftime("%d-%m-%Y"))
                        self.send(author_id,gdate)
                        # Open a file
                        fo = open(gdate, "r+")
                        strws = fo.read()
                        self.send(author_id,strws)
                        # Close opend file
                        fo.close()
                    except:
                        self.send(author_id,'ไม่พบตารางเวลาหรือการอ่านล้มเหลว')
                    bot_status = 0
                    status = 1
                if 'B' in message:
                    try:
                        self.send(author_id,'รายการตารางงานและการนัดหมายวันนี้')
                        gdate = (now.strftime("%d-%m-%Y"))
                        self.send(author_id,gdate)
                        # Open a file
                        fo = open(gdate, "r+")
                        strws = fo.read()
                        self.send(author_id,strws)
                        # Close opend file
                        fo.close()
                    except:
                        self.send(author_id,'ไม่พบตารางเวลาหรือการอ่านล้มเหลว')
                    bot_status = 0
                    status = 1
                if 'c' in message:
                    try:
                        self.send(author_id,'รายการตารางงานและการนัดหมายวันนี้')
                        gdate = (now.strftime("%d-%m-%Y"))
                        self.send(author_id,gdate)
                        # Open a file
                        fo = open(gdate, "r+")
                        strws = fo.read()
                        self.send(author_id,strws)
                        # Close opend file
                        fo.close()
                        self.send(author_id,'กรุณาใส่เลขหัวข้องานที่ต้องการจะลยเช่น 3')
                    except:
                        self.send(author_id,'ไม่พบตารางเวลาหรือการอ่านล้มเหลว')
                    bot_mode = 2
                    bot_status = 1
                    status = 1
                if 'C' in message:
                    try:
                        self.send(author_id,'รายการตารางงานและการนัดหมายวันนี้')
                        gdate = (now.strftime("%d-%m-%Y"))
                        self.send(author_id,gdate)
                        # Open a file
                        fo = open(gdate, "r+")
                        strws = fo.read()
                        self.send(author_id,strws)
                        # Close opend file
                        fo.close()
                        self.send(author_id,'กรุณาใส่เลขหัวข้องานที่ต้องการจะลบเช่น 3')
                    except:
                        self.send(author_id,'ไม่พบตารางเวลาหรือการอ่านล้มเหลว')
                    bot_mode = 2
                    bot_status = 1
                    status = 1
            if status == 0:
                for tmp in tellasc_cmd:
                    if tmp in message:
                        going = tmp.replace('tell all associate','')
                        stringtosend = 'Message From Colonel : '
                        stringtosend += strs(going)
                        self.send(author_id,random.choice(tellasc_ans))
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
                for tmp in menu_cmd:
                    if tmp in message:
                        self.send(author_id,'กรุณาเลือกฟังก์ชัน');
                        self.send(author_id,'a.เพิ่มงาน,ตารางนัดหมาย\nb.ตรวจสอบตารางเวลางาน\nc.ลบตารางเวลานัดหมาย')
                        bot_status = 1
                        status = 1
            if status == 0:
                if 'Get Interest Now' in message:
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
