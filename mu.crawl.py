from bs4 import BeautifulSoup
import requests

html = requests.get("http://mu.ac.in/portal/results/")
data = html.text
soup = BeautifulSoup(data,"html.parser")
search = soup.find_all(class_= "specials")
for i in search[3:4]:
	list = i.find_all("li")
	for x in list:
		print x.contents[1].string
	