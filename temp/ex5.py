human_name = 'Zed A. Shaw'
human_age = 35 #not a lie
human_height = 74 * 0.393701 # inches
human_weight = 180 * 2.2 # lbs
human_eyes = 'Blue'
human_teeth = 'White'
human_hair = 'Brown'

print "Let's talk about %s." % human_name
print  "He's %d inches tall." % human_height
print "he's %d pounts heavy." % human_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (human_eyes, human_hair)
print "His teeth are usually %s depending on the coffee." % human_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (human_age, human_height, human_weight, human_age + human_height + human_weight) 