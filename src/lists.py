#Lists

faveSingers = ["Whitney Houston", "Mariah Carey", "Celine Dion", "Joni Mitchell"]
#print (faveSingers) # print entire list surrounded by brackets
#print(faveSingers[0]) # prints first element in list faveSingers

#print(type(faveSingers))#prints "<class 'list'>"
print(len(faveSingers))

print(faveSingers)

#append:
faveSingers.append("Lady Gaga")#adds Gaga as last element in the list
#insert:
faveSingers.insert(0,"Dolly Parton")#adds Dolly Parton as the first element
#update:
#faveSingers[5] = "Stefani Germanotta"# changes element [4] from "lady gaga" to her legal name, Stefani Germanotta
#remove:
faveSingers.remove("Joni Mitchell") #OR : #del(faveSingers[4])
#length:
print(len(faveSingers))


print(faveSingers)
