# Author: Josuel Musambaghani

# library that breaks text into parts
# note that the module nltk needs to be installed first in the directory

import nltk
import string

from_file=str(raw_input("Enter the name of the file to read: "))
# c:/Python27/fileIn.txt

with open(from_file, 'r') as in_file:
    text = in_file.read()
    f = nltk.sent_tokenize(text)

# This code deals with the proble of parenthesis
for item in range(len(f)-1):
	if '(' in f[item] and ')' in f[item+1]:
		f[item] += ' ' + f[item+1]
		f.remove(f[item+1])


# count and display results of counted words
myDict = {}
linenum = -1

for line in f:
    line = line.strip()
    line = line.lower()
    line = line.split()
    linenum += 1
    for word in line:
###################################################
# Trying to eliminate punctuations that are appended to words
        if word in string.punctuation:
            line.remove(word)

        for elt in word[len(word)-2:]:
            if "e.g." in word:
                continue
            elif elt in string.punctuation:
                word = word.replace(elt, "")

        for elt in word[:1]:
            if elt in string.punctuation:
                word = word.replace(elt, "")        

###################################################
# the code continues as normal ...

        word = word.strip()
        word = word.lower()

        if not word in myDict:
            myDict[word] = []
        myDict[word].append(linenum)


to_file = str(raw_input("Enter the name of the file to write: "))
# c:/Python27/fileOut.txt

text1 = "%-15s %5s  %s" %("Word", 'Count', "Line Numbers")
text2 = "%-15s %5s  %s" %("====", '=====', "============")


with open(to_file, 'w') as Out_file:
    text1 = Out_file.write(text1)
    Out_file.write("\n")
    text2 = Out_file.write(text2)
    Out_file.write("\n")
    #text3 = Out_file.write(text3)


    for key in sorted(myDict):
        text3 = '%-15s %5d: %s' % (key, len(myDict[key]), myDict[key])
        Out_file.write(text3)
        Out_file.write("\n")

    Out_file.close()


