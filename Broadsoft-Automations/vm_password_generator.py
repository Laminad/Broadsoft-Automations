import random
import csv

class VMGenerator:
    
    def __init__(self):
        self.vmPass = []
        self.userIDlist = []
        self.userCSV = ' '
        self.outputCSV = ' '
        self.outputUserIDandPass = ' '
        
    def importUserCSV(self):
        file = ' '
        self.userCSV = raw_input('Please Enter the User ID CSV File: ')
        with open(self.userCSV, 'rb') as csvfile:
            file = csv.reader(csvfile, delimiter=' ', quotechar=' ')
            for rows in file:
                for user in rows:
                    self.userIDlist.append(user)
                
    def outputFile(self): 
        self.outputCSV = raw_input('Please Enter the CSV file to output the User ID Password pair to: ')
        print ' '
        
    def vmPasswordGenerator(self):
        for user in self.userIDlist:
            self.vmPass.append(str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
    
    def writeOCI(self):
        i = 0
        for user in self.userIDlist:
            print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
            print '<BroadsoftDocument protocol="OCI" xmlns="C">'
            print '    <sessionId xmlns="">dan</sessionId>'
            print '    <command xsi:type="UserPortalPasscodeModifyRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            print '        <userId>'+ user +'</userId>'
            print '        <newPasscode>'+ self.vmPass[i] +'</newPasscode>'
            print '    </command>'
            print '</BroadsoftDocument>'
            print ' '
            i += 1
    
    def writeOutput(self):
        i = 0                
        with open(self.outputCSV, 'wb') as outputfile:
            self.outputUserIDandPass = csv.writer(outputfile, delimiter = ' ', quotechar=' ')
            for user in self.userIDlist: 
                self.outputUserIDandPass.writerow(user + ',' + self.vmPass[i])
                i +=1
        
    def __del__(self):
        del self.vmPass
        del self.userIDlist
        del self.userCSV

    def __main__(self):
        self.importUserCSV()
        self.outputFile()
        self.vmPasswordGenerator()
        self.writeOCI()
        self.writeOutput()
        self.__del__()
        
vm1 = VMGenerator()
vm1.__main__()