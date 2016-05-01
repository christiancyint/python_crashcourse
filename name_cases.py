"""A program to practice exercises 2-3 through 2-5"""

name_friend = "dr. von tillington"

message_1 = "Hello, " + name_friend + " let me show the cool Python stuff I'm learning!"
print message_1

message_2 = "Hello, " + name_friend.title() + " check this out!"
print message_2

message_3 = "Hello, " + name_friend.upper() + " check this out, too!"
print message_3

"""code to print a famous quotation from a climber"""

climber = "anonymous"
famous_quote = "Mountain climbing is extended periods of intense boredom, interrupted by occasional moments of sheer terror."
print famous_quote + " -- " + climber.title()

"""code to practice creating and eliminating whitespaces"""

climber_names = "climbers:\n\tjohn bachar\n\talex honnold\n\tdean potter"
print climber_names

climber_1 = " john long "
print climber_1.strip()
print climber_1.lstrip()
print climber_1.rstrip()
