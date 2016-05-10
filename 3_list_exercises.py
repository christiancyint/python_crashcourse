# Practicing exercises from Chapter 3

# Exercise 3-1: Names

my_friends = ["Laser", "Blazer", "Razor", "Blade"]

print my_friends[0].upper()
print my_friends[1].upper()
print my_friends[2].upper()
print my_friends[-1].upper()

# Exercise 3-2: Greetings

print "\nHey, " + my_friends[0] + " let's play some dodgeball!"
print "Hey, " + my_friends[1] + " let's play some dodgeball!"
print "Hey, " + my_friends[2] + " let's play some dodgeball!"

# Exercise 3-3: Your Own List

climbing_destinations = ["boat rock", "rocktown", "new river gorge", "rumney rocks"]

print "\nMan, I'd love to vist " + climbing_destinations[-1] + "!"
print "Man, I need to get back to " + climbing_destinations[0] + "!"

# Exercise 3-4: Guest List. Print statements of the list are simply for learning, but I would not expect to include those in a final program.

my_guests = ['lincoln', 'nixon', 'washington']
print "\nHello, Mr." + my_guests[0].title() + " , I'd like you to join me."
print "\nHello there, Mr. " + my_guests[1].title() + " you are not a criminal. Join me for dinner?"
print "\nHi, Mr. " + my_guests[-1].title() + " let's ford the river and eat dinner!"

# Exercise 3-5: Changing Guest List

print "\nExercise 3-5"
print "\nOh no! Mr. " + my_guests[1].title() + " can't make it."
my_guests.remove('nixon')
print my_guests
my_guests.insert(1, 'reagan')
print "I guess we can invite Mr. " + my_guests[1].title() + " instead."
print my_guests

# Exercise 3-6: More Guests

print "\nExerise 3-6"
