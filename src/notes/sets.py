#Sets

#list of singers w a duplicate item
#faveSingers = ["Dolly Parton", "Whitney Houston", "Mariah Carey", "Celine Dion","Lady Gaga","Whitney Houston"]
#Whitney Houston is two elements, theres a dupe in this list
#print(faveSingers)
#^tolerates dupe, prints: ['Dolly Parton', 'Whitney Houston', 'Mariah Carey', 'Celine Dion', 'Lady Gaga', 'Whitney Houston']


#set of singers w a duplicate item
faveSingers = set(["Dolly Parton", "Whitney Houston", "Mariah Carey", "Celine Dion","Lady Gaga","Whitney Houston"])
#removed dupe.
print(faveSingers) #prints:{'Whitney Houston', 'Dolly Parton', 'Mariah Carey', 'Celine Dion', 'Lady Gaga'}

#can i print an item by index?no :/
#print(faveSingers[2])#returns: TypeError: 'set' object is not subscriptable

#how do i append an item to the end?:
faveSingers.add("Robyn")
