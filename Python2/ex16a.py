from sys import argv

script, filename = argv

print "We're going to delete the contents of %r." %(filename)
print "To continue, press RETURN."
print "To abort, press CTRL+C."

raw_input('>')

file = open(filename, 'w')

file.truncate()

print "Your file has been successfully truncated."

print "Now type whatever you want to be in this file instead."

line = raw_input('Input:')

file.write(line)

print "Now we close it."
file.close()
 