from itertools import repeat
import csv

twFile = open("testTweets.txt",'w')
with open('/home/vanshika/Downloads/Project3/test.tsv','rb') as tsvin :
    tsvin = csv.reader(tsvin, delimiter='\t')
    for i in tsvin:
	twFile.write(i[1]+'\n')

twFile.close()


