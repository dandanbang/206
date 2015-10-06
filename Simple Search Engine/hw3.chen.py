#---------------------------------------------------------
# <Daniel Wei-Hsuan Chen>
# <daniel@ischool.berkeley.edu>
# Homework #3
# September 29, 2015
# hw3.chen.py
#---------------------------------------------------------
from __future__ import print_function
import urllib2
import re
from sys import argv
import sys
import requests

def promptUser():
    userInput = str(raw_input("Search term?"))
    return userInput.lower()

def createDict(text):
	booknumber = 0
	titleList = []
	bookDict = {}
	for line in text:
		if (line != ''):
			bookDict[line.split(",")[0]] = booknumber, line.split(",")[1]
			titleList.append(line.split(",")[0])
		booknumber += 1
	return bookDict, titleList

def readBook(url):
	url = str(url)
	try:
	    urllib2.urlopen(url)
	except URLError as e:
	    if hasattr(e, 'reason'):
	        print ('We failed to reach a server.')
	        print ('Reason: ', e.reason)
	    elif hasattr(e, 'code'):
	        print ('The server couldn\'t fulfill the request.')
	        print ('Error code: ', e.code)
	except:
		print ("Unexpected error: Your file is probably formated wrong.", sys.exc_info()[0])
		raise
	else:
		html = urllib2.urlopen(url).read()
		return html

def clean(raw):
    list1 = []
    list2 = []
    for word in raw:
        list1.append("".join(s.lower() for s in word if not s.isdigit()))
    for word in list1:
        list2.append("".join(s for s in word if s.isalpha()))
    return [x for x in list2 if x]

def wordCount(bookDict, titleList):
	wordDict = {}
	wordCountList = []
	for titleNumber in range(len(titleList)):
		url = bookDict[titleList[titleNumber]][1]
		text = readBook(url)
		textSplit = re.split(r'[ \t\n]+', text)
		textSplitClean = clean(textSplit)
		for word in textSplitClean:
			if word not in wordDict:
				wordDict[word] = [0] * len(titleList)
				wordDict[word][titleNumber] = 1
			else:
				wordDict[word][titleNumber] = wordDict[word][titleNumber] + 1
	return wordDict

def search(wordDict, searchword, titleList, bookDict):
	if (searchword == 'catalog'):
		sortedDict = sorted(bookDict.items(), key=lambda bookDict: bookDict[1])
		for book in sortedDict:
			print(str(book[0]) + ' : ' + str(book[1]))
	elif (searchword == 'titles'):
		for title in titleList:
			print(title)
	elif searchword not in wordDict:
		print('The word ' + searchword + ' does not appear in any books in the library.')
	else:
		wordCountList = wordDict[searchword]
		dictionary = {}
		number = 0
		number2 = 1
		for title in titleList:
			dictionary[title] = wordCountList[number]
			number += 1
		sortedDict = sorted(dictionary.items(), key=lambda dictionary: dictionary[1], reverse = True)
		for book in sortedDict:
			if book[1] > 0:
				print (str(number2) + '. The word ' + str(searchword) + ' appears ' + str(book[1]) + ' times in ' + str(book[0]) + ' (link: ' + 
					bookDict[book[0]][1])
				number2 += 1

def main():
	filename = argv
	print ("Enter the file name to read:" )
	filename = raw_input("> ")
	try:
		with open(filename, "r") as file:
			loadedText = file.read()
			loadedText = loadedText.replace("\r","")
			splitText = re.split(r'[\t\n]+', loadedText)
			bookDict, titleList = createDict(splitText)
			wordDict = wordCount(bookDict, titleList)
		file.close()
	except IOError:
	    print ("Unable to open."), filename
	    print ("Bye!")
	    sys.exit()
	except:
	    print ("Unexpected error: Your file is probably formated wrong.", sys.exc_info()[0])
	    raise
	else:
		userInput = promptUser()
		while userInput != "terminate":
		    search(wordDict, userInput, titleList, bookDict)
		    userInput = promptUser()

if __name__ == "__main__":
    main()    