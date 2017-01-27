# -*- coding: utf-8 -*-
import sys,traceback
import time
import gspread
from datetime import datetime
now = datetime.now()
from line import LineClient, LineGroup, LineContact
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
state = '0'
GROUPNAME = 'ภาคีผู้นำคอมพิวเตอร์'
GROUPNAME = GROUPNAME.encode("utf-8")
GROUPNAME2 = 'คณะตลก CN15'
GROUPNAME2 = GROUPNAME2.encode("utf-8")
GROUPNAME3 = 'test'
GROUPNAME3 = GROUPNAME3.encode("utf-8")
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
worksheet = sh.worksheet("Account")
cell = worksheet.acell('U31').value
cell = cell.encode("utf-8")
cella = worksheet.acell('W1').value
cella = cella.encode("utf-8")
value_list = worksheet.col_values(21)
value_list_comp = worksheet.col_values(21)
print 'Connected\n'
# Login with your Google account
def sendlinenotiall():
    try:
        stringtosend = ""
        client = LineClient("anon-col@outlook.com", "Skr010527")
        client_group = client.getGroupByName(GROUPNAME3)
        cell = worksheet.acell('U31').value
        cell = cell.encode("utf-8")
        stringtosend += "*** ระบบบัญชีอัตโนมัติ ***\n\n"
        stringtosend += "รายชื่อที่ค้างชำระ 3 เดือน :\n"
        for num in range (2,30):
            ispaid = 0
            name = worksheet.cell(num,7).value
            if num == 8:
                continue
            name = name.encode("utf-8")
            for num2 in range (7,20):
                val = worksheet.cell(num, num2).value
                if val == '0':
                    ispaid = ispaid+1
            if ispaid >= 3 :
                stringtosend += ("- ")
                stringtosend += str(name)
                stringtosend += (" ")
                stringtosend += ispaid
                stringtosend += ("เดือน")
                stringtosend += "\n"
                varia = int(worksheet.cell(num,22).value)
                varia = ispaid-varia
                variatoup =  int(worksheet.cell(num,22).value)
                variatoup += varia
                worksheet.update_cell(num, 22, variatoup)
        stringtosend += "\nดอกเบี้ย 5% ได้ถูกบวกเข้าจำนวนกรุณาชำระให้ครบถ้วน"
        client_group.sendMessage (stringtosend)
        client_group.sendMessage ('สรุปยอดประจำวันนี้ : %s บาท' % cell)
            #client = LineClient(authToken="AUTHTOKEN")
        print "Done"
    except:
        print "Login Failed"
        print "Exception in user code:"
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
def sendlinenotistaff(stringup):
    try:
        state = 0
        client = LineClient("anon-col@outlook.com", "Skr010527")
        client_group = client.getGroupByName(GROUPNAME3)
        cell = worksheet.acell('U31').value
        cell = cell.encode("utf-8")
        client_group.sendMessage (stringup)
        client_group.sendMessage ('สรุปยอดประจำวันนี้ : %s บาท' % cell)
            #client = LineClient(authToken="AUTHTOKEN")
        print "Done"
    except:
        print "Login Failed"
        print "Exception in user code:"
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
#Login


