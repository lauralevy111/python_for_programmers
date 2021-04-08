#Init

class Cat:

    def __init__(self):     #wahts self? in python when u create a new obj it will call the init meothod if u have one.
                                # you can use anyword you want in place of self, its traditional to do self.

        #^^this is an init method, you always need to call it like this with the  2 underscores
        #a function inside a class like this, is called a method, theyre diff but thats the diff
        #this method will get called every time u create an instance of this class :
        print("inside __init__(self) hello, Laura !")

cat1 = Cat()

class Dog:
    def __init__(age, name, fur_color, weight):
