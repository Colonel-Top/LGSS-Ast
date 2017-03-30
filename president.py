# -*- coding: utf-8 -*-
import time
import random
import string
import gspread
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from datetime import datetime


now = datetime.now()


from oauth2client.service_account import ServiceAccountCredentials
import fbchat

client = fbchat.Client("colonel-secretary@outlook.com", "skr010527")
#chloeclient = fbchat.Client("colonel-secretary@outlook.com", "skr010527")
colonelid = 100000325120614
#sent = client.send(colonelid, "***********************")
#sent = client.send(colonelid, "Messenger API Connected")
#print ("Messenger API Connected")

#print ("Google API Connected")
sent = client.send(colonelid, 'Your Auto Pilot System is Online now')
# Login with your Google account
import os.path
bot_status = 0
bot_mode = 0
# define hi or hello
greet = ['ประธาน','Colonel','colonel','Top','top','ท๊อป','ท็อป','ทอป','ท้อป','ประทาน','ปธ']
president_state = 0
#execfile("timeahead.py")
tellasc_cmd = ['tell all associate']
tellasc_ans = ['Okay i will update send msg for you','Yes, wait a second','Let me work on it','Here we go','Alright here is it','Ya this one ^^']
# Class def
class EchoBot(fbchat.Client):
    def __init__(self, email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self, email, password, debug, user_agent)
    def on_message(self, mid, author_id, author_name, message, metadata):
        #message = message.encode("utf-8")
        print("%s said: %s" % (author_id, message))
        status = 0
        global president_state
        global bot_mode
        global bot_status
        # if you are not the author, echo
        if str(author_id) != str(self.uid):
        #if(1):
            if status == 0 and president_state == 1: 
                for tmp in greet:
                    if tmp in message:
                        if(os.path.exists(author_id)):
                            print "already called"
                        else:
                            id = ""
                            state_reply = 0
                            self.send(author_id,'ขณะนี้ประธานไม่อยูกรุณาติดต่อในภายหลัง กรุณาทิ้งข้อความไว้ได้เลย\nหากต้องการนัดหมายคุณสามารถนัดผ่านเลขาโคลอี้ได้โดยไม่ต้องรอ ตามนี้เลย !');
                            self.send(author_id,'https://www.facebook.com/messages/t/chloe.aiprincess/');
                            self.markAsDelivered(author_id, mid)  # mark delivered
                            self.markAsRead(author_id)  # mark read
                            try:
                                id = author_id
                                fo = open(id,"a")
                                fo.write("1")
                                fo.close()
                                fo = open(checkid,"a")
                                fo.write(id+'\n')
                                fo.close()
                            except Exception as e:
                                sent = client.send(colonelid,"Debug::Self Contact Exception!")
                                sent = client.send(colonelid, e)
                        status = 1

        else:
            try:
                self.markAsDelivered(author_id, mid)  # mark delivered
                self.markAsRead(self.uid)  # mark read
                global president_state
                if 'uto pilot' in message:
                    president_state = 1
                    sent = client.send(colonelid, 'Your Auto Pilot System Active Now ['+str(president_state)+']')
                if 'top pilot' in message:
                    president_state = 0
                    sent = client.send(colonelid, 'Your Auto Pilot System is Stop & Standby Now ['+str(president_state)+']')
                    f = open(input_file)
                    for line in f:
                        try:
                            os.remove(line)
                        except Exception as e:
                            sent = client.send(colonelid,"Debug::Self Contact Exception!")
                    f.close()
                if 'Show Pilot State' in message:
                    if president_state == 1:
                        sent = client.send(colonelid, 'Your Auto Pilot System Active Now ['+str(president_state)+']')
                    elif president_state == 0:
                        sent = client.send(colonelid, 'Your Auto Pilot System is Stop & Standby Now ['+str(president_state)+']')
            except Exception as e:
                    sent = client.send(colonelid,"Debug::Self Contact Exception!")
                    sent = client.send(colonelid, e)
                


bot = EchoBot("promsurinm@hotmail.com", "%(!)^!##!#")
while (True):
        bot.listen()
