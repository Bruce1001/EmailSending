import smtplib

class EmailServerConfig(object):

    def __init__(self, adminEmail, adminPassword):
        self.__adminEmail = adminEmail
        self.__adminPassword = adminPassword
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.startserver()

    def startserver(self):
        if self.serverAuthentication():
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.__adminEmail, self.__adminPassword)
        else:
            self.server.quit()

    def serverAuthentication(self):
        self.server.set_debuglevel(True)
        self.server.ehlo()
        if self.server.has_extn('STARTTLS'):
            return True

        else:
            return False
