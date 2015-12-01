name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cent = 74 * 2.54
weight = 180 # lbs
weight_kilo = 180 * 0.4535924
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches (%f centmeters) tall." % (height, height_cent)
print "He's %r pounds (%f kilograms) heavy." % (weight, weight_kilo)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." %(eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)