from sys import argv

script, filename = argv

txt = open(filename) #txt is a variable which opens a file

print "Here's your file %r:" %filename #prints text, nothing fancy
print txt.read() #Calling a function on txt named read
#You can give command to a file opened by using '.'

print "Type the filename again:" #Doing it again, this time using rawinput
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

print txt_again.close()