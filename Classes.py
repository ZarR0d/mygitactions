# We use clases to define NEW TYPES. These types can have methods that we define in the body of the class and they also
# have attributes that we can set anywhere in our programs

# Basic types examples in Python:Numbers, Strings and Booleans
# Complex types examples in Python: Lists, Dictionaries

class Point: # By convention classes start with a capital letter (Pascal naming convention)
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point() # Instanciation of the class
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw() # Don't forget the parenthesis. Objects are called as functions

point2 = Point()
point2.x = 1
print(point2.x)