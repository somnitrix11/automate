#a = 0 #Setting the initial value of a to 0
#while a < 10: #Remember to put ':' at the end of while statement
#  a = a + 1
#  print(a)

a=1
s=0
print("Enter nos. to add to the sum:")
print("Enter 0 to quit.")
while a!=0:
    print("Current Sum:",s)
    a=float(input("Number?"))
    s=s+a
print("Total sum=",s)
