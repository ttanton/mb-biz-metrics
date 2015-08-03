# Mines local html files for metric data
#
#
#


from BeautifulSoup import BeautifulSoup


## FUNCTIONS ####################################


html_doc = open('102013_sales_.html', 'r')

soup = BeautifulSoup(html_doc, fromEncoding="ascii")
table = soup.find('table', attrs={"class": "normalfont","border": "1"})

d 		= []
data	= []	#[date, kind, tran, subt, tax, ship, tota]

for row in table.findAll('tr'):
	if len(row.findAll('td'))>6:
		date = row.findAll('td')[0].getText()
		kind = row.findAll('td')[1].getText()
		tran = row.findAll('td')[2].getText()
		subt = row.findAll('td')[3].getText()
		tax  = row.findAll('td')[4].getText()
		ship = row.findAll('td')[5].getText()
		tota = row.findAll('td')[6].getText()
		d.append([date, kind, tran, subt, tax, ship, tota])	

for i in range(2, len(d), 3):
	data.append(d[i])

print sum(float(data[6]))

## PROGRAM OPERATION ############################


