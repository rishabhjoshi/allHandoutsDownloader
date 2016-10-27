# RUN AS ADMIN - $sudo python download_handouts.py

import urllib2
import bs4
import requests
import os

# ID URL
url = 'http://172.18.6.180/ID/Handouts.do'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text)

#selects all pdf links
links = [a.attrs.get('href') for a in soup.select('tr a[href^=/HANDOUTS]')]
#** try to do usin regex

currdirectory = os.getcwd()
directory = currdirectory+'/../Handouts'  # change if you want to access 
# some other directory other than the default.
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory)

#find all html under table which has class_ as tableGrid
# l is a list and so is d, but not x
l = soup.findAll('table', class_='tableGrid') 
# x stores the only instance of tableGrid
x = l[0]
d = x.findAll('tr')
d = d[1:]
# d now doesnt have table headings th, has only td
i=0
for ele in d:
    r = ele.findAll('td')
    if(r[3].contents[0] != '\n'):
        continue
    s = r[1].contents[0]+'_'+r[2].contents[0]
    #print i, s is filename
    s = s + '.pdf'
    file = open(s, 'w')
    pdffile = urllib2.urlopen('http://172.18.6.180/'+links[i])
    file.write(pdffile.read())
    file.close()
    i = i+1
print 'Successfully downloaded the handouts. Thank RISHABH JOSHI'
