"""
Let's create our first class!
"""

class Triangle(object):
    """ Triangle comments """
    COUNT = 0 #CLASSS VARIABLE, Public to Triangle class. Sharing.

    def __init__(self, bottom, height):
        """ init func """
        self.name = 'Triangle' #OBJECT VARIABLE. Private to each object
        self.bottom = bottom
        self.height = height
        Triangle.COUNT = Triangle.COUNT + 1

    def calc_area(self):
        """ calc area docstring """
        return self.bottom * self.height / 2

    def draw(self):
        """ calc area docstring """
        print 'Geometry name=', self.name, 'Count=', Triangle.COUNT
