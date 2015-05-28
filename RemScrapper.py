import requests
from bs4 import BeautifulSoup as BS
from reportlab.pdfgen import canvas
import re

payload= {'username':' ','password':' ', 'login':'Log In'}
details= {}

session = requests.session()
page = session.post('http://rembook.nitt.edu/home/login',data=payload)

response = BS(page.text).find('div',{'class':'panel','id':'alerts'})

notice = response.find_all('a')

rN=[]
names={}
detail = {}
rollNumbers=[]

for i in notice:
    rN.append(re.search('(\d+)',i['href']).group())
   
for i in (set(rN)):
    rollNumbers.append(i)


for i in notice:
    if i.get_text() == u'comments':
        continue
    names[re.search('(\d+)',i['href']).group()] = i.text

for i in rollNumbers:
    page = session.get('http://rembook.nitt.edu/home/{0}/#comment'.format(i))
    response = BS(page.text).find('div',{'class':'panel','id':'comment'})

    comment = [ X.text for X in response.find_all('h4')]

    detail[i] = {'Author : ':names[i] , 'People Call You : ': comment[0] , ' You Frequently Utter : ': comment[1] ,' Striking Features : ': comment[2], ' You  : ': comment[3] }
    
for i in detail:
    print ("Author : " ,names[i])
    you = detail[i]
    print (" Nicknames : " , you ['People Call You : '])
    print (" ")
    print (" You Frequently Utter : " , you[' You Frequently Utter : '])
    print (" ")
    print (" Striking Features : ", you[' Striking Features : '])
    print (" ")
    print (" You : ",you[' You  : '])
    print ("_________________XXXXXXXXXXXXXXXXXXX_________________")

