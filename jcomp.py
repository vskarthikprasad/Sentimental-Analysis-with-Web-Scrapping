import requests
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from textblob import TextBlob
analyzer=SentimentIntensityAnalyzer()
page = requests.get("https://www.goodreads.com/book/show/136251.Harry_Potter_and_the_Deathly_Hallows")
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
s1='it was amazing'
s2='it was ok'
s3='liked it'
s4='did not like it'
s5='really liked it'
pos=0
neg=0
stars=[]
names=[]
reviews=[]
likes=[]
dates=[]
text=[]
for l1 in soup.find_all('div',{'class': 'left bodycol'}):
	for l2 in l1.find_all('div',{'class': 'reviewFooter uitext buttons'}):
		for l3 in l2.find_all('div',{'class': 'updateActionLinks'}):
			for l4 in l3.find_all('span',{'class': 'likeItContainer'}):

				for l5 in l4.find_all('span',{'class':'likesCount'} ):

						likes.append(l5.text)

for r1 in soup.find_all('div',{'class': 'left bodycol'}):
	for r2 in r1.find_all('div',{'class': 'reviewHeader uitext stacked'}):
		for r3 in r2.find_all('span',{'class': 'staticStars'}):
			for r4 in r3.find_all('span',{'class':'staticStar p10'}):

					reviews.append(r3.attrs['title'])

for n1 in soup.find_all('div',{'class': 'left bodycol'}):
	for n2 in n1.find_all('div',{'class': 'reviewHeader uitext stacked'}):
		for n3 in n2.find_all('span',{'itemprop': 'author'}):
			for n4 in n3.find_all('a',{'class':'user'}):

				names.append(n4.text)

for d1 in soup.find_all('div',{'class': 'left bodycol'}):
	for d2 in d1.find_all('div',{'class': 'reviewHeader uitext stacked'}):
		for d3 in d2.find_all('a',{'class': 'reviewDate createdAt right'}):
			dates.append(d3.text)


for x1 in soup.find_all('div',{'class':'left bodycol'}):
	for x2 in x1.find_all('div',{'class':'reviewHeader uitext stacked'}):
		for x3 in x2.find_all('span',{'class':'staticStars notranslate'}):
			stars.append(x3.text)

for j in range(0,len(dates)):
	if (stars[j]==s1):
		stars[j]=5
	elif (stars[j]==s2):
		stars[j]=2
	elif(stars[j]==s3):
		stars[j]=3
	elif(stars[j]==s4):
		stars[j]=1
	elif(stars[j]==s5):
		stars[j]=4

"""
with open('my.csv','w',newline='') as f:
	fn=['c1','c2','c3']
	thewriter=csv.DictWriter(f,fieldnames=fn)
	thewriter.writeheader()
	thewriter.writerow({'col1':dates,'col2':names,'col3':reviews})
"""
for t1 in soup.find_all('div',{'class': 'left bodycol'}):
	for t2 in t1.find_all('div',{'class': 'reviewText stacked'}):
		for t3 in t2.find_all('span',{'class': 'readable'}):

				text.append(t3.text)

for j in range(0,len(dates)):
	line=text[j]
	analysis=TextBlob(line)
	if analysis.sentiment.polarity>0 and analysis.sentiment.subjectivity>0.5 and stars[j]>=2:
		pos=pos+1
	else:
			neg=neg+1

print ('postive reviews:')
print(pos)
print ('negative reviews:')
print(neg)

"""
line=text[15]
vs=analyzer.polarity_scores(line)
print(vs)
print(line)
"""

for i in range(0,len(dates)):
	row=[dates[i],names[i],reviews[i],likes[i],text[i],stars[i]]
	with open('my.csv','a',encoding='utf-8') as csvFile:
		writer=csv.writer(csvFile)
		writer.writerow(row)
csvFile.close()
