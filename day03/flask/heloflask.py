from flask import Flask
# import sys
# sys.path.append('H:\Project\course\python')

import day02.module_package.geometry.triangle as triangle
import day02.module_package.geometry.circle as circle
import day02.module_package.geometry.square as square

application = Flask(__name__)
@application.route('/')
def index():
    return 'Hello World!'

@application.route('/segitiga/<int:bottom>/<int:height>')
def segitiga(bottom, height):
    return 'Triangle: %d' % triangle.calc_triangle_area(bottom, height)

@application.route('/lingkaran/<int:rad>')
def lingkaran(rad):
    return 'Circle: %d' % circle.calc_circle_area(rad)

@application.route('/bujursangkar/<int:side>')
def bujursangkar(side):
    return 'Square: %d' % square.calc_square_area(side)

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0",port=8888)

