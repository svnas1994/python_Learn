"""This programme is for arithmatic operation of two numbers"""
a = int(input("enter the number"))
b = int(input("enter the number"))
print ("for addtion enter add\n\
for subtraction etner sub\n\
for multipliction enter mul\n\
for remainder of division add rem")
c=input("enter your required operation").lower()
def add(a, b):
    '''adding the two numbers'''
    print (a+b)
def sub(a, b):
    '''subtracting the two numbers'''
    print (a-b)
def mul(a, b):
    '''multiplication the two numbers'''
    print (a*b)
def rem(a,b):
    ''' remainder of divison'''
    print(a%b)
if c == "add":
    add(a, b)
elif c == "sub":
    sub(a, b)
elif c == "mul":
    mul(a, b)
elif c == "rem":
    rem(a,b)
else:
    print ("the requested operation is not supported")
    
print ("adding some extra lllinasdfe")