import requests #for making the request and getting http status code
import sys #for accepting arguments when called from terminal / command line
import time #for waiting between requests 

timeBetweenRequests = 30 #seconds
urlToCheck = sys.argv[1] #first argument is the script name, second is provided by user

if(urlToCheck[:4] != "http"):
	print("Please specify a url that starts with http or https")
	exit()

r = requests.get(urlToCheck)

if(r.status_code != 200):
	print("Got a status code of " + r.status_code)
	response = raw_input("Get notified when it's back up?   ")
	if (response[:1] == "y"):
		while(r.status_code != 200): #user must cancel with ctrl + c if it never comes back
			print("Status code is: " + r.status_code)
			r = requests.get(urlToCheck)
			time.sleep(timeBetweenRequests)
		print(urlToCheck + " responded with a 200. Exitting.")
		exit()
	else:
		print("Exitting...")
		exit()
else:
	print(urlToCheck + " responded with a http status code of 200, exitting.")
	exit()