import csv

class TagModify:
    
    def __init__(self):
        self.maclist = ' '
        self.csvfile = ' '
        self.serviceProviderId = ' '
        self.groupId = ' '
        self.proxy = ' '
        
    def welcome(self):
        print '#'*53
        print '#' + '                   Tag Modify                      ' + '#'
        print '#' + '  This is a python class that will remove and      ' + '#'
        print '#' + '  add Proxy, BLF, and Call Center Tags in bulk.    ' + '#'
        print '#' + '  This class takes in a Service Provider ID,       ' + '#'
        print '#' + '  Group ID, MAC Address CSV, and Proxy Address.    ' + '#'
        print '#' + '  Tag Modify then outputs the OCI XML to modify    ' + '#'
        print '#' + '  the tags for the phones in the MAC Address CSV.  ' + '#'
        print '#'*53
        print ' '
        
    def getIds(self):
        self.serviceProviderId = raw_input("Please enter the service provider ID: ")
        self.groupId = raw_input("Please enter the group ID: ")
        
    def getProxy(self): self.proxy = raw_input("Please enter the proxy address: ")
    
    def importMAClist(self): self.csvfile = raw_input('Input the MAC address CSV file: ')
        
    def removeProxyTags(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.maclist = csv.reader(csvfile, delimiter = ' ', quotechar = ' ')
            for rows in self.maclist:
                for mac in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '    <sessionId xmlns="">dan</sessionId>'
                    print '        <command xsi:type="GroupAccessDeviceCustomTagDeleteListRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '            <serviceProviderId>'+ self.serviceProviderId + '</serviceProviderId>'
                    print '            <groupId>'+ self.groupId + '</groupId>'
                    print '            <deviceName>' + mac + '</deviceName>'
                    print '            <tagName>%voIpProt.server.1.address%</tagName>'
                    print '            <tagName>%voIpProt.SIP.outboundProxy.address%</tagName>'
                    print '            <tagName>%reg.1.server.1.address%</tagName>'
                    print '            <tagName>%reg.1.outboundProxy.address%</tagName>'
                    print '        </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def addProxyTags(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.maclist = csv.reader(csvfile, delimiter = ' ', quotechar = ' ')
            for rows in self.maclist:
                for mac in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%reg.1.outboundProxy.address%</tagName>'
                    print '        <tagValue>' + self.proxy + '</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%reg.1.server.1.address%</tagName>'
                    print '        <tagValue>' + self.proxy + '</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%voIpProt.server.1.address%</tagName>'
                    print '        <tagValue>' + self.proxy + '</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%voIpProt.SIP.outboundProxy.address%</tagName>'
                    print '        <tagValue>' + self.proxy + '</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def removeBLFTags(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.maclist = csv.reader(csvfile, delimiter = ' ', quotechar = ' ')
            for rows in self.maclist:
                for mac in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '    <sessionId xmlns="">dan</sessionId>'
                    print '        <command xsi:type="GroupAccessDeviceCustomTagDeleteListRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '            <serviceProviderId>'+ self.serviceProviderId + '</serviceProviderId>'
                    print '            <groupId>'+ self.groupId + '</groupId>'
                    print '            <deviceName>' + mac + '</deviceName>'
                    print '            <tagName>%blf-DOMAIN-1%</tagName>'
                    print '            <tagName>%voIpProt.SIP.outboundProxy.transport%</tagName>'
                    print '            <tagName>%reg.1.outboundProxy.transport%</tagName>'
                    print '            <tagName>%reg.1.server.1.transport%</tagName>'
                    print '            <tagName>%voIpProt.server.1.transport%</tagName>'
                    print '        </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def addBLFTags(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.maclist = csv.reader(csvfile, delimiter = ' ', quotechar = ' ')
            for rows in self.maclist:
                for mac in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%blf-DOMAIN-1%</tagName>'
                    print '        <tagValue>' + '@' + self.proxy + '</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%voIpProt.SIP.outboundProxy.transport%</tagName>'
                    print '        <tagValue>TCPpreferred</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%reg.1.outboundProxy.transport%</tagName>'
                    print '        <tagValue>TCPpreferred</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%reg.1.server.1.transport%</tagName>'
                    print '        <tagValue>TCPpreferred</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%voIpProt.server.1.transport%</tagName>'
                    print '        <tagValue>TCPpreferred</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def removeCCTags(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.maclist = csv.reader(csvfile, delimiter = ' ', quotechar = ' ')
            for rows in self.maclist:
                for mac in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '    <sessionId xmlns="">dan</sessionId>'
                    print '        <command xsi:type="GroupAccessDeviceCustomTagDeleteListRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '            <serviceProviderId>'+ self.serviceProviderId + '</serviceProviderId>'
                    print '            <groupId>'+ self.groupId + '</groupId>'
                    print '            <deviceName>' + mac + '</deviceName>'
                    print '            <tagName>%feature.acdAgentAvailability.enabled%</tagName>'
                    print '            <tagName>%feature.acdLoginLogout.enabled%</tagName>'
                    print '            <tagName>%voIpProt.SIP.acd.signalingMethod%</tagName>'
                    print '            <tagName>%feature.callCenterStatus.enabled%</tagName>'
                    print '        </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def addCCTags(self):
        with open(self.csvfile, 'rb') as csvfile:
            self.maclist = csv.reader(csvfile, delimiter = ' ', quotechar = ' ')
            for rows in self.maclist:
                for mac in rows:
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%feature.acdAgentAvailability.enabled%</tagName>'
                    print '        <tagValue>1</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%feature.acdLoginLogout.enabled%</tagName>'
                    print '        <tagValue>1</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%voIpProt.SIP.acd.signalingMethod%</tagName>'
                    print '        <tagValue>1</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    print '        <?xml version="1.0" encoding="ISO-8859-1"?>'
                    print '<BroadsoftDocument protocol="OCI" xmlns="C">'
                    print '<sessionId xmlns="">dan</sessionId>'
                    print '    <command xsi:type="GroupAccessDeviceCustomTagAddRequest" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                    print '        <serviceProviderId>' + self.serviceProviderId + '</serviceProviderId>'
                    print '        <groupId>'+ self.groupId + '</groupId>'
                    print '        <deviceName>' + mac + '</deviceName>'
                    print '        <tagName>%feature.callCenterStatus.enabled%</tagName>'
                    print '        <tagValue>1</tagValue>'
                    print '    </command>'
                    print '</BroadsoftDocument>'
                    print ' '
                    
    def modifyOS(self):
        end = 0
        while end != 7:
            print '1. Remove Proxy Tags.'
            print '2. Add Proxy Tags.'
            print '3. Remove BLF Tags.'
            print '4. Add BLF Tags.'
            print '5. Remove Call Center Tags'
            print '6. Add Call Center Tags.'
            print '7. End Program.'
            print ' '
            end = int(raw_input("Enter the Tag modification type: "))
            if end == 1:
                self.getIds()
                self.importMAClist()
                print ' '
                self.removeProxyTags()
            elif end == 2:
                self.getIds()
                self.importMAClist()
                self.getProxy()
                print ' '
                self.addProxyTags()
            elif end == 3:
                self.getIds()
                self.importMAClist()
                print ' '
                self.removeBLFTags()
            elif end == 4:
                self.getIds()
                self.importMAClist()
                self.getProxy()
                print ' '
                self.addBLFTags()
            elif end == 5:
                self.getIds()
                self.importMAClist()
                print ' '
                self.removeCCTags()
            elif end == 6:
                self.getIds()
                self.importMAClist()
                print ' '
                self.addCCTags()
            
    def __del__(self):
        del self.maclist
        del self.csvfile
        del self.serviceProviderId
        del self.groupId
        del self.proxy
        
    def __main__(self):
        self.welcome()
        self.modifyOS()
        self.__del__()
        
tag1 = TagModify()
tag1.__main__()