import unittest
from EmailServerConfig import EmailServerConfig

'''
MISSING VALUES

1 - fromemail  - Email used to send from
2 - emailpass  - password of fromemail

Note: cmd + f any of the above and replace.

'''

class TestServer(unittest.TestCase):

    def test_Server(self):
        fromemail = 
        emailpass =
        newtest = EmailServerConfig(fromemail, emailpass)
        self.assertTrue(newtest)



if __name__ == "__main__":
    unittest.main()
