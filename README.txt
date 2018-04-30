The files provided are scripts to automatically send emails to customers. It's
part of a recent project I was working on.

In the original project, the customer's emails and names are queried from a database.

However, in the scripts I've provided, they're parsed from a JSON file because I cant
provide the entity's DB.

I've written a 'Queue' class, which provides adequate functionality to python's standard Queue lib.

I've used the Queue class that I've written in the email automation script.

The files provided are:
 1 - EmailQueue: The Queue class I wrote as mentioned above
 2 - NewCustomerEmailSend.py : Contains the class and methods to execute sending the emails
 3 - emailTest.py : Test case for sending email
 4 - emailTestingfunctions.py : helper functions to enable email testing
 5 - EmailServerConfig.py : Contains the class necessary to connect to smtp server and enable email sending.
 6 - TestServer.py : Test case for EmailServerConfig.py
 7 - person.json: Template for JSON file to be used for parsing. I've included my personal info in this file.
     However, feel free to add as many contacts as you want, as long as it's the same format.

 Note: In this case, I've used the gmail server. Please use a gmail account or change the smtp to appropriate
 domain.

USAGE:

To test the email sending, Simply run 'NewCustomerEmailSend.py' from the command line or crontab, after
filling in the missing values, which are emails and paths. Instructions are in the file. 
