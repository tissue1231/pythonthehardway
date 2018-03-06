# x is a strin
x= "There are %d types of people." % 10 
# binary is a string
binary = "binary"
#do_not is a string
do_not = "don't"
#y is a string
y = "those who %s and those %s." % (binary, do_not)
#This will pring x
print x
#this will print y
print y
#this will pring and tring and include the text from x in a raw string format
print "I said: %r." % x
#this will print the below text and include text from y
print "I also said: '%s." % y
#this is showing that hilarious is false
hilarious = False
#Joke isnt funny
joke_evaluation = "Isn't that joke so funny?! %r"
#this prints both joke_evaluation and hilarious content
print joke_evaluation % hilarious
#noth strings
w = "This is the left side..."
e = "a string with a right side."
#prints w and e
print w + e