#get-words.py

# Reads a text file and writes unique words to a plaintext file, one word per line, in
# alphabetical order.
import codecs
import re
punct = re.compile('[\.,\?;:!\(\)\d]')
unique_words = []
with codecs.open('K132743-typography.txt', 'r', 'utf-8') as infile, codecs.open('/media/sf_RBSDigitalApproaches/output/Sophonisba_words.txt', 'w', 'utf-8') as outfile :
	text = infile.read()
	de_punc = re.sub(punct,'',text)
	split = de_punc.split(' ')
	for word in split :
		if word.strip() not in unique_words :
			unique_words.append(word.strip())
	for unique_word in sorted(unique_words) :
		outfile.write(unique_word + '\n')