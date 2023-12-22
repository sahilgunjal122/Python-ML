#1. WAP to check numbers are divisible by 4 and 5 Print those numbers

# x=int(input("Enter Number:"))
# if(x%4==0 & x%5==0):
#     print("%d The Number is Divisible by 4 & 5" %x)
# else:
#     print("Number is Not Divisble by 5 & 4")

#2. WAP to determine whether entered angles define a right-angled triangle. Take three values of angle from the user.

# x=int(input("Enter First Angles :"))
# y=int(input("Enter Second Angles :"))
# z=int(input("Enter Third Angles :"))
# sum=x+y+z;
#
# if(sum==180):
#     print("{},{},{} Can Define the Righ-Angled Triangle".format(x,y,z))
# else:
#     print("Not Define A Right-Angled Triangle")


#3.Take two numbers from users and print the sum of those numbers if the sum is even.

# x,y=[int(x) for x in input("Enter Two Numbers:").split()]
#
# sum=x+y
# if(sum%2==0):
#     print("The Sum is {}".format(sum))

#4.Take a number from the user and check whether it is present in the list. If it's in the list, print "Available."

# List1 = [10, 20, 30, 40, 50]
# num=int(input("Enter Number to be Found:"))
#
# if(num in List1):
#     print("Available")
# else:
#     print("Not Available")

#5.Print the "Core2web" string a number of times entered by the user if the number is even.

# string="Core2web"
# num=int(input("How Many Times The String Should be Print:"))
#
# if(num%2==0):
#     print(num *string.format(num))
# else:
#     print("Not a Even Number")

#6.Write a program that checks if a given number is odd using the "if" statement.

# num=int(input("Enter Number:"))
# if(num%2!=0):
#     print("Number is ODD")

#7.Take two numbers from the user, check if both are odd and then print the sum of the numbers.

# x,y=[int(x) for x in input("Enter Two Numbers:").split()]
#
# if(x%2!=0 and y%2!=0):
#     sum=x+y
#     print("Sum of Two Numbers is %d" %sum)

#8.Take single character from user check if the ascii value of character is Even the print character.

# string=input("Enter a Character:")
# asciiii=ord(string)
#
# if(asciiii%2==0):
#     print("The Character is {}".format(string))


#9.Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character
# char1,char2=input("Enter two Character:").split()
# a=ord(char1)
# b=ord(char2)
#
# if a%2!=0 and b%2!=0:
#     sum=a+b
#     print("The Sum of Ascci is {}".format(sum))


#10.Take the number from user and modulus with 8 if the reminder of the number is 3 then print reminder.

num=int(input("Enter Number:"))

if(num%8==3):
    print("number is {}".format(num))








