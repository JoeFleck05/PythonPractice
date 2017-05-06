
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