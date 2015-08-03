# Mines local html files for metric data
#
#
#


from bs4 import BeautifulSoup

## FUNCTIONS ####################################

def getHeaders(infile):
	html_doc = open(infile).read()
	soup = BeautifulSoup(html_doc.replace('iso-8859-1', 'utf-8'))
	table = soup.findAll("table", {"cellpadding":"3","border":"1"} )
	header = []
	data = []

	for t in table:
		rows = t.findAll('tr')				#Holds Each Row of data
		entries = (len(rows)-3)/3			#Number of Days of data
	
		head = rows[0].findAll('td')			#Capture Header Data 
		for j in range(0, len(head)):
				a = str(head[j]).split("<strong>")
				b = str(a[1]).split("</strong>")
				header.append(b[0])
	return header						#Returns string list of header data for infile

def getSalesData(infile):
	html_doc = open(infile).read()
	soup = BeautifulSoup(html_doc.replace('iso-8859-1', 'utf-8'))
	table = soup.findAll("table", {"cellpadding":"3","border":"1"} )
	data = []
	sales = []

	for t in table:
		rows = t.findAll('tr')				#Holds Each Row of data
		entries = (len(rows)-3)/3			#Number of Days of data
		head = rows[0].findAll('td')			#Capture Header Data 
		for j in range(0, len(head)):
				data.append([])

		for i in range (2, len(rows)-2, 3):		#Determine lines with Purchase Data
			columns = rows[i].findAll('td') 	#Holds Each Column of Data of Row i
			count = 0
			for j in range(0, len(columns)):
				a = str(columns[j]).split(">")
				b = str(a[1]).split("<")
				d = b[0]			#Capture Data stripped of HTML code
				data[count].append(d)
				count = count + 1
	sales = data[:2]
	for i in data[2:]:
		sales.append(makeNum(i))	
	return sales						#Returns String Matrix of per day sales data for infile
	
def getSalesRefund(infile):
	html_doc = open(infile).read()
	soup = BeautifulSoup(html_doc.replace('iso-8859-1', 'utf-8'))
	table = soup.findAll("table", {"cellpadding":"3","border":"1"} )
	data = []

	for t in table:
		rows = t.findAll('tr')				#Holds Each Row of data
		entries = (len(rows)-3)/3			#Number of Days of data
		head = rows[0].findAll('td')			#Capture Header Data 
		for j in range(0, len(head)):
				data.append([])

		for i in range (3, len(rows)-2, 3):		#Determine lines with Purchase Data
			columns = rows[i].findAll('td') 	#Holds Each Column of Data of Row i
			count = 0
			for j in range(0, len(columns)):
				a = str(columns[j]).split(">")
				b = str(a[1]).split("<")
				d = b[0]			#Capture Data stripped of HTML code
				data[count].append(d)
				count = count + 1
		
	return data						#Returns String Matrix of per day refund data for infile

def getProfitData(infile):
	html_doc = open(infile).read()
	soup = BeautifulSoup(html_doc.replace('iso-8859-1', 'utf-8'))
	table = soup.findAll("table", {"cellpadding":"3","border":"1"} )
	profit = ''

	for t in table:
		rows = t.findAll('tr')				#Holds Each Row of data
		head = rows[0].findAll('td')			#Capture Header Data 
		columns = rows[3].findAll('td')
		a = str(columns[7]).split(">")
		b = str(a[1]).split("<")
		d = b[0]					#Capture Data stripped of HTML code
		profit = d
	return profit						#Returns string of profit value from infile

def getProductData(infile):
	html_doc = open(infile).read()
	soup = BeautifulSoup(html_doc.replace('iso-8859-1', 'utf-8'))
	table = soup.findAll("table", {"cellpadding":"2","border":"1"} )
	data = []
	
	for t in table:
		rows = t.findAll('tr')				#Holds Each Row of data
		entries = (len(rows)-3)/3			#Number of Days of data
		head = rows[1].findAll('td')			#Capture Header Data 
		for j in range(0, len(head)):
				data.append([])

		for i in range (2, len(rows)-1):		#Determine lines with Product Data
			columns = rows[i].findAll('td') 	#Holds Each Column of Data of Row i
			count = 0
			for j in range(0, len(columns)):
				a = str(columns[j]).split(">")
				b = str(a[1]).split("<")
				d = b[0]			#Capture Data stripped of HTML code
				data[count].append(d)
				count = count + 1
	return data						#Returns String Matrix of product data for infile

def makeNum(old):
	if isinstance(old, list):
		new = []
		for i in old:
			j = i.replace("$","")
			k = j.replace(",","")
			new.append(float(k))
		return new					#Returns list in float type

	elif isinstance(old, str):
		j = old.replace("$","")
		k = j.replace(",","")
		new = float(k)
		return new					#Returns float

