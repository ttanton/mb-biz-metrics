# Run Metrics 
# run_metrics.py
#
# Retrieves necessary data and saves them as html files locally. Mines local html files for metric data. For now, retrieves new archive files for every run.

import icgadmin as mb
import getpass
import ga
from datetime import date
import pprint

def get_icg(day, month, year_current, year_past):
	
	## Retrieve and Save ################################################
	
	r = mb.gain_authentication()
	opener = r[0]
	url = r[1]
	mb.get_month_sales(url, month, month, opener, day, year_current,'mtd')		#Current Month Sales
	mb.get_month_sales(url, 1, month, opener, day, year_current, 'ytd') 		#Current YTD Sales
	mb.get_month_sales(url, month, month, opener, day, year_past,'mtd')		#Past Month Sales
	mb.get_month_sales(url, 1, month, opener, day, year_past, 'ytd')		#Past YTD Sales

	mb.get_month_profit(url, month, month, opener, day, year_current, 'mtd')	#Current Month Profit
	mb.get_month_profit(url, 1, month, opener, day, year_current, 'ytd')		#Current YTD Profit
	mb.get_month_profit(url, month, month, opener, day, year_past, 'mtd')		#Past Month Profit
	mb.get_month_profit(url, 1, month, opener, day, year_past, 'ytd')		#Past YTD Profit

	mb.get_month_product(url, month, month, opener, day, year_current, 'mtd')	#Current Month Products
	mb.get_month_product(url, 1, month, opener, day, year_current, 'ytd')		#Current YTD Products
	mb.get_month_product(url, month, month, opener, day, year_past, 'mtd')		#Past Month Products
	mb.get_month_product(url, 1, month, opener, day, year_past, 'ytd')		#Past YTD Products
	

	## Operations & Analysis #############################################

	vendors = ['NoVendor','Amazon','Amazon-FBA']
	export_list = []	#Ordered List of each box value for spreadsheet
	i = ''			#Place holder of For loop thru vendors

	print "Extracting initial Data"
	current_ytd_sales = mb.mine_getSalesData('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
	current_mtd_sales = mb.mine_getSalesData('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
	past_ytd_sales = mb.mine_getSalesData('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
	past_mtd_sales = mb.mine_getSalesData('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

	current_ytd_ref = mb.mine_getSalesRefund('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
	current_mtd_ref = mb.mine_getSalesRefund('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
	past_ytd_ref = mb.mine_getSalesRefund('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
	past_mtd_ref = mb.mine_getSalesRefund('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

	current_ytd_profit = mb.mine_getProfitData('archive/' + str(year_current) + 'ytd_profit_' + i + '.html')
	current_mtd_profit = mb.mine_getProfitData('archive/' + str(year_current) + 'mtd_profit_' + i + '.html')
	past_ytd_profit = mb.mine_getProfitData('archive/' + str(year_past) + 'ytd_profit_' + i + '.html')
	past_mtd_profit = mb.mine_getProfitData('archive/' + str(year_past) + 'mtd_profit_' + i + '.html')

	print "Mining Overall Revenue Data"
	# YTD Past Total Revenue
	export_list.append(sum(past_ytd_sales[3]) - sum(mb.makeNum(past_ytd_ref[3])))
	# YTD Current Total Revenue
	export_list.append(sum(current_ytd_sales[3]) - sum(mb.makeNum(current_ytd_ref[3])))
	# MTD Past Total Revenue
	export_list.append(sum(past_mtd_sales[3]) - sum(mb.makeNum(past_mtd_ref[3])))
	# MTD Current Total Revenue
	export_list.append(sum(current_mtd_sales[3]) - sum(mb.makeNum(current_mtd_ref[3])))
	
	print "Mining Overall Profit Data"
	# YTD Past Total Profit
	export_list.append(mb.makeNum(past_ytd_profit))
	# YTD Current Total Profit
	export_list.append(mb.makeNum(current_ytd_profit))
	# MTD Past Total Profit
	export_list.append(mb.makeNum(past_mtd_profit))
	# MTD Current Total Profit
	export_list.append(mb.makeNum(current_mtd_profit))
	print "Mining Overall Orders Data"
	# YTD Past Total Orders
	export_list.append(sum(past_ytd_sales[2]))
	# YTD Current Total Orders
	export_list.append(sum(current_ytd_sales[2]))
	# MTD Past Total Orders
	export_list.append(sum(past_mtd_sales[2]))
	# MTD Current Total Orders
	export_list.append(sum(current_mtd_sales[2]))

	# For loop to extract revenue data for vendors (site, amazon, and amazon-fba)
	for i in vendors:
		print "Mining Revenue Data for Vendor: " + i
		current_ytd_sales = mb.mine_getSalesData('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
		current_mtd_sales = mb.mine_getSalesData('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
		past_ytd_sales = mb.mine_getSalesData('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
		past_mtd_sales = mb.mine_getSalesData('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

		current_ytd_ref = mb.mine_getSalesRefund('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
		current_mtd_ref = mb.mine_getSalesRefund('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
		past_ytd_ref = mb.mine_getSalesRefund('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
		past_mtd_ref = mb.mine_getSalesRefund('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')
		
		# YTD Past Total Revenue
		export_list.append(sum(past_ytd_sales[3]) - sum(mb.makeNum(past_ytd_ref[3])))
		# YTD Current Total Revenue
		export_list.append(sum(current_ytd_sales[3]) - sum(mb.makeNum(current_ytd_ref[3])))
		# MTD Past Total Revenue
		export_list.append(sum(past_mtd_sales[3]) - sum(mb.makeNum(past_mtd_ref[3])))
		# MTD Current Total Revenue
		export_list.append(sum(current_mtd_sales[3]) - sum(mb.makeNum(current_mtd_ref[3])))

	i = 'NoVendor'	# Change New Datasets to Site Only
	print "Mining Profit Data for Vendor: " + i
	# YTD Past Site Profit
	export_list.append(mb.makeNum(mb.mine_getProfitData('archive/' + str(year_past) + 'ytd_profit_' + i + '.html')))
	# YTD Current Site Profit
	export_list.append(mb.makeNum(mb.mine_getProfitData('archive/' + str(year_current) + 'ytd_profit_' + i + '.html')))
	# MTD Past Site Profit
	export_list.append(mb.makeNum(mb.mine_getProfitData('archive/' + str(year_past) + 'mtd_profit_' + i + '.html')))
	# MTD Past Site Profit
	export_list.append(mb.makeNum(mb.mine_getProfitData('archive/' + str(year_current) + 'mtd_profit_' + i + '.html')))

	current_ytd_sales = mb.mine_getSalesData('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
	current_mtd_sales = mb.mine_getSalesData('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
	past_ytd_sales = mb.mine_getSalesData('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
	past_mtd_sales = mb.mine_getSalesData('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

	print "Mining Order Data for Vendor: " + i
	# YTD Past Site Orders
	export_list.append(sum(past_ytd_sales[2]))
	# YTD Current Site Orders
	export_list.append(sum(current_ytd_sales[2]))
	# MTD Past Site Orders
	export_list.append(sum(past_mtd_sales[2]))
	# MTD Current Site Orders
	export_list.append(sum(current_mtd_sales[2]))

	current_ytd_site_product = mb.mine_getProductData('archive/' + str(year_current) + 'ytd_product_' + i + '.html')
	current_mtd_site_product = mb.mine_getProductData('archive/' + str(year_current) + 'mtd_product_' + i + '.html')
	past_ytd_site_product = mb.mine_getProductData('archive/' + str(year_past) + 'ytd_product_' + i + '.html')
	past_mtd_site_product = mb.mine_getProductData('archive/' + str(year_past) + 'mtd_product_' + i + '.html')

	print "Mining Product Data for Vendor: " + i
	# YTD Past Site Products
	export_list.append(sum(mb.makeNum(past_ytd_site_product[1])))
	# YTD Current Site Products
	export_list.append(sum(mb.makeNum(current_ytd_site_product[1])))
	# MTD Past Site Products
	export_list.append(sum(mb.makeNum(past_mtd_site_product[1])))
	# MTD Current Site Products
	export_list.append(sum(mb.makeNum(current_mtd_site_product[1])))

	return export_list

def get_ga(d, m, yc, yp):	
	
	day = format(d, '02')
	month = format(m, '02')
	
	###################################################################
	## Grabbing Google Analytics Data #################################

	# Define the auth scopes to request.
	scope = ['https://www.googleapis.com/auth/analytics.readonly']

	# Use the developer console and replace the values with your
	# service account email and relative location of your key file.
	service_account_email = '764727577979-8f2hs2kgononjmp5hon4kbachecil7ju@developer.gserviceaccount.com'
	key_file_location = 'GA_client_secrets.p12'

	# Authenticate and construct service.
	service = ga.get_service('analytics', 'v3', scope, key_file_location, service_account_email)
	profile = "11464615" 

	ga_data = []

	mtd_sd_now = str(yc) + "-" + str(month) + "-01"
	mtd_ed_now = str(yc) + "-" + str(month) + "-" + str(day)
	mtd_sd_pas = str(yp) + "-" + str(month) + "-01"
	mtd_ed_pas = str(yp) + "-" + str(month) + "-" + str(day)
	ytd_sd_now = str(yc) + "-01-01"
	ytd_ed_now = str(yc) + "-" + str(month) + "-" + str(day)
	ytd_sd_pas = str(yp) + "-01-01"
	ytd_ed_pas = str(yp) + "-" + str(month) + "-" + str(day)
	
	## Pull & append Conv Rate & Total Traffic from GA ##################
	metrics = ["ga:goal1ConversionRate","ga:sessions"]
	for m in metrics:
		ga_data.append(float(ga.get_results(service, profile, mtd_sd_pas, mtd_ed_pas, m).get('rows')[0][0]))
		ga_data.append(float(ga.get_results(service, profile, mtd_sd_now, mtd_ed_now, m).get('rows')[0][0]))
		ga_data.append(float(ga.get_results(service, profile, ytd_sd_pas, ytd_ed_pas, m).get('rows')[0][0]))
		ga_data.append(float(ga.get_results(service, profile, ytd_sd_now, ytd_ed_now, m).get('rows')[0][0]))
	
	## Pull & append direct, organic, email, and cpc from GA ############
	met = "ga:transactionRevenue"
	dim = "ga:medium"
	a = []
	a.append(ga.get_results_wdim(service, profile, mtd_sd_pas, mtd_ed_pas, met, dim).get('rows'))
	a.append(ga.get_results_wdim(service, profile, mtd_sd_now, mtd_ed_now, met, dim).get('rows'))
	a.append(ga.get_results_wdim(service, profile, ytd_sd_pas, ytd_ed_pas, met, dim).get('rows'))
	a.append(ga.get_results_wdim(service, profile, ytd_sd_now, ytd_ed_now, met, dim).get('rows'))
	
	mediums = ["(none)", "organic", "cpc", "email"]
	temp = []
	for i in a:
		for med in mediums:
			tot = 0
			for j in i:
				if j[0].lower() == med.lower():
					tot = tot + float(j[1])
			temp.append([med, tot])	
	for i in range(0,4):
		for j in range(0,4):
			index = i+(j*4)
			ga_data.append(temp[index][1])
			
	return ga_data

def main():
	
	print "\n\nGet Metrics\nRetrieve pages and save locally\n---------------------------------"

	## Initial Inputs ###################################################

	month = int(raw_input('Month of Analysis (4,10): '))
	year_current = date.today().year
	year_past = year_current - 1
	day = 0

	# Determine intToDay from input
	# intToDay should be 1 day before current date
	if int(date.today().month) == month:
		day = date.today().day - 1
	elif month in [4,6,9,11]:
		day = 30
	elif month == 2:
		day = 28
	else:
		day = 31

	print "Analyzing for month " + str(month) + " of " + str(year_current) + " thru " + str(month) + "/" + str(day) + "/" + str(year_current) + "\n"
	
	icg_data = get_icg(day, month, year_current, year_past)
	ga_data = get_ga(day, month, year_current, year_past)
	
	
	###################################################################
	## Export plugNchug Data to CSV ###################################
	print "Exporting plugNchug data to CSV"
	icg_data = map(str, icg_data)
	outFile = open('plugNchug.csv', 'w')
	for j in icg_data:
		outFile.write(j + '\n')
	for j in ga_data:
		outFile.write(str(j) + '\n')
	print "Done!\n\n"


if __name__ == '__main__':
  main()