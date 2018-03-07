#imports argv from module sys
from sys import argv
#this shows that this is a script and what variable is the argv
script, filename = argv
#adds file name to the string
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#asks the question whther they want to delete the file or not
raw_input("?")
#opens the file
print "Opening the file..."
target = open(filename, 'w')
#delets the contents of the file
print "Truncating the file.   Goodbye!"
target.truncate()

print "Now I'm going to ask you for threee lines."
#has us input 3 lines of text
line1 = raw_input("line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."
#writes the text you wrote ot the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#closes the file
print "And finally, we close it."
target.close()

