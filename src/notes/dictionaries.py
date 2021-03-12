#Dictionaries = stores key/value pairs
'''each value in the list has a number associated with it
in a dictionary  you have these things called keys
you want a value, you give the key to get the value.
'''

dogsAges= {"Zilpha":8, "Beauregard":1,"Gidget":1, "Apollo":0}#name = key, age = value
'''keys have to be mutable, ints floats strings all work. tuple is immutable so that wont work.
you can add a item to this dictionary with an int key and a string value! and that'll be okay!
'''

#adding to Dictionaries
dogsAges["Mason"]=7


print(dogsAges)
