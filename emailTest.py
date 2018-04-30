import unittest
from emailTestingfunctions import emailSendMain, checkEmail, emailinfo
import numpy as np

'''
In this test case, I will generate a random number and send it as an email
then, login to that email and check if that particular email has really recieved
that random int in an email.

just for the record, fromaddr and toaddr can be the same. 
'''

class TestEmailSending(unittest.TestCase):

    def test_emailSending(self):
        randomNumber = str(np.random.randint(1,100,10))
        fromaddr, password, toaddr = emailinfo()
        result = emailSendMain(randomNumber)
        if result:
            resulttwo = checkEmail(fromaddr, password, toaddr, randomNumber)
        else:
            resulttwo = None

        self.assertIn(randomNumber, resulttwo)


if __name__ == "__main__":
    unittest.main()
