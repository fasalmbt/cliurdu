import argparse
import requests
import lxml.html as lx

print('''
===============================================================
		    Cliurdu v1.0.0
	A simple cli based utility for urdu dictionary
===============================================================
''')

ap = argparse.ArgumentParser()
ap.add_argument('word')
args = ap.parse_args()
word = args.word
req = requests.get('https://www.rekhta.org/urdudictionary/?lang=1&keyword='+word)
parser = lx.fromstring(req.content)
hindi = ''.join(parser.xpath('//span[1]//bdi//text()'))
urdu = ''.join(parser.xpath('//span[2]//bdi//text()'))
english = ''.join(parser.xpath('//div[@class="rdotherlangSpeech clearfix"]//ul//li[1]//text()')).rsplit()[:3]
english = ''.join(english)
source = "https://www.rekhta.org/"
if hindi == '' or urdu == '' or english == '':
	hindi = "Not found"
	urdu = "Not found"
	english = "Not found"

print('''
Hindi   :	%s
Urdu    :	%s
Meaning :	%s
Source	:  	%s
===============================================================
	'''%(hindi, urdu, english, source))