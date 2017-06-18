""" Main Program """
from flask import Flask
import waktusholat_class as p

app = Flask(__name__)
prayer = p.Prayer_Times();
options = {
        'maghrib':'maghrib_time',
        'all':'all'
    }

@app.route('/')
def index():
    return 'Assalamualaykum'

@app.route('/waktu-berbuka')
def bukaa():
    return "Waktu berbuka hari ini: %s" % prayer.waktu_berbuka(options["maghrib"])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8888)