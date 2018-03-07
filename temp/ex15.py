# This imports the argument value from the sys
from sys import argv
#this uses argv to get a file
script, filename = argv
#this opens the file
txt = open(filename)
#This prints out the filename
print "Here's your file %r:" % filename
#this prints out the contents of the file
print txt.read()
#this prints out the a string that prompts for the file name again
print "type the file again:"
file_again = raw_input("> ")
#This defines txt_again as the file that will be opened
txt_again = open(file_again)
#This prints out the file once again after the user inputs the file name
print txt_again.read()
txt.close()
txt_again.close()