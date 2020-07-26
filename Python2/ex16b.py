from sys import argv

script, filename = argv

print "Now we're going to read the file we just wrote in 16/16a."

file = open(filename)

print "If you want to continue this action, press RETURN."
print "Else, press CTRL+C."

raw_input('>>')

print "Reading the file..."

print file.read()

print "Now we'll close the file."
file.close()