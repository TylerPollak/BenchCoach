from bs4 import BeautifulSoup
import csv
import urllib, urllib2

# r = urllib.urlopen('http://www.baseballpress.com/lineups').read()
# soup = BeautifulSoup(r, 'html.parser')
# for link in soup.find_all('a'):
# 	print(link.get('href'))

# Helper function for text
def send_text(numstring, message):
    data = urllib.urlencode({'number': numstring, 'message': message})
    r = urllib2.urlopen("http://textbelt.com/text", data)
    return r.getcode(), r.read()

#Open your roster
f = open('roster.csv', 'rbU')
IDlist = []

try:
	reader = csv.reader(f)
	for row in reader:
		IDlist.append([row[0], row[1], ""])
finally:
	f.close()


url = 'http://crunchtimebaseball.com/master.csv'
response = urllib.urlopen(url)
MLBlist = csv.reader(response)


for row in MLBlist:
	for x in range(0, len(IDlist)):
		if row[1] in IDlist[x]:
			print IDlist[x][0]



#print send_text(xxx, "lasttest")




# for row in MLBlist:
# 	if 'Andrew Benintendi' in row:
# 		print "mlb_id is: " + row[0] + " and mlb_name is: " + row[1]





# Use CSV file to get the mlb_id from your team's players, then go to baseballpress lineup to see if that mlb_id is somewhere in the page.  if not, then send text
