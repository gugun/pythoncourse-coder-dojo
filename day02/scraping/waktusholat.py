"""
WebScrapping waktu sholat from pkpu
"""
import requests
import bs4

url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=308'
r = requests.get(url)

if r.status_code == 200:    
    data = bs4.BeautifulSoup(r.content, 'html.parser')    

    #find table_highlight class
    row=data.find_all('tr', 'table_highlight')
    column = row[0]
    
    i = 0
    for c in column:
        if i == 5:
            maghrib = c.text
        
        i = i + 1
        
    print('Waktu berbuka puasa', maghrib)
else:
    print('Unable to get data from website')