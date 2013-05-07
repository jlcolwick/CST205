import random
import calendar
from datetime import date
import string
import operator
import re
from urllib.request import urlopen

# This function will print out the HTML file that creates the word cloud
# The first parameter is the full text of the body of the page
# The second parameter is the title
def printHTMLfile(body,title):
    # Fill in the full path to the html page you'd like to create
    fd = open('results.html','wt')
    theStr="""
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    <address></address>
    </body> </html>
    """
    fd.write(theStr)
    fd.close()

# This function makes the box that contains the word cloud
# To change how your box displays, change some of the values
# For example, changing the width value will change how wide
# the box appears on your screen.  You can also change the background
# color and the border.  If you like you can add additional styles as well
def makeHTMLbox(body):
    boxStr = """<div style=\"
    width: 600px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\">%s</div>
    """
    return boxStr % (body)



def makeHTMLword(word,cnt,high,low, wordColor):
    ''' make a word with a font size to be placed in the box. Font size is scaled
    between htmlBig and htmlLittle (to be user set). high and low represent the high 
    and low counts in the document. cnt is the cnt of the word 
    '''
    htmlBig = 120
    htmlLittle = 45
    ratio = (cnt-low)/float(high-low)
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    wordStr = '<span style=\"font-size:%spx; color:'+str(wordColor)+'\">%s </span>'
    return wordStr % (str(fontsize), word)




def generateWordle():
  #response = urlopen("http://localhost:8888/text/speech.txt")
  #page_source = response.read()

  text = open("speech.txt", "rt").read()

  text = text.lower()
  #text = filter(str.isalnum, string.printable)
  #text = text.replace('-', ' ')
  tokenList = text.split()
  
  #printNow(tokenList)
  
  dictionary = {}
  
  for x in tokenList:
    if x in dictionary:
      dictionary[x] = dictionary[x] + 1
    else:
      dictionary[x] = 1



  
  
  

# In another function in your program you will need to set the high and low
# count for your source (you can have your program figure these out for you
# like we did in the Green Eggs and Ham lab)
  highCount=80
  lowCount=5
# Initialize the body to an empty string
  body=''
 
# For each word, call makeHTMLword and append the results to teh body string
# The parameters to makeHTMLword are:
# (1) The word, (2) the count for the word, (3) the highest and (4) lowest word counts
# in the document and (5) the color to use for the word in the word cloud
  keys = dictionary.keys()

  for key in keys :
    body = body + makeHTMLword(key,dictionary[key],highCount,lowCount, "#006600")

# After you have built the body string, call makeHTMLbox and printHTMLfile
# Check your results in a browser and tweak your code until you get a word cloud
# that you like
  box = makeHTMLbox(body)
  printHTMLfile(box,'testfile.html')

generateWordle()