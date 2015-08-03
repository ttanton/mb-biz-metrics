# Retrieves necessary data and saves them as html files locally
#
#
#


import cookielib
import urllib2
import urllib
from datetime import date


## FUNCTIONS ####################################

def month_sales(url, sm, em, opener, day, year, kind):
# sm:start month, em:end month, opener, day, year, kind:mtd or ytd	
	vendors = ['','NoVendor','Amazon','Amazon-FBA']
	sales_url = 'https://' + url + '/admin/monsterbrew-reports-sales-daily.cfm'
	
	for i in vendors:
		print 'Getting', sm, '/', year, 'sales report data for', i
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
		with open ('archive/' + str(year) + kind + '_sales_' + i + '.html', 'w') as fid:
			fid.write(resp)

def month_profit(url, sm, em, opener, day, year, kind):
# sm:start month, em:end month, opener, day, year, kind:mtd or ytd
	vendors = ['','NoVendor','Amazon','Amazon-FBA']
	sales_url = 'https://' + url + '/admin/monsterbrew-profit-report.cfm'
	
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

def month_product(url, sm, em, opener, day, year, kind):
# sm:start month, em:end month, opener, day, year, kind:mtd or ytd
	vendors = ['NoVendor']
	sales_url = 'https://' + url + '/admin/monsterbrew-reports.cfm'
	
	for i in vendors:
		print 'Getting', sm, '/', year, 'product report data for', i
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
		with open ('archive/' + str(year) + kind + '_product_' + i + '.html', 'w') as fid:
			fid.write(resp)

def gain_authentication(url, user, passw):
	admin_authentication_url = 'https://' + url + '/admin/login.cfm'

	#Store the login cookie and create an opener to hold them
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	#Admin Login Parameters
	payload = {
		'adminID': user,
		'strPassword': passw
		}
	#Encode the payload & request
	login_data = urllib.urlencode(payload)

	#Send/receive login request and data
	opener.open(admin_authentication_url, login_data)
	return opener

