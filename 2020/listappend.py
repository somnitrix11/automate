
#These methods only apply to lists
#append() to a list, adds to the end of list
spam = ['cat','dog','bat']

spam.append('moose')

print(spam)

#insert() Can add values to any place in the list; adds, doesn't replace
spam.insert(1,'chicken')

print(spam)

#remove() can remove a value from a list
spam.remove('chicken')
print(spam)

#sort() can sort values dec. to inc. or alphabetically(Upper case come first tho)

spam.sort()
print(spam)
spam.sort(reverse=True) #does what you think it does
print(spam)

