class Data(object):
    def getData(self):
        print('In data!')

class Time(Data):           #Inheriting from Data class
    def getTime(self):
        print('In Time!')

if __name__ == '__main__':
    data = Data()
    time = Time()
#inheritance methods
    data.getData()
    time.getTime()
    time.getData()      