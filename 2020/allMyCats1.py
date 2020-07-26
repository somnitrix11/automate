#print("Enter name of cat 1:")
#cat1=input()
#print("Enter name of cat 2:")
#cat2 = input()
#print("Enter name of cat3:")
#cat3 = input()
#print("Enter the name of cat 4:")
#cat4 = input()

#print("The cat names are:" +cat1 + cat2 + cat3 + cat4)

#Doing the same thing with lists

catNames = []
while True:
    print('Enter the name of the cat' + str(len(catNames)+1)+' (or enter nothing to stop)')
    name = input()
    if name =='':
        break
    catNames = catNames + [name] #List concatenation i.e. adding the new names to the previous list

print('The cat names are:'+ str(catNames))