while(True):
    now = datetime.now()
    reportstring = ''
    statuschk = ''
    cella = worksheet.acell('W1').value
    cella = cella.encode("utf-8")
    if now.hour %2 == 0 and now.minute == 59 and (now.second == 00 or now.second == 1) and state == '0':
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_code.json', scope)
        gc = gspread.authorize(credentials)
        sh = gc.open_by_key('1m0OUgl7O3lXEGV6XOa_I-kUJmxBTx6yZP5VrERjQWOM')
        worksheet = sh.worksheet("Account")
        cell = worksheet.acell('U31').value
        cell = cell.encode("utf-8")
        state = '1'
        if now.date == 14 and (now.second >= 00 or now.second <= 1) and now.hour == 23 and now.minute == 59:
            state = '2'
    #time.sleep(1)
    value_list_comp = worksheet.col_values(21)
    #time.sleep(1)
    #for a in range (1,30):
    #    print value_list[a]

    #for a in range (1,30):
    #    print value_list_comp[a]
    #print '*******************'
    for i in range (0,30):
        if value_list[i] != value_list_comp[i]:
            state = '1'
            tmp = worksheet.cell(i+1,7).value
            tmp = tmp.encode("utf-8")
            reportstring += "ชื่อ: "
            reportstring += tmp
            reportstring += " "
            reportstring += value_list[i]
            reportstring += " => "
            reportstring += value_list_comp[i]
            reportstring += ("\n")
            #print (reportstring)
            value_list[i] = value_list_comp[i]

    if cella == '1':
        print 'Status need Update'
        state = '1'
    if cella == '2':
        print 'Status need Update'
        state = '2'
    print state
    #print (now.date)
    if state == '1' and (now.second >= 30 or now.second <= 31) :
        print 'Sending Update(1)\n'
        #print now.second
        tmpstr = '***รายงานบัญชีอัพเดต***\n'
        tmpstr += reportstring
        worksheet.update_acell('W1', '0')
        #print tmpstr
        sendlinenotistaff(tmpstr)
        state = '0'
    if state == '2':
        print 'Sending Update(2)\n'
        sendlinenotiall()
        state = '0'
        worksheet.update_acell('W1', '0')

"""
try:
        client = LineClient("anon-col@outlook.com", "Skr010527")
        client_group = client.getGroupByName(GROUPNAME3)
        print ("Logged in")
        while(1):
            client.updateAuthToken()
            time.sleep(7)
            print ("Check\n")
            #recent_group_msg = client_group.getRecentMessages(count=10)
            op_list = []
            for op in client.longPoll():
                op_list.append(op)
            for op in op_list:
                sender   = op[0]
                receiver = op[1]
                message  = op[2]
                msg = message.text
                sendto = str(check_for_greeting(msg))
                if word in sendto:
                    client_group.sendMessage(sendto)
except:
    print "Login Failed"
    print "Exception in user code:"
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60

try:
        stringtosend = ""
        client = LineClient("anon-col@outlook.com", "Skr010527")
        client_group = client.getGroupByName(GROUPNAME)
        cell = worksheet.acell('U31').value
        cell = cell.encode("utf-8")
        client_group.sendMessage ('สรุปยอดประจำวันนี้ : %s' % cell)
        stringtosend += "รหัสชื่อที่ค้างชำระ 3 เดือน :\n"
        for num in range (2,29):
            ispaid = 0
            name = worksheet.cell(num,7).value
            name = name.encode("utf-8")
            for num2 in range (7,20):
                val = worksheet.cell(num, num2).value
                if ispaid == 3:
                    stringtosend += str(name)
                    stringtosend += "\n"
                    break
                elif val == '0':
                    ispaid = ispaid+1
        stringtosend += "ดอกเบี้ย 5% ได้ถูกบวกเข้าจำนวนกรุณาชำระให้ครบถ้วน\n"
        client_group.sendMessage (stringtosend)
        while
            #client = LineClient(authToken="AUTHTOKEN")
        print "Done"
except:
    print "Login Failed"

for num in range (2,29):
    ispaid = 0
    name = worksheet.cell(num,7).value
    name = worksheet.cell(num,2).value
    name = name.encode("utf-8")
    for num2 in range (8,20):
        val = worksheet.cell(num, num2).value
        if ispaid == 3:
            print('%s ค้าง 3 เดือน\n' % name)
            break
        elif val == '0':
            ispaid = ispaid+1
    #client = LineClient(authToken="AUTHTOKEN")
print('สรุปยอดประจำเดือนนี้ : %s' % cell)
    print "Login Failed"
"""
