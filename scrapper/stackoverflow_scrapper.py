import requests 
from bs4 import BeautifulSoup 
import csv 
import pandas as pd
import re
import sys,traceback
#csv=pd.read_csv('mayank.csv',header=None)
#URL = "https://www.youtube.com/watch?v=9DAKh_XCk6g"
c=0
rows=[]
#print(csv[0])
		#print(url['href'])
#url='https://stackoverflow.com/questions/2742124/insert-text-into-a-div-from-a-poput-form-and-rewrite-the-inserted-text-with-java/2742623#2742623'

#url='https://stackoverflow.com/questions/tagged/javascript?tab=Votes'
#url='https://stackoverflow.com/questions/tagged/javascript?tab=Votes'
#url='https://stackoverflow.com/search?q=js'
#url='https://stackoverflow.com/search?q=user:816620+[javascript]'
#url='https://stackoverflow.com/search?q=user:5445+[javascript]'
#url='https://stackoverflow.com/search?q=user:1447675+[javascript]'
#url='https://stackoverflow.com/search?q=user:1048572+[javascript]'
#url='https://stackoverflow.com/search?q=user:34397+[javascript]'
#url='https://stackoverflow.com/search?q=user:896358+[javascript]'
#url='https://stackoverflow.com/search?q=user:5458200+[javascript]'
#url='https://stackoverflow.com/search?q=user:5018300+[javascript]'
#url='https://stackoverflow.com/search?q=user:519413+[javascript]'

#url='https://stackoverflow.com/search?q=user:5648954+[javascript]'
#url='https://stackoverflow.com/search?q=user:65387+[javascript]'
#url='https://stackoverflow.com/search?q=user:7461381+[javascript]'
#url='https://stackoverflow.com/search?q=user:1479419+[javascript]'
#url='https://stackoverflow.com/search?q=user:62076+[javascript]'
#url='https://stackoverflow.com/search?q=user:1646240+[javascript]'
#url='https://stackoverflow.com/search?q=user:3858806+[javascript]'
#url='https://stackoverflow.com/search?q=user:69083+[javascript]'
#url='https://stackoverflow.com/search?q=user:13249+[javascript]'
#url='https://stackoverflow.com/search?q=user:9021+[javascript]'
#url='https://stackoverflow.com/search?q=user:675721+[javascript]'
url='https://stackoverflow.com/search?q=user:476+[javascript]'
#page6 done
r = requests.get(url,verify=False) 
soup = BeautifulSoup(r.content, 'html.parser') 
questions=soup.findAll("a",{'class':'question-hyperlink'})



for question in questions:
	print(question['href'])
	try:
		if(question['href'][0]!='/'):
			continue
		url='https://stackoverflow.com'+question['href']

		r = requests.get(url,verify=False) 

		soup = BeautifulSoup(r.content, 'html.parser') 
			  
	#			print(tags)
		title = soup.find("div",{'id':'question-header'})
		#print(title.text.replace('Ask Question',''))
		answers = soup.find("div",{'class':'answer accepted-answer'})
#		print(answers)
#		children = answers.findChildren('div',{'class':'snippet-code'})
		children = answers.findChildren('pre')
		if(len(children)>3):
			continue
		print(children[0].text)
		
		description=soup.find("div",{'class':'post-text'})
		#print(description.text)
	#			print(description)
	#			break
		rows.append({'url':url,'title':title.text.replace('Ask Question',''),'description':description.text,'answer':children[0].text})
		df=pd.DataFrame(data=rows,columns=['url','title','description','answer'])
		df.to_csv('qna.csv',mode='a',header=False,index=False)
		#break
	except Exception as e:
		print(c,'skipped',e)
		traceback.print_exc(file=sys.stdout)
#print(soup)


