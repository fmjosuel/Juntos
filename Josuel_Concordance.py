# Josuel Musambaghani
# Juntos Assignment - CONCORDANCE
# ==============================================================================
''' PROMPT: ASSIGNMENT
A 'concordance' is an alphabetical list of the words present in a text with a
count of how often each word appears and citations of where each word appears
in the text (e.g. page number). Write a program - in the programming language
of your choice - that will generate a concordance of an arbitrary text document
written in English: the text can be read from stdin, and the program should
output the concordance to stdout or a file. For each word, it should print the
count and the sorted list of citations, in this case the zero-indexed sentence
number in which that word occurs. You may assume that the input contains only
spaces, newlines, standard English letters, and standard English punctuation
marks.
'''
# ==============================================================================
# Libraries to be used
# ------------------------------------------------------------------------------

import nltk             # this module needs to prealably be installed. 
import string           # this available module helps to deal with punctuations

# ------------------ PART 1 : GETTING DATA FROM THE USER -----------------------

from_file=str(raw_input("Enter the name of the file to read: "))
# c:/Python27/fileIn.txt

# Openining the file as a list of sentences in the text file (Each sentence is a string)
with open(from_file, 'r') as in_file:
    text = in_file.read()
    f = nltk.sent_tokenize(text)

# ------------------ PART 2 : MANIPULATING DATA --------------------------------

# This part deals with parenthesis. The nltk does not consider parenthesis when
# sequencing sentences.Example of what this for loop does:
# ["I was ill (not totally.", "Just a bit)"] --> ["I was ill (not totally. Just a bit)"]
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

    for item in string.punctuation:
            line = [elt for elt in line if elt != item]
    
    for word in line:
            
        # this next part eliminate eventual punctuations that might be
        # appended to words. For example 'english.' --> 'english'.
        # This makes the count realistic with no repeated words.
        
        for elt in word[len(word)-2:]:
            if word.count(".") >= 2:            # for example 'e.g.' must be kept as such
                continue
            elif elt in string.punctuation:
                word = word.replace(elt, "")    # for example 'file.' becomes 'file'

        for elt in word[:1]:
            if elt in string.punctuation:
                word = word.replace(elt, "")    # for example '(assume' becomes 'assume'

        word = word.strip()
        word = word.lower()

        # this next if statement append word by word in the dictionary.
        if not word in myDict:
            myDict[word] = []
        myDict[word].append(linenum)

# ------------------ PART 3 : RESULTS: WRITING THE OUTPUT TO FILE 2 ------------

to_file = str(raw_input("Enter the name of the file to write: "))
# c:/Python27/fileOut.txt

text1 = "%-15s %5s  %s" %("Word", 'Count', "Line Numbers")
text2 = "%-15s %5s  %s" %("====", '=====', "============")

# this part write the ouptut in the file entered by the user
with open(to_file, 'w') as Out_file:
    text1 = Out_file.write(text1)
    Out_file.write("\n")
    text2 = Out_file.write(text2)
    Out_file.write("\n")

    for key in sorted(myDict):
        text3 = '%-15s %5d: %s' % (key, len(myDict[key]), myDict[key])
        Out_file.write(text3)
        Out_file.write("\n")

    Out_file.close()
    
# ==============================================================================
# ------------------- this is the END of the assignment ------------------------
