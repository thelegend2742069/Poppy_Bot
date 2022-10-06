import requests, bs4, re, datetime

def main(var):

    res = requests.get('https://apod.nasa.gov/apod/ap%s.html' %(var))       #get html page
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image = soup.select('img')                          #get image css

    try:                                                #get image url
        imgURL = 'https://apod.nasa.gov/apod/'+image[0].get('src')
    except IndexError:                                  #return error if no image on requested day
        return ('This day did not have an astropic.\nPlease check https://apod.nasa.gov/apod/ap%s.html' %(var))
    
    imgres = requests.get(imgURL)                       #request image page
    imgres.raise_for_status


    imgFile = open('images/astropic.jpg', 'wb')
    for chunk in imgres.iter_content(100000):           #download picture in chunks of 100kb
        imgFile.write(chunk)
    imgFile.close()


    explan = re.sub(r'(\s+|\n)', ' ', soup.select('p')[2].text).strip()     #print explanation of image
    return explan.split(' Tomorrow')[0]


def astropic(date="today"):
    if date == 'today':                                                         #check for relative dates
        date = re.sub('-','', str(datetime.date.today())[2:])

    elif date == 'yesterday':
        date = re.sub('-','', str(datetime.date.today())[2:])
        date = str(int(date)-1)
    elif len(date) != 6:
        return('This is not a valid date.')
    return main(date)