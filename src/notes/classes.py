#like a blueprint for the py app
#so you can create as many objs liek this class as ou like
#instance variable = usuallly unique

class Dog:
    dogInfo = "Dogs are animals iwth 4 legs and a tail"

    "Hello new dog"

dog1 = Dog()
dog1.name = "Zilpha"
dog2 = Dog()
dog2.name = "Gidgette"
dog3 = Dog()
dog3.age = 8 # you can create instance variable kinds on the fly

print(dog1.dogInfo)
