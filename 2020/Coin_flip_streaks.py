import random

for i in range(10000):
    spam = []
    for i in range(100):
        a = random.randint(0,1)
        spam.append(a)
    
    if spam[i]!=spam[i+1]:
        break
