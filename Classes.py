# We use classes to define NEW TYPES. These types can have methods that we define in the body of the class and they also
# have attributes that we can set anywhere in our programs

# Basic types examples in Python:Numbers, Strings and Booleans
# Complex types examples in Python: Lists, Dictionaries


class Point:  # By convention classes start with a capital letter (Pascal naming convention)
    def __init__(self, x, y):  # Self is a reference to the current ojbject #This method is a constructor. This methjod is used to contruct or create an object
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(0,0)  # Instanciation of the class
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()  # Don't forget the parenthesis. Objects are called as functions
point2 = Point(0,0)
point2.x = 1
print(point2.x)
