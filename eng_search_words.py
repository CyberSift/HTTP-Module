# first, download "google-10000-english-usa-no-swears.txt" from https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears.txt
# this file contains a google generated wordlist of the most common english words used
# the below script simply randomly pciks words and puts them together, loosely simulating the way 
# users would (for example) submit common search terms into a website. Results are stored in the file "wordlist"

with open('google-10000-english-usa-no-swears.txt') as f:
    content = f.readlines()


content = [x.strip() for x in content] 

from random import randint

f = open('wordlist', 'w')


for i in range(0, 50000):

	pos1 = randint(0,len(content)-1)
        f.write(content[pos1]+'\n')

	pos1 = randint(0,len(content)-1)
	pos2 = randint(0,len(content)-1)
	f.write(content[pos1]+' '+content[pos2]+'\n')

	pos1 = randint(0,len(content)-1)
	pos2 = randint(0,len(content)-1)
	pos3 = randint(0,len(content)-1)
	f.write(content[pos1]+' '+content[pos2]+' '+content[pos3]+'\n') 


f.close()
