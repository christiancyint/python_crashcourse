# You can use the pop() method to remove a value from a list, but still use that value later on

motorcycles = ["honda", "yamaha", "suzuki"]
print (motorcycles)

popped_motocycles = motorcycles.pop()
print motorcycles
print popped_motocycles

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print ("\nThe last motorcycle I owned was a " + last_owned.title() + ".")

# Popping items in a list by specifying their index

first_owned = motorcycles.pop(0)
print "\nThe first motorcycle I owned was a " + first_owned.title() + "."

# Remember that each time you use pop(), the item you work with is no longer stored in the list. When you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

# Removing a value using remove(). This removes the first matching value, not an index. Use del to remove a specific index. Reference: http://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists. 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

motorcycles.remove('ducati')
print motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print motorcycles
print ("\nA " + too_expensive.title() + " is too expensive for me.")
