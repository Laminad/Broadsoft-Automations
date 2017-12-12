import csv

class International:

    def __init__(self):
        self.userIDlist = ' '
        self.csvfile = ' '
        
    def importUserList(self): 
        self.csvfile = raw_input('Enter the User List CSV file: ')
        print ' '
      
    def welcome(self):
        print '#'*51
        print '#' + '                International Enable             ' + '#'
        print '#' + '  This is a Python class that will enable        ' + '#'
        print '#' + '  international calling in bulk from a User ID   ' + '#'
        print '#' + '  CSV. International Enable then outputs the OCI ' + '#'
        print '#' + '  XML to enable international calling for the    ' + '#'
        print '#' + '  user in the user list csv.                     ' + '#'
        print '#'*51
        print ' '
        
    def internationalOS(self):
        end = 0
        while end != 3:
            print '1. Enable International.'
            print '2. Disable International.'
            print '3. End Program.'
            print ' '
            end = int(raw_input('Enter a numeric value: '))
            if end == 1:
                self.importUserList()
                self.enableInternational()
            elif end == 2:
                self.importUserList()
                self.disableInternational()

    def enableInternational(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.userIDlist = csv.reader(csvfile, delimiter=" ", quotechar=" ")
            for rows in self.userIDlist:
                for users in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '    <sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="UserOutgoingCallingPlanOriginatingModifyRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <userId>' + users + '</userId>'
                    print "        <useCustomSettings>true</useCustomSettings>"
                    print '        <userPermissions>'
                    print '            <group>Allow</group>'
                    print '            <local>Allow</local>'
                    print '            <tollFree>Allow</tollFree>'
                    print '            <toll>Allow</toll>'
                    print '            <international>Allow</international>'
                    print '            <operatorAssisted>Allow</operatorAssisted>'
                    print '            <chargeableDirectoryAssisted>Allow</chargeableDirectoryAssisted>'
                    print '            <specialServicesI>Allow</specialServicesI>'
                    print '            <specialServicesII>Allow</specialServicesII>'
                    print '            <premiumServicesI>Disallow</premiumServicesI>'
                    print '            <premiumServicesII>Disallow</premiumServicesII>'
                    print '            <casual>Disallow</casual>'
                    print '            <urlDialing>Allow</urlDialing>'
                    print '            <unknown>Allow</unknown>'
                    print '        </userPermissions>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def disableInternational(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.userIDlist = csv.reader(csvfile, delimiter=" ", quotechar=" ")
            for rows in self.userIDlist:
                for users in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '    <sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="UserOutgoingCallingPlanOriginatingModifyRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <userId>' + users + '</userId>'
                    print "        <useCustomSettings>true</useCustomSettings>"
                    print '        <userPermissions>'
                    print '            <group>Allow</group>'
                    print '            <local>Allow</local>'
                    print '            <tollFree>Allow</tollFree>'
                    print '            <toll>Allow</toll>'
                    print '            <international>Disallow</international>'
                    print '            <operatorAssisted>Allow</operatorAssisted>'
                    print '            <chargeableDirectoryAssisted>Allow</chargeableDirectoryAssisted>'
                    print '            <specialServicesI>Allow</specialServicesI>'
                    print '            <specialServicesII>Allow</specialServicesII>'
                    print '            <premiumServicesI>Disallow</premiumServicesI>'
                    print '            <premiumServicesII>Disallow</premiumServicesII>'
                    print '            <casual>Disallow</casual>'
                    print '            <urlDialing>Allow</urlDialing>'
                    print '            <unknown>Allow</unknown>'
                    print '        </userPermissions>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def __del__(self):
        del self.userIDlist
        del self.csvfile
             
    def __main__(self):
        self.welcome()
        self.internationalOS()
        self.__del__()
        
int1 = International()
int1.__main__()