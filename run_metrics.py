# Run Metrics 
# run_metrics.py
#
# Retrieves necessary data and saves them as html files locally. Mines local html files for metric data. For now, retrieves new archive files for every run.

import mine_metrics
import get_metrics
import getpass
from datetime import date

print "\n\nGet Metrics\nRetrieve pages and save locally\n---------------------------------"

## Initial Inputs ###################################################
url = raw_input('Domain URL (domain.com): ')
user = raw_input('Username: ')
passw = getpass.getpass('Password: ')
month = int(raw_input('Month of Analysis (4,10): '))
year_current = 2015
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


## Retrieve and Save ################################################

opener = get_metrics.gain_authentication(url, user, passw)
get_metrics.month_sales(url, month, month, opener, day, year_current,'mtd')		#Current Month Sales
get_metrics.month_sales(url, 1, month, opener, day, year_current, 'ytd') 		#Current YTD Sales
get_metrics.month_sales(url, month, month, opener, day, year_past,'mtd')		#Past Month Sales
get_metrics.month_sales(url, 1, month, opener, day, year_past, 'ytd')		#Past YTD Sales

get_metrics.month_profit(url, month, month, opener, day, year_current, 'mtd')	#Current Month Profit
get_metrics.month_profit(url, 1, month, opener, day, year_current, 'ytd')		#Current YTD Profit
get_metrics.month_profit(url, month, month, opener, day, year_past, 'mtd')		#Past Month Profit
get_metrics.month_profit(url, 1, month, opener, day, year_past, 'ytd')		#Past YTD Profit

get_metrics.month_product(url, month, month, opener, day, year_current, 'mtd')	#Current Month Products
get_metrics.month_product(url, 1, month, opener, day, year_current, 'ytd')		#Current YTD Products
get_metrics.month_product(url, month, month, opener, day, year_past, 'mtd')		#Past Month Products
get_metrics.month_product(url, 1, month, opener, day, year_past, 'ytd')		#Past YTD Products


## Operations & Analysis #############################################

vendors = ['NoVendor','Amazon','Amazon-FBA']
export_list = []	#Ordered List of each box value for spreadsheet
i = ''			#Place holder of For loop thru vendors

