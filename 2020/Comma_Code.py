#Note: This prints the list items vertically, like how the
#the 'print' function outputs them. But a program to print
#it in a single line remains elusive

from itertools import count

print("Enter the items in a list. (Enter nothing when finished.)")

spam = []


for i in count():
    a = input()
    if a == '':
        break
    else:
        spam.append(a)

def comma(spam):
    if spam == []:
        return print("This is an empty list.")
    else:
        for i in range(0,len(spam)-1):
           print(str(spam[i])+', ')
    print('and '+str(spam[len(spam)-1])+'.')

b = comma(spam)


