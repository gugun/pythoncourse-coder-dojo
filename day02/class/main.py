"""
Main program to calculate lots of geometry using class
"""

import geometry.triangle as triangle

print 'Main program calculate geometry using class'
t1 = triangle.Triangle(20, 100) #via init or construct
t2 = triangle.Triangle(200, 10)

print t1.calc_area()
print t2.calc_area()

t1.draw()