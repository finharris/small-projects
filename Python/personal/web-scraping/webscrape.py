from bs4 import BeautifulSoup
import requests
from summarizer import summarize
# Here, we're just importing both Beautiful Soup and the Requests library

page_link = "https://en.wikipedia.org/wiki/England"
# this is the url that we've already determined is safe and legal to scrape from.#

page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library

page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.

textContent = []

for tag in page_content.find_all('h2')[1:]:
    texth2=tag.text.strip()
    textContent.append(texth2)
    for item in tag.find_next_siblings('p'):
        if texth2 in item.find_previous_siblings('h2')[0].text.strip():
            textContent.append(item.text.strip())

for i in range(len(textContent)):
	textContent[i] = summarize("{}".format(i),textContent[i], count=2)

for i in range(len(textContent)):
	while True:
		try:
			if len(textContent[i+1]) == 1:
				# remove array i
			break
		except IndexError:
			break


with open('test.txt', 'w') as f:
	for item in textContent:
		while True:
			try:
				f.write("{}\n\n".format(item))
				break
			except UnicodeEncodeError:
				break
			except IndexError:
				break