#config file for shonydanza searches

#REQUIRED
#shodan account API key

API_KEY = ''


#REQUIRED
#maximum number of results that will be returned per search
#default is 100

SEARCH_LIMIT = 100


#REQUIRED
#IPs exceeding the honeyscore limit will not show up in IP results
#adjust to desired probability to adjust results, or change to 1.0 to include all results

HONEYSCORE_LIMIT = 0.5


#REQUIRED - at least one key: value pair
#stock searches that can be selected from a menu
#add search to the dictionary to automatically add it to your shonydanza menu

STOCK_SEARCHES = {
'ANONYMOUS_FTP':'ftp anonymous ok',
'RDP':'port:3389 has_screenshot:true'
}


#OPTIONAL
#IP or cidr range constraint for searches that return list of IP addresses
#use comma-separated list to designate multiple (e.g. 1.1.1.1,2.2.0.0/16,3.3.3.3,3.3.3.4) 

#NET_RANGE = '0.0.0.0/0'
