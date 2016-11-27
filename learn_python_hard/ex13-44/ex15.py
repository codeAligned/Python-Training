from sys import argv
#"unpacks" argv 
script, filename = argv
#opens up file with filename 'filename' and assigns file object to variable
txt = open(filename)
#prints out text with 'filename'
print "Here's your file %r:" % filename
#reads file with name 'filename'
print txt.read()

txt.close()