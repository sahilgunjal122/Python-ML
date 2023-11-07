#1.maxi between two numbers

'''
a=int(input("Enter Num1:"))
b=int(input("Enter Num2:"))

if(a>b):
    print("{} is MAX number between {} & {}".format(a,a,b))
else:
    print("{} is MAX number between {} & {}".format(b, a, b))
'''


#2.check number is negative
'''
neg=int(input("Enter Number:"))
if(neg<0):
    print("{} is the negative Number".format(neg))
'''

#3.even or odd
'''
numeo=int(input("Enter Number to Check Even odd:"))
if(numeo % 2 == 0):
    print("%d is an Even Number" %numeo)
else:
    print("%d is an Odd Number" % numeo)
'''

#4.number Divisible by 5
'''
num=int(input("Enter Number:"))

if(num%5==0):
    print("%d Number is Divisible by 5" %num)
else:
    print("%d Number is Not Divisible by 5" %num)
'''

#5.week days
'''
num=int(input("Enter Number:"))

if(num==0):
    print("Monday")
elif(num==1):
    print("Tuesday")
elif(num==2):
    print("Wednesday")
elif(num==3):
    print("Thursday")
elif(num==4):
    print("Friday")
elif(num==5):
    print("Saturday")
else:
    print("Sunday")
'''

#6.character is alphabet or not
'''
n=input("Enter Your Input:")

if(ord(n)>=65):
    print("{} is charater".format(n))
else:
    print("{} is Integer".format(n))
'''

#7.months & days
'''
month=int(input("Enter Month:"))

if(month==1):
    print("January is a 31-Day Month")
elif(month==2):
    print("Feb is a 28/29-Day Month")
elif(month==3):
    print("March is a 31-Day Month")
elif(month==4):
    print("April is a 30-Day Month")
elif(month==5):
    print("May is a 31-Day Month")
elif(month==6):
    print("June is a 30-Day Month")
elif(month==7):
    print("July is a 31-Day Month")
elif(month==8):
    print("August is a 31-Day Month")
elif(month==9):
    print("Sep is a 30-Day Month")
elif(month==10):
    print("Oct is a 31-Day Month")
elif(month==11):
    print("Nov is a 30-Day Month")
elif(month==12):
    print("Dec is a 31-Day Month")
else:
    print("Invalid Month")

'''

#8.Greater than 10
'''
num=int(input("Enter Num:"))
if(num>10):
    print("%d is Greater than 10" %num)
elif(num==10):
    print("%d is Equal to 10" %num)
else:
    print("Number is Less than  10")
'''

#9.vowel or not
'''
char=input("Enter the Character:")

if len(char)==1  and ((char=='a' or char=='e' or char=='i' or char=='o' or char=='u')):
    print("Vowel")
elif len(char)==1 and ((char>='a' and char<='z')and (char !='a' and char!='e' and char!='i' and char!='e' and char!='o')):
    print("Consonant")
else:
    print("Special Charcter")
'''

#10.leap year

year=int(input("Enter Year:"))

if(year%4==0 and year %100 !=100) or (year%400==0):
    print("{} Year is a Leap Year".format(year))
else:
    print("{} is Not a Leap Year")
