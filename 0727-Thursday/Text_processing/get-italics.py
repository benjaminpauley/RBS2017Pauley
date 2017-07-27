#get-italic-words.py

# If you're running this script on your RBSDigitalApproaches2017 virtual machine, you'll
# need to run first activate the web-scraping virtualenv:
# workon web-scraping
# If you are running the script on a different computer, you'll need the bs4 and lxml
# packages installed.
from bs4 import BeautifulSoup
import codecs
import lxml
import sys

reload(sys)
sys.setdefaultencoding('utf8')

with open('/media/sf_RBSDigitalApproaches/output/italic-words.txt','wb') as outfile :
	soup = BeautifulSoup(codecs.open('K132743.000-typography.xml', encoding = 'utf-8'), 'xml')
	italics = soup.find_all('hi')
	for italic in italics :
# 		print italic
		output = italic.string
# 		print italic.string
		outfile.write(unicode(output) + '\n')
outfile.close()