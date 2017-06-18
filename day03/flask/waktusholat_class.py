import requests
import bs4

class Prayer_Times:
    url = 'http://jadwalsholat.pkpu.or.id/?id=83'

    def __init__(self):        
        ''
    def waktu_berbuka(self, options):
        data = self.request_url(self.url)

        if data != '':
            parse = self.parsing_data(data, 'maghrib_time')
            return parse

    def request_url(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            data = bs4.BeautifulSoup(r.content, 'html.parser')
        else:
            data = ''
        
        return data
    def parsing_data(self, data, options):        
        if options == 'maghrib_time':
            #find table_highlight class
            row=data.find_all('tr', 'table_highlight')
            column = row[0]            
            
            i = 0
            for c in column:
                if i == 5:
                    maghrib = c.text
                
                i = i + 1
            result = maghrib
        else:
            result = 'undefined'
        
        return result