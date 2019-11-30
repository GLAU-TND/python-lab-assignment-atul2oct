#Define an custom exception (i.e user define exception) class called "MyException".
#This class contains a parameterized constructor which accept one argument String message.
#Whenever this exception arise will print "Custom Exception Occured".
#Create another function called Xyz.
#This function perform sum of two user given values by using standard input.
#If the sum is less than 150 throw user defined exception or else display sum.
#i/p:
#   a = 30
#   b = 40
#   sum = a + b
#   as sum is 70 .. then
#o/p:
#   custom exception is occured
class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        return str(self.v)
def Xyz(a, b):
    c = a + b
    if c < 150:
        raise MyException("Custom Exception Occurred")
    else:
        return c

a=eval(input("a = "))
b=eval(input("b = "))
result=Xyz(a,b)
print("sum = a + b")
print("as sum is ",result)
