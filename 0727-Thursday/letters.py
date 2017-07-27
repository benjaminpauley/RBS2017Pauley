#letters.py

import csv
import re
import glob
from PIL import Image
import os
import sys
import argparse
reload(sys)
sys.setdefaultencoding('utf-8')


parser = argparse.ArgumentParser(description='Define input (folder of TIFF/box pairs) and output folder for resulting glyphs.')
parser.add_argument('-i', action='store', dest='source', help='Give path to TIFF file or folder of TIFFs')
parser.add_argument('-o', action='store', dest='destination', help='Give path to desired destination for output glyphs')
	
args = parser.parse_args()

source = args.source
destination = args.destination

if not os.path.isdir(destination) :
	os.makedirs(destination)

print('Working on TIFF files in ' + source + '...')
for filename in glob.glob(source + '/*.tif') :
	filename_root = filename.rstrip('.tif')
	print('\tFound TIFF file ' + filename)
	boxfile_name = filename.rstrip('.tif') + '.box'
	print('\tFound boxfile ' + boxfile_name)
	number = re.compile('\d+')
	pagenum = re.findall(number,filename)[0]

	im = Image.open(filename)
	height = im.height
	
	if os.path.isfile(boxfile_name) :
		print('Opening ' + boxfile_name)
		with open(boxfile_name, "rb") as boxfile :	
			reader = csv.reader(boxfile, delimiter=' ', quotechar='"')
			print('Reading ' + boxfile_name)
			for row in reader :
				print('Reading row...')
				char = row[0].encode('unicode_escape')
				x1 = int(row[1])
				y1 = height - int(row[2])
				x2 = int(row[3])
				y2 = height - int(row[4])
				w = x2 - x1
				h = y2 - y1

				if re.findall('e6',char) :
					char = 'u00e6'
				elif char == '\u2019' :
					char = 'apostrophe'
				elif char == '\u201C' :
					char = 'lquot'
				elif char == '\u201D' :
					char = 'rquot'
				elif re.findall('\u',char) :
					char = char.replace('\\','')
				elif char == "~" :
					char = 'tilde'
				elif char == '.' :
					char = 'period'
				elif char == ',' :
					char = 'comma'
				elif char == ':' :
					char = 'colon'
				elif char == ';' :
					char = 'semicolon'
				elif char == '!' :
					char = 'exclamation'
				elif char == '(' :
					char = 'lparen'
				elif char == ')' :
					char = 'rparen'
				elif char == '-' :
					char = 'hyphen'
				elif char == '?' :
					char = 'question'

				upper = re.compile('[A-Z]')
				lower = re.compile('[a-z]')
				punct = re.compile('tilde|period|comma|colon|semicolon|apostrophe|quot|exclamation|lparen|rparen|hyphen|question')
				if re.findall(punct, char) :
					char = char
				elif re.findall(upper, char) :
					char = 'Upper-' + char
				elif re.findall(lower, char) :
					char = 'lower-' + char
				
				if not os.path.isdir(destination + '/' + char) :
					os.mkdir(destination + '/' + char)
					
				letter = im.crop((float(x1),float(y2),float(x2),float(y1)))
				letter_filename = char + '-' + str(pagenum) + '-' + str(x1) + '-' + str(y2) + '-' + str(x2) + '-' + str(y1) + '.tif'
				letter.save(destination + '/' + char + '/' + letter_filename)
				print('Writing ' + letter_filename)
				letter.close()
	# 			
			boxfile.close()
			im.close()
