import random
import time
import re

def find(pat, text):
    match = re.search(pat,text)
    if match: return True
    
class passGenerator:
    def __init__(self):
        self.length = 0
        self.amount = 0
        self.passCheck = False
        self.password = ""
        self.passwordArray = []
        self.dictionary = {
            1: "a", 2: "A", 3: "b", 4: "B", 5: "c", 6: "C", 7: "d", 8: "D",
            9: "e", 10: "E", 11: "f", 12: "F", 13: "g", 14: "G", 15: "h",
            16: "H", 17: "i", 18: "I", 19: "j", 20: "J", 21: "k", 22: "K",
            23: "l", 24: "L", 25: "m", 26: "M", 27: "n", 28: "N", 29: "o",
            30: "O", 31: "p", 32: "P", 33: "q", 34: "Q", 35: "r", 36: "R",
            37: "s", 38: "S", 39: "t", 40: "T", 41: "u", 42: "U", 43: "v",
            44: "V", 45: "w", 46: "W", 47: "x", 48: "X", 49: "y", 50: "Y",
            51: "z", 52: "Z", 53: "1", 54: "2", 55: "3", 56: "4", 57: "5",
            58: "6", 59: "7", 60: "8", 61: "9", 62: "0", 63: "!", 64: "@",
            65: "#", 66: "$", 67: "%", 68: "^", 69: "&", 70: "*", 71: "(",
            72: ")", 73: "_", 74: "-", 75: "+"
            }
        
    def getLength(self):
        while self.length < 8: 
            self.length = int(raw_input("Enter the length of password needed: "))
            print " "
            if self.length < 8: 
                print "8 is the minimum value."
                print " "
                
    def getAmount(self):
        while self.amount <= 0:
            self.amount = int(raw_input("Enter the amount of passwords needed: "))
            print " "
            if self.amount <= 0:
                print "1 is the minimum value."
                print " "
        
    def passGenerator(self):
        while len(self.password) != self.length:
            key = random.randint(1,75)
            self.password = self.password + self.dictionary[key]
            
    def strengthCheck(self):
        if find(r'\d', self.password) and find(r'\W',self.password) and find(r'\w', self.password) and find(r'[!,@,#,$,%,^,&,*,(,),_,-,+]', self.password): self.passCheck = True
        else: self.password = ""
            
    def printPass(self):
        num = len(self.passwordArray) - 1
        print "Your randomly generated passwords are: "
        print " "
        while num >= 0:
            print self.passwordArray[num]
            print " "
            num -= 1
        time.sleep(60)
        
    def welcome(self):
        print " "
        print "-"*77
        print "-" + " "*24 + "Strong Password Generator " + " "*25 + "-"
        print "-"*77
        print " "
        
    def postPross(self):
        self.passwordArray.append(self.password)
        self.passCheck = False
        self.password = ""    
        self.amount -= 1
        
    def delAll(self):
        del self.length
        del self.passCheck
        del self.password
        del self.dictionary
        
    def __main__(self):
        self.welcome()
        self.getLength()
        self.getAmount()
        while self.amount > 0:
            while self.passCheck != True:
                self.passGenerator()
                self.strengthCheck()
            self.postPross()
        self.printPass()
        self.delAll()
        
pg1 = passGenerator()
pg1.__main__()