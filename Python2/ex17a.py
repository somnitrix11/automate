from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "We'll be copying the contents of %s to %s." %(from_file, to_file)
print "Here's your file to be copied..."

infile = open(from_file).read()


print "The input file is %d bytes long." %len(infile)

print "Does the output file really exist? %r" %exists(to_file)

print "Ready? Hit RETURN to continue, CTRL-C to abort."

raw_input(">")

out_file = open(to_file,'w')
out_file.write(infile)

print "All right. All done."

