# Author: Josuel Musambaghani

# library that breaks text into parts
import nltk
import string

with open('c:/Python27/fileIn.txt', 'r') as in_file:
    text = in_file.read()
    f = nltk.sent_tokenize(text)


# This code deals with the proble of parenthesis
for item in range(len(f)-1):
	if '(' in f[item] and ')' in f[item+1]:
		f[item] += ' ' + f[item+1]
		f.remove(f[item+1])

'''
# This code solve the problem of having punctuations appended to words
# when running. For example 'english:' and 'english' that might be consider
# as different because of the punctuation mark

punctuations = ['.', ':', ':', "'", ',', '...', '?', '!', '~']
g = []
for elt in f:
    for mark in punctuations:
        if mark in elt:
            z = elt.split(mark)
            new = z[0] + z[1]
            g.append(new)

print g

################################################################

for elt in f:
    for let in elt[len(elt)-2:]:
        if let in string.punctuation:
            elt = elt.replace(let, "")

for elt in f:
    for let in elt[:1]:
        if let in string.punctuation:
            elt = elt.replace(let, "")

print f

'''

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

print "%-15s %5s  %s" %("Word", 'Count', "Line Numbers")

print "%-15s %5s  %s" %("====", '=====', "============")

for key in sorted(myDict):
    print '%-15s %5d: %s' % (key, len(myDict[key]), myDict[key])

