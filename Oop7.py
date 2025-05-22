#Public and Private only use with in the class
class person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
    
    def welcome(self):
        self.__hello()

p1 = person()

print(p1.welcome())
        