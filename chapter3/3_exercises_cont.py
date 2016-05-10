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
