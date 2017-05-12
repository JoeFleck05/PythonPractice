
# for [variable_name] in [iterable_name]: [instructions] where [variable_name]
name = "Joe"
for character in name:
    print(character)

print("")

# to iterate through the items
shows = ["Got","NARCOS","Vice"]

for show in shows:
    print(show)

print("")

# iterate through items in a tuplate
coms = ("A. Development","Friends","Always Sunny")

for show in coms:
    print(show)

print("")

# iterate through the keys in a dictionary
people = {"G. Bluth II":
          "A. Development",
          "Barney":
          "HIMYM",
          "Dennis":
          "Always Sunny"}

for character in people:
    print(character)

print("")

# change items in a mutable iterable
tv=["GOT",
    "Narcos",
    "Vice"]

i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

print("")

#
tv = ["GOT","Narcos","Vice"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

print("")
# You can use for-loops to move data between mutable iterables.
# For example, you can use two for-loops to take all the strings
# from two different lists, capitalize each character in them, and
# put them into a new list:

tv = ["GOT","Narcos","Vice"]

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

print("")
#
tv = ["GOT","Narcos","Vice"]
coms = ["Arrested Development","Friends","Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

# range function to create a sequence of integers, and use a for-loop to iterate through them.
# The range function takes two parameters: a number where the sequence starts and a number where
# the sequence stops. The sequence of integers returned by the range function includes
# the first parameter (the number to start at), but not the second parameter
# (the number to stop at).


