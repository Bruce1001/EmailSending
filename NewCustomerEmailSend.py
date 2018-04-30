import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import json
from EmailServerConfig import EmailServerConfig
from EmailQueue import EmailQueue as Eq

'''
MISSING VALUES:
 1 - self.__adminADDR   -   The email sending from
 2 - self.__adminPASS   -   The password of self.__adminADDR
 3 - imgfile            -   The path of the image that will be embedded into Email
 4 - jsonPath           -   The path of the json file that has the names and emails

 Note: cmd + f any of the above and replace.
'''


class NewCustomerEmailSend(EmailServerConfig):

    def __init__(self, contact):
        self.newCustomerEmail = contact[0]
        self.newCustomerName = contact[1]
        self.__adminADDR =
        self.__adminPASS = 
        self.newMessage = self.initMessage()
        super(NewCustomerEmailSend, self).__init__(self.__adminADDR, self.__adminPASS)

    @property
    def CustomerEmail(self):
        return self.newCustomerEmail

    @property
    def CustomerName(self):
        return self.newCustomerName

    @property
    def adminEmail(self):
        return self.__adminADDR

    def __eq__(self, other):
        return other == None

    def initMessage(self):
        newMessage = MIMEMultipart()
        newMessage['From'] = self.__adminADDR
        newMessage['Subject'] = 'A new customer message'
        return newMessage

    @staticmethod
    def embeddNameIntoHTML(name):
        html = """\
        <h1> """ + str(name) + """ Hello World</h1>
        <p>Hello World (again)</p>``
                <img src="cid:image1">
            </p>
        """
        msghtml = MIMEText(html, 'html')
        return msghtml

    @staticmethod
    def getImage(message):
        imgfile =
        img = open(imgfile, 'rb').read()
        msgImg = MIMEImage(img, 'jpeg')
        msgImg.add_header('Content-ID', '<image1>')
        msgImg.add_header('Conctent-Disposition', 'inline filename = {}'.format(imgfile))
        message.attach(msgImg)
        return message

    @staticmethod
    def getNamesEmails():
        emaillist = Eq()
        nameslist = Eq()
        try:
            jsonPath =
            with open(jsonPath, 'r') as fil:
                decoded = json.load(fil)
                for x in decoded['persons']:
                    emaillist.rightAppendtoQ(str(x['email']))
                    nameslist.rightAppendtoQ(str(x['name']))
                zipped = zip(emaillist, nameslist)
                return zipped
        except ValueError as VE:
            print "Couldn't open the json emails", VE

    @classmethod
    def Main(cls):
        contacts = NewCustomerEmailSend.getNamesEmails()
        contactList = Eq(contacts)
        namesEmails = contactList.sortQueue()
        for contact in namesEmails:
            newCustomer = cls(contact)
            msgHTML = cls.embeddNameIntoHTML(newCustomer.newCustomerName)
            msgImg = cls.getImage(newCustomer.newMessage)
            msgImg.attach(msgHTML)
            text = newCustomer.newMessage.as_string()
            newCustomer.server.sendmail(newCustomer.__adminADDR,newCustomer.newCustomerEmail, text)

    @staticmethod
    def TestMain(randomNumber):
        contacts = NewCustomerEmailSend.getNamesEmails()
        contactList = Eq(contacts)
        namesEmails = contactList.sortQueue()
        for contact in namesEmails:
            newCustomer = NewCustomerEmailSend(contact)
            msg = randomNumber
            newCustomer.server.sendmail(newCustomer.__adminADDR,
            newCustomer.newCustomerEmail, msg)
        return True



if __name__ == "__main__":
    NewCustomerEmailSend.Main()
