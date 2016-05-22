# Exercise 3-8: Seeing the World

print "Exercise 3-8: Seeing the World\n"

locations = ['joshua tree', 'yosemite', 'new river gorge', 'rocktown', 'grand mother mountain']
print locations

print sorted(locations) # printing the list alphabetically and temporarily.
print locations # printing the original list.
print (sorted(locations,reverse=True)) # printing hte list in reverse order.

# Using the reverse() method.

locations.reverse()
print locations

locations.reverse() # reversing the order of the list again back to its originial order.
print locations

# Exercise 3-9: Dinner Guests

print "\nExercise 3-9: Dinner Guests\n"

# Copying code from Exercise 3-4 to re-build a full guest list - simply for practice and to re-examine the earlier code and methods used.

my_guests = ['lincoln', 'nixon', 'washington']

my_guests.insert(0, 'bush')
my_guests.insert(1, 'adams')
my_guests.append('clinton')

print my_guests
print len(my_guests)

# Exercise 3-10: Every Function

print ("\nExercise 3-10: Use Every Function")

ttp_lateralmovement = ['application deployment software', 'exploitation of vulnerability', 'logon scripts', 'pass the hash', 'peer connections', 'remote desktop protocol', 'windows management instrumentation', 'windows remote management', 'remote services']

print ("\nHere is a list of possible adversary lateral movement techniques:\n")
print ttp_lateralmovement

print "\nThe use of " + ttp_lateralmovement[7].title() + " is an increasingly common technique.\n"

ttp_lateralmovement.append('remote services')
ttp_lateralmovement.insert(-1, 'windows admin shares')

print ttp_lateralmovement

del ttp_lateralmovement[4]
print ttp_lateralmovement

popped_ttp = ttp_lateralmovement.pop()
print "\nI'm not too familiar with the " + popped_ttp.title() + " technique."

ttp_lateralmovement.remove('remote services')
print ttp_lateralmovement

ttp_lateralmovement.sort(reverse=True)
print ttp_lateralmovement
