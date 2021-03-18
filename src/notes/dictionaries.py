#Dictionaries = stores key/value pairs
'''each value in the list has a number associated with it
in a dictionary  you have these things called keys
you want a value, you give the key to get the value.
'''

dogsAges= {"Zilpha":8, "Greyson":5, "Beauregard":1,"Gidget":1, "Apollo":0}#name = key, age = value
'''keys have to be mutable, ints floats strings all work. tuple is immutable so that wont work.
you can add a item to this dictionary with an int key and a string value! and that'll be okay!

dictionaries are organized by key ONLY!! they have no order
'''

#adding to Dictionaries
dogsAges["Mason"]=7

#deleting :
del(dogsAges["Greyson"])

print(dogsAges)

#dictionary.keys() method:
#for name in dogsAges.keys(): #loops through keys
print(dogsAges.keys())# will print: dict_keys(['Zilpha', 'Beauregard', 'Gidget', 'Apollo', 'Mason'])
for name in dogsAges.keys(): #loops through keys, instructor says you cant be sure what order they'll be in
    print(name)

#dictionary.values() method:
print(dogsAges.values())# will print : dict_values([8, 1, 1, 0, 7])

#dictionary.items() method:
print(dogsAges.items()) # will print : dict_items(['Zilpha',8), ('Beauregard',1), ('Gidget',1), ('Apollo',0), ('Mason',7)])
#^^ this is each of the items in the dictionary as a tuple.
