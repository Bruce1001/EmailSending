import smtplib
import imaplib
import time
import numpy as np
from NewCustomerEmailSend import NewCustomerEmailSend

'''
MISSING VALUES

1 - fromaddr  - Email used to send from
2 - toaddr    - Email to send to
3 - password  - password of fromaddr
Note: cmd + f any of the above and replace.

'''

def emailSendMain(randomNumber):
    result = NewCustomerEmailSend.TestMain(randomNumber)
    return result


def SendEmail(randomNumber):
    fromaddr, password, toaddr = emailinfo()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    msg = randomNumber
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    return True

def emailinfo():
    fromaddr =
    toaddr =
    password = 
    return fromaddr, password, toaddr

def checkEmail(fromaddr, password, toaddr, randomNumber):

    time.sleep(5)
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(fromaddr, password)
    M.select("INBOX")
    typ, data = M.search(None, 'BODY', randomNumber)
    typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
    M.close()
    M.logout()
    return msg[0][1]
