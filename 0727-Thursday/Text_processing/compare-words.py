#compare-words.py
import codecs

dictwords = []
with codecs.open('EMOP-dict.txt', 'r', 'utf-8') as dictfile :
	for line in dictfile :
		dictwords.append(line)
dictfile.close()
sophwords = []
with codecs.open('/media/sf_RBSDigitalApproaches/output/Sophonisba_words.txt', 'r', 'utf-8') as sophtext :
	for line in sophtext :
		sophword = line.strip('\n')
		if sophword not in dictwords :
			sophwords.append(sophword)
sophtext.close()
with codecs.open('/media/sf_RBSDigitalApproaches/output/Sophonisba-user-words.txt', 'w', 'utf-8') as outfile :
	for sophword in sophwords :
		print('Thinking...')
		if sophword not in dictwords :
			outfile.write(sophword + '\n')

outfile.close()