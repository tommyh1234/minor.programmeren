import pickle
import csv
import datetime
import os


class DataHelper(object):

    def __init__(self, fileToLoad=None):
        timestamp = str(datetime.datetime.utcnow())
        self.fileToLoad = fileToLoad
        self.starttime = timestamp
        if fileToLoad is None:
            os.makedirs('output/' + self.starttime)
            self.file = open('output/' + self.starttime +
                             '/' + timestamp + '.csv',
                             'w', newline='')
            self.writer = csv.writer(self.file)
            self.writer.writerow(['Houses', 'Price', 'Area'])

    def writeArea(self, area):
        if self.file is None:
            raise RuntimeError('Trying to write before opening a .csv file!')

        timestamp = str(datetime.datetime.utcnow())
        binaryFile = open('output/' + self.starttime + '/' +
                          timestamp + '.area', mode='wb')
        pickle.dump(area, binaryFile)
        binaryFile.close()

        self.writer.writerow([
                             len(area.allHousesList),
                             area.price,
                             timestamp + '.area'])

    def writeSeperator(self):
        if self.file is None:
            raise RuntimeError('Trying to write before opening a .csv file!')

        self.writer.writerow(['', '', ''])

    def getArea(self):
        if self.fileToLoad is None:
            raise RuntimeError('Tried to open a file without \
                               specifying one in my constructor!')
        binaryFile = open(self.fileToLoad, 'rb')
        area = pickle.load(binaryFile)
        binaryFile.close()
        return area
