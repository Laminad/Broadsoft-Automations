import random
import time

##########################################################################################################################
#                                                 codeGenerator                                                          #
#                                                                                                                        #
# codeGenerator is a class that generates ld codes of length 1 to 10 and outputs them in broadsoft oci xml format.       #  
#                                                                                                                        #
# If you find any bugs or have suggestions please email dan.thompson@voyant.com.                                         #
##########################################################################################################################

class codeGenerator:
    def __init__(self):
        self.codeArray = [ ]
        self.length = 15 
        self.amount = 0
        self.amountTest = False
        self.serviceProviderId = ""
        self.groupId = ""
        self.sessionId = ""

# getServiceProviderId gets the broadsoft service provider id from the user to output in oci xml format

    def getServiceProviderId(self): self.serviceProviderId = raw_input("Enter the Service Provider ID: ")
	
# getGroupID get the broadsoft group id from ther user to output in oci xml format.

    def getGroupId(self): self.groupId = raw_input("Enter the Group ID: ")
	
# codeTotal prints the code total by taking the length of the array.

    def codeTotal(self): print len(self.codeArray)

# getLength gets the length of number needed from the user and checks to makes sure the value makes sense.
	
    def getLength(self):
        while self.length > 14: 
            self.length = int(raw_input("Enter the Length of LD Codes Needed: "))
            if self.length > 14: print "This value is too large."
            elif self.length < 1: print "This value is too small."

# getAmount gets the amount of random numbers needed from the users and checks to make sure it makes sense

    def getAmount(self):
        while self.amountTest != True:
            self.amount = int(raw_input("Enter the Amount of LD Codes Needed: "))
            self.amountTest = self.maxCodes()
            if self.amount <= 0: print "This value is too small."
            elif self.amountTest == False: print "This value is too large."

# codeGenerator the fucntion generates the random numbers of requested amount and length.
# It uses the randint function from the random library to generate random numbers of a specific
# length in a while loop that ends when the requested amount is reached.

    def codeGenerator(self):
        amount = self.amount
        while amount != 0:
            if self.length == 1: self.codeArray.append(random.randint(1,9))
            elif self.length == 2: self.codeArray.append(random.randint(10, 99))
            elif self.length == 3: self.codeArray.append(random.randint(100, 999))
            elif self.length == 4: self.codeArray.append(random.randint(1000, 9999))
            elif self.length == 5: self.codeArray.append(random.randint(10000, 99999))
            elif self.length == 6: self.codeArray.append(random.randint(100000, 999999))
            elif self.length == 7: self.codeArray.append(random.randint(1000000, 9999999))
            elif self.length == 8: self.codeArray.append(random.randint(10000000, 99999999))
            elif self.length == 9: self.codeArray.append(random.randint(100000000, 999999999))
            elif self.length == 10: self.codeArray.append(random.randint(1000000000, 9999999999))
            elif self.length == 11: self.codeArray.append(random.randint(10000000000, 99999999999))
            elif self.length == 12: self.codeArray.append(random.randint(100000000000, 999999999999))
            elif self.length == 13: self.codeArray.append(random.randint(1000000000000, 9999999999999))
            elif self.length == 14: self.codeArray.append(random.randint(10000000000000, 99999999999999))
            amount -= 1

# maxCodes checks the maximum allowed amount for a specific length of random number. If the requested
# amount is larger than the length provided allows, it will return false. If everything checks out it
# returns true.

    def maxCodes(self):
        if self.length == 1 and self.amount > 9: return False
        elif self.length == 2 and self.amount > 89: return False
        elif self.length == 3 and self.amount > 899: return False
        elif self.length == 4 and self.amount > 8999: return False
        elif self.length == 5 and self.amount > 89999: return False
        elif self.length == 6 and self.amount > 899999: return False
        elif self.length == 7 and self.amount > 8999999: return False
        elif self.length == 8 and self.amount > 89999999: return False
        elif self.length == 9 and self.amount > 899999999: return False
        elif self.length == 10 and self.amount > 8999999999: return False
        elif self.length == 11 and self.amount > 89999999999: return False
        elif self.length == 12 and self.amount > 899999999999: return False
        elif self.length == 13 and self.amount > 8999999999999: return False
        elif self.length == 14 and self.amount > 89999999999999: return False
        return True

# writeCodes prints ld codes in OCI XML format.

    def writeCodes(self):
        amount = 0
        serviceProviderId = str(self.serviceProviderId)
        groupId = str(self.groupId)
        while amount != self.amount:
            LDcode = str(self.codeArray[amount])
            print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
            print '<BroadsoftDocument protocol="OCI" xmlns="C">'
            print '    <sessionId mlns="">dan</sessionId>'
            print '    <command xsi:type="GroupAccountAuthorizationCodesAddListRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            print '        <serviceProviderId>' + serviceProviderId + '</serviceProviderId>'
            print '        <groupId>' + groupId + '</groupId>'
            print '        <codeEntry>'
            print '            <code>' + LDcode + '</code>'
            print '            <description>Auth Code ' + LDcode + '</description>'
            print '        </codeEntry>'
            print '    </command>'
            print '</BroadsoftDocument>'
            print ''
            amount += 1

# delAll is the deconstructor.

    def delAll (self):
        del self.codeArray
        del self.length
        del self.amount
        del self.amountTest
        del self.serviceProviderId
        del self.groupId
        del self.sessionId
 
    def __main__(self):
        print "-"*20
        print " LD Code Generator "
        print "-"*20
        self.getServiceProviderId()
        self.getGroupId()
        self.getLength()
        self.getAmount()
        print "-"*20
        print "Generating Codes"
        print "-"*20
        self.codeGenerator()
        print "Writing Codes"
        print "-"*20
        self.writeCodes()
        print "Code Total"
        self.codeTotal()
        print "-"*20
        print "Clearing Data"
        print "-"*20
        self.delAll()
        
            
LD1 = codeGenerator()
LD1.__main__()