print "Extracting initial Data"
current_ytd_sales = mine_metrics.getSalesData('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
current_mtd_sales = mine_metrics.getSalesData('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
past_ytd_sales = mine_metrics.getSalesData('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
past_mtd_sales = mine_metrics.getSalesData('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

current_ytd_ref = mine_metrics.getSalesRefund('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
current_mtd_ref = mine_metrics.getSalesRefund('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
past_ytd_ref = mine_metrics.getSalesRefund('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
past_mtd_ref = mine_metrics.getSalesRefund('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

current_ytd_profit = mine_metrics.getProfitData('archive/' + str(year_current) + 'ytd_profit_' + i + '.html')
current_mtd_profit = mine_metrics.getProfitData('archive/' + str(year_current) + 'mtd_profit_' + i + '.html')
past_ytd_profit = mine_metrics.getProfitData('archive/' + str(year_past) + 'ytd_profit_' + i + '.html')
past_mtd_profit = mine_metrics.getProfitData('archive/' + str(year_past) + 'mtd_profit_' + i + '.html')

print "Mining Overall Revenue Data"
# YTD Past Total Revenue
export_list.append(sum(past_ytd_sales[3]) - sum(mine_metrics.makeNum(past_ytd_ref[6])))
# YTD Current Total Revenue
export_list.append(sum(current_ytd_sales[3]) - sum(mine_metrics.makeNum(current_ytd_ref[6])))
# MTD Past Total Revenue
export_list.append(sum(past_mtd_sales[3]) - sum(mine_metrics.makeNum(past_mtd_ref[6])))
# MTD Current Total Revenue
export_list.append(sum(current_mtd_sales[3]) - sum(mine_metrics.makeNum(current_mtd_ref[6])))
print "Mining Overall Profit Data"
# YTD Past Total Profit
export_list.append(mine_metrics.makeNum(past_ytd_profit))
# YTD Current Total Profit
export_list.append(mine_metrics.makeNum(current_ytd_profit))
# MTD Past Total Profit
export_list.append(mine_metrics.makeNum(past_mtd_profit))
# MTD Current Total Profit
export_list.append(mine_metrics.makeNum(current_mtd_profit))
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
	current_ytd_sales = mine_metrics.getSalesData('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
	current_mtd_sales = mine_metrics.getSalesData('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
	past_ytd_sales = mine_metrics.getSalesData('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
	past_mtd_sales = mine_metrics.getSalesData('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

	current_ytd_ref = mine_metrics.getSalesRefund('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
	current_mtd_ref = mine_metrics.getSalesRefund('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
	past_ytd_ref = mine_metrics.getSalesRefund('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
	past_mtd_ref = mine_metrics.getSalesRefund('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')
	
	# YTD Past Total Revenue
	export_list.append(sum(past_ytd_sales[3]) - sum(mine_metrics.makeNum(past_ytd_ref[6])))
	# YTD Current Total Revenue
	export_list.append(sum(current_ytd_sales[3]) - sum(mine_metrics.makeNum(current_ytd_ref[6])))
	# MTD Past Total Revenue
	export_list.append(sum(past_mtd_sales[3]) - sum(mine_metrics.makeNum(past_mtd_ref[6])))
	# MTD Current Total Revenue
	export_list.append(sum(current_mtd_sales[3]) - sum(mine_metrics.makeNum(current_mtd_ref[6])))

i = 'NoVendor'	# Change New Datasets to Site Only
print "Mining Profit Data for Vendor: " + i
# YTD Past Site Profit
export_list.append(mine_metrics.makeNum(mine_metrics.getProfitData('archive/' + str(year_past) + 'ytd_profit_' + i + '.html')))
# YTD Current Site Profit
export_list.append(mine_metrics.makeNum(mine_metrics.getProfitData('archive/' + str(year_current) + 'ytd_profit_' + i + '.html')))
# MTD Past Site Profit
export_list.append(mine_metrics.makeNum(mine_metrics.getProfitData('archive/' + str(year_past) + 'mtd_profit_' + i + '.html')))
# MTD Past Site Profit
export_list.append(mine_metrics.makeNum(mine_metrics.getProfitData('archive/' + str(year_current) + 'mtd_profit_' + i + '.html')))

current_ytd_sales = mine_metrics.getSalesData('archive/' + str(year_current) + 'ytd_sales_' + i + '.html')
current_mtd_sales = mine_metrics.getSalesData('archive/' + str(year_current) + 'mtd_sales_' + i + '.html')
past_ytd_sales = mine_metrics.getSalesData('archive/' + str(year_past) + 'ytd_sales_' + i + '.html')
past_mtd_sales = mine_metrics.getSalesData('archive/' + str(year_past) + 'mtd_sales_' + i + '.html')

print "Mining Order Data for Vendor: " + i
# YTD Past Site Orders
export_list.append(sum(past_ytd_sales[2]))
# YTD Current Site Orders
export_list.append(sum(current_ytd_sales[2]))
# MTD Past Site Orders
export_list.append(sum(past_mtd_sales[2]))
# MTD Current Site Orders
export_list.append(sum(current_mtd_sales[2]))

current_ytd_site_product = mine_metrics.getProductData('archive/' + str(year_current) + 'ytd_product_' + i + '.html')
current_mtd_site_product = mine_metrics.getProductData('archive/' + str(year_current) + 'mtd_product_' + i + '.html')
past_ytd_site_product = mine_metrics.getProductData('archive/' + str(year_past) + 'ytd_product_' + i + '.html')
past_mtd_site_product = mine_metrics.getProductData('archive/' + str(year_past) + 'mtd_product_' + i + '.html')

print "Mining Product Data for Vendor: " + i
# YTD Past Site Products
export_list.append(sum(mine_metrics.makeNum(past_ytd_site_product[1])))
# YTD Current Site Products
export_list.append(sum(mine_metrics.makeNum(current_ytd_site_product[1])))
# MTD Past Site Products
export_list.append(sum(mine_metrics.makeNum(past_mtd_site_product[1])))
# MTD Current Site Products
export_list.append(sum(mine_metrics.makeNum(current_mtd_site_product[1])))


## Export plugNchug Data to CSV ###################################
print "Exporting plugNchug data to CSV"
export_list = map(str, export_list)
outFile = open('plugNchug.csv', 'w')
for j in export_list:
	outFile.write(j + '\n')
print "Done!\n\n"

