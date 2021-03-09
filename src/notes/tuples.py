#Tuples! :)

#faveSingers = ["Dolly Parton", "Whitney Houston", "Mariah Carey", "Celine Dion","Lady Gaga"]
#print(type(faveSingers)) #this is a list^ we made lists in lists.py


#to make a tuple: you just make a list ^^^ but use parenthases instead of square brackets
faveSingers = ("Dolly Parton", "Whitney Houston", "Mariah Carey", "Celine Dion","Lady Gaga")
#print(type(faveSingers))#this is a tuple^^^ so easy

#can we get from index? yes
print(faveSingers[2])#works

#can we change the tuple or elements? no 
#faveSingers[4]= "Stefani Germanotta" #this line wont work bc you cant  chage the elements of a tuple
#faveSingers.append("Kali Uchis")#this line wont work bc there's no append method for tuples
