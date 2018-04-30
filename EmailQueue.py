import numpy as np

class EmailQueue(object):

    def __init__(self, *listobj):
        self.__list = []
        self.__queue = listobj

    def __iter__(self):
        for i in self.__list:
            yield i

    def __eq__(self, other):
        return self.__list == other

    def __str__(self):
        print 'List Contents are {}'.format(self.__list)

    def isEmpty(self):
        return self.__queue == []

    def isNone(self, value):
        return value == None

    def leftAppendtoQ(self, value):
        self.__queue.insert(0, value)

    def rightAppendtoQ(self,value):
        self.__list.append(value)

    def popQ(self):
        return self.__queue.pop()

    def genRandomInt(self):
        return np.random.randint(1000)

    def sortQueue(self):
        temp_ = [[self.genRandomInt(), i] for i in self.__queue]
        temp = self.extractNamesEmails(sorted(temp_)[::-1])
        return temp[0]

    def extractNamesEmails(self, obj):
        return [i[1] for i in obj]

    @property
    def classlist(self):
        return self.__list

    @property
    def classQueue(self):
        return self.__queue
