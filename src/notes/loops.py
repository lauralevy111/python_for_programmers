#Loops
faveSingers = ["Dolly Parton", "Whitney Houston", "Mariah Carey", "Celine Dion","Lady Gaga","Whitney Houston"]

#forloops
'''
for x in range(5):
    print(x)#printing iterator, x, starts at 0, ends @4

print("******(***)")
for n in range(5,12):
    print(n)#prints 5 - 11



for singer in faveSingers:
    print(singer)
'''
#whileloops
capacity = 300
'''
while capacity< 330:
    print(capacity)
    capacity+=1


guess = input("Guess a number between 1 and 10:")
while guess != "9":
    guess = input("thats not it, guess again please:")
print("you win!💃")

'''

#break:
for x in range(10):
    print(x)
    if x ==5 :
        break
print("All done")

#continue:
for x in range(10):
    print(x)
    if x ==5 :
        print("I will now continue")
        continue
    print("x ! = 5")
print("All done")

#else:
for x in range(10,14):
    print(x)
    if x ==5 :
        print("I will now continue")
        break#the addition of this line means we break out of the loop & we dont even touch the else
    print("x ! = 5")
else:
    print("💅 else")
print("All done")
