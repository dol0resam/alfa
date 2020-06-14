from bs4 import BeautifulSoup as BSHTML
import urllib3
import wget

http = urllib3.PoolManager()
crushname = input("Whats your crush's instagram username ?: -->")
url = 'https://www.instadp.com/fullsize/' + crushname

response = http.request('GET', url)
soup = BSHTML(response.data, "html.parser")
images = soup.findAll('img')

for image in images:
    #print image source
    print("Your crush src :", image['src'])

image_filename = wget.download(image['src'])

print("                         Image Successfully Downloaded !! : " , image_filename)