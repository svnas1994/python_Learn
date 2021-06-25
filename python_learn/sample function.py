def printfunction():
    a=input("enter your name")
    retrun (a)

try:
    b = printfunction()
    print (b)
except Exception as c:
    print ("excetption is ", c)