###### Juntos Assignment
###### Author: Josuel Musambaghani
###### Email: <joshlixmus@gmail.com>
===

### Informations about the Program

- **Project Title: Concordance**
- **Overview**
A 'concordance' is an alphabetical list of the words present in a text with a count of how often each word appears and citations of where each word appears in the text (e.g. page number).

- **Example usage**
A concordance is used in books to show how many times each word occurs, and the specific location where the word may be found.
- **Getting Started**
The main language used in this project is ***Python***. The repository (on GitHub) containing the code for the project is called **Juntos** and the python file itself in the repository is called `JosuelJuntos.py`. 
- **Design Goals**
The goal of our project is to write a code that will be  able to get input from one file (in my case, I used a `.txt` file), to read and manipulate data from the input, and at the end, the code must write, in an empty file, an ordered (sorted) list of words that shows the number of occurences and the specific location of the word at each occurence.  
- **Detailed Usage**
In this project, we assumed that data from the input file are simple; they only contain punctuation marks and spaces. 
As talking about punctuations, it is to be noted that a library called `nltk` had to prealably be installed in the directory for our python compiler to deal with punctuation marks.  

### Formatting

The program (the code itself) is structured into three parts: 

1. Part 1: **Getting data from the user** (From the first file)

After importing the necessary modules (`nltk` and `string`), this part prompts the user to enter a file name from which data should be read.

Once data are accessed, the operation `nltk.sent_tokenize(text)` breaks the data into elements with resect to punctuations marks. The output here is a list of strings, each string representing a sentence from the input file. 

##### Note: 

- The `nltk` module needs to prealably installed in the PC (directory) for the code to run.
- The `nltk` presents some weaknesses when it comes to sequence sentences containing parenthesis. This minor issue were solved in the next part (Manipulating data).

2. Part 2: **Manipulating data**

This part essentially does three main tasks:
* Firstly, the code solve the issue of the `nltk`'s weakness faced to parenthesis.
* Secondly, it eliminate punctuations that might complicate  the count of words' occurences.
* Thirdly, the part count appearances of each word and stores it in a dictionary. 
    

3. Part 3: Results: **Writing ouptput to the second file.**

This last part focuses on three main tasks: 
- It sort by key every word in the dictionary called `myDict`
- Next, the code prompts the user to enter the name of a file where to write the ouptut. 
- And then, finally the code writes the results in the file entered by the user.

### Supporting documentation

The project mainly used `for` loops. Outside documentations did not apply. 
However, some materials were helpful to double-check some skills that may have been forgotten about libraries and modules. We have:
* ***Think Python***: a book by Allen B. Downey 
    - Link: <http://www.greenteapress.com/thinkpython/>
* Notes from my Python Class
    - Link <http://glassy-filament-680.appspot.com/> 


