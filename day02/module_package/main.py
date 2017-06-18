"""
This program will calculate triangle area using the formula
area = height * bottom /2
"""
import geometry.triangle as triangle
import geometry.square as square
import geometry.circle as circle

print 'Main Program'
print 'Triangle area', triangle.calc_triangle_area(10, 5)
print 'Square area', square.calc_square_area(3)
print 'Circle area', circle.calc_circle_area(5)

