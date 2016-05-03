# Chapter 3 practicing lists in Python
# You can access values in a list by specifying their index, which starts at 0.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles[0].title()
print bicycles[2].title()
print bicycles[-1].title()

# Values in an index can be used like any other variable

message = "My first bicycle was a " + bicycles[0].title() + "."
print message
