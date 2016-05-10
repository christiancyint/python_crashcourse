# Organizing lists. Permanently sorting a list alphabetically using sort().

cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort()
print cars

# Reversing the sorting order by passing the reverse=True argument.

cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort(reverse=True)
print cars

# You can temporarily alphabetically sort a list using the sorted() method.

print ("\nHere is my previous list:")
print cars

print ("\nNow here is my new sorted list:")
print (sorted(cars))

print ("\nAnd here is my previous list again:")
print cars

# Reversing the order of a list using the method reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print cars

# Finding the length of a list using the len() function. Exercise conducted in terminal / python interpreter.

>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
>>> 
