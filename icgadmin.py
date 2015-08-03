# Retrieves necessary data and saves them as html files locally
# Accepts 2 datetime objects defining the start and end points for 
# date retrieval.
#
# 
#
#


import cookielib
import urllib2
import urllib
from datetime import date


## FUNCTIONS ####################################

def gain_authentication():
	admin_authentication_url = 'https://icgadmin.com/admin/login.cfm'

	#Store the login cookie and create an opener to hold them
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	#Admin Login Parameters
	payload = {
		'adminID': 'tyler',
		'strPassword': 'barley19'
		}
	#Encode the payload & request
	login_data = urllib.urlencode(payload)

	#Send/receive login request and data
	opener.open(admin_authentication_url, login_data)
	return opener

def sales(opener, start, end):
# Accepts 2 datetime objects for start and end points
	sales_url = 'https://icgadmin.com/admin/monsterbrew-reports-sales-daily.cfm'
	
	#vendors = ['','NoVendor','Amazon','Amazon-FBA']
	vendors = ['NoVendor'] #Selecting Site Only data
	
	for i in vendors:
		print 'Getting sales report data for ' + str(start) + " - " + str(end)
		payload = {
			'intFromMonth': int(start.month),
			'intFromDay': int(start.day),
			'intFromYear': int(start.year),
			'intToMonth': int(end.month),
			'intToDay': int(end.day),
			'intToYear': int(end.year),
			'vendorID': i,
			'submitForm': 'submit'
			}
		
		# Encode the payload & request
		date_data = urllib.urlencode(payload)
	
		# Send request
		resp = opener.open(sales_url, date_data).read()
		with open ('archive/monitor_sales_'+str(end.month)+str(end.year)+'.html', 'w') as fid:
			fid.write(resp)

def profit(sm, em, opener, day, year, kind):
# sm:start month, em:end month, opener, day, year, kind:mtd or ytd
	vendors = ['','NoVendor','Amazon','Amazon-FBA']
	sales_url = 'https://icgadmin.com/admin/monsterbrew-profit-report.cfm'
	
	for i in vendors:
		print 'Getting', sm, '/', year, 'profit report data for', i
		payload = {
			'intFromMonth': int(sm),
			'intFromDay': 1,
			'intFromYear': year,
			'intToMonth': int(em),
			'intToDay': day,
			'intToYear': year,
			'vendorID': i,
			'submitForm': 'submit'
			}
		
		# Encode the payload & request
		date_data = urllib.urlencode(payload)
	
		# Send request
		resp = opener.open(sales_url, date_data).read()
		#page_content = resp.read()
		with open ('archive/' + str(year) + kind + '_profit_' + i + '.html', 'w') as fid:
			fid.write(resp)

def product(opener, start, end):
# sm:start month, em:end month, opener, day, year, kind:mtd or ytd
	vendors = ['NoVendor']
	sales_url = 'https://icgadmin.com/admin/monsterbrew-reports.cfm'
	
	for i in vendors:
		print 'Getting', start.month, '/', start.year, 'product report data for', i
		payload = {
			'intFromMonth': start.month,
			'intFromDay': start.day,
			'intFromYear': start.year,
			'intToMonth': end.month,
			'intToDay': end.day,
			'intToYear': end.year,
			'vendorID': i,
			'submitForm': 'submit'
			}
		
		# Encode the payload & request
		date_data = urllib.urlencode(payload)
	
		# Send request
		resp = opener.open(sales_url, date_data).read()
		with open ('archive/monitor_product_' + str(start.month) + str(start.day) + '.html', 'w') as fid:
			fid.write(resp)
