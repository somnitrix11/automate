#Tuples vs. Lists

#tuples are immutable (can't be changed once declared)

a = (1,2,4)

a.remove

print(a) #this will output an error

#Tuples are useless lists with parentheses and are immutable
#Why did they even bother with this type I wonder...
#Tuples can be converted into lists and vice versa

list((a))