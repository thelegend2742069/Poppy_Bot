import requests, bs4, re, random


def xkcdDownload(number):
    res2 = requests.get(f"https://xkcd.com/{number}/")     #get requested comic issue html page
    soup = bs4.BeautifulSoup(res2.text, 'html.parser')

    title = str(soup.select('#ctitle'))             #get title html code
    elem = soup.select('#comic img')                #get image html code

    comicUrl = 'https:'+elem[0].get('src')          #get image url
    res3 = requests.get(comicUrl)

    image = open("images/xkcd.jpg", 'wb')


    for chunk in res3.iter_content(100000):         #download image in chunks of 100kb
        image.write(chunk)
    image.close()
    return (f'xkcd #{number}: {title[18:-7]}')

    
def comic(issue=None):
    res = requests.get("https://xkcd.com")          #get xkcd html page
    res.raise_for_status()


    current_finder = re.compile(r'/(\d+)/')         #find latest issue number
    current = int(current_finder.findall(res.text)[0])


    if not issue:
        issue = random.randint(1, current)     #choose random issue number if no input (random function includes upper bound)
        return xkcdDownload(issue)

    if int(issue)>current:
        return f"Issue number #{issue} does not exist. Latest issue is {current}."

    else:
        return xkcdDownload(issue)
