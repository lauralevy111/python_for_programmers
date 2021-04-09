#Inits

class Dog:
    def __init__(self, age, name, fur_color, weight):
        self.name = name #self.name = instance variable, name = value from constructor
        self.age = age
        self.fur_color = fur_color
        self.weight = weight
        print("creating a dog")
        #print(self.weight)

    def bark_hello(self):
        print("Hello, bark bark!")

    def bark_goodbye(self):
        print("Bark bark, goodbye")

dog1 = Dog("Zilpha",8,"White",10)
dog1.bark_hello()
dog1.bark_goodbye()
