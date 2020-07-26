def eggs(SomeParameter):
    SomeParameter.append('Hello')

spam = [1,2,3]

eggs(spam)
print(spam) #eggs function changes the list(spam) in-place