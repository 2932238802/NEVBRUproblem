
import csv

class ReadCsv:
    
    def __init__(self):
        self.__csv = []
        pass
    
    
    def readcsv(self,path):
        """
        阅读 csv 文件
        """
        
        with open(path,mode='r',encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            
            for row in csv_reader:
                year = int(row[0])
                num = float(row[1])
                self.__csv.append((year,num))
        
        
    
    def printcsv(self):
        """
        打印 csv文件
        """
        pass
    
    @property
    def get_csv(self)->list:
        return self.__csv
    
    