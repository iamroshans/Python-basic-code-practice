a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))
if a>b:
 if a>c:
  print("First given number is greater among all.")
elif b>c:
 print("Second number is greater.")
else:
 print("Third number is greater.")
 
 #Alternative code:
# a=float(input("Enter the first number: "))
# b=float(input("Enter the second number: "))
# c=float(input("Enter the third number: "))
# max=a
# if max<b:
#  max=b
# if max<c:
#  max=c
# print("The largest number is: ",max)
