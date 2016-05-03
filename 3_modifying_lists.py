# Practice from Chapter 3. Modifying values in a list.

motorcycles = ["honda", "yamaha", "suzuki"]
print motorcycles

# You can change the value in a list by specifying its index and then creating a new value.

motorcycles[0] = "ducati"
print motorcycles

motorcycles[0] = "honda"
print motorcycles

# You can append values to a list by using the method append()

motorcycles.append('ducati')
print motorcycles

# You can dynamically add values to an empty list using append()

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print (motorcycles)

# You can insert a value into any position in the list by using the method insert()

motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, 'ducati')
print motorcycles

# You can remove values from a list by using the method

del motorcycles[1]
print motorcycles

# You can use the pop() method to remove a value from a list, but still use taht value later on
