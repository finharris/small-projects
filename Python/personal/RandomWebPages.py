import webbrowser
import time
import random

sites = ["google.com", "youtube.com", "pointless.com", "finharris.cf"]

# range
num1 = 1
num2 = 5

while True:
	chosensite = random.choice(sites)
	gotosite = "http://{}".format(chosensite)
	webbrowser.open(gotosite)
	time.sleep(random.randrange(num1, num2))