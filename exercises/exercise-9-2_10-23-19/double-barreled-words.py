# Open function to open the file "leaves-of-grass.txt"
#%%
##from gutenberg.acquire import load_etext
##from gutenberg.cleanup import strip_headers
##from textblob import TextBlob

##text = strip_headers(load_etext(1322)).strip()
##blob = TextBlob(text)
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...' exercises\exercise-9-2_10-23-19\double-barreled-words.py
# This will save the text to a local .txt file in this directory.

##source = open('exercises/exercise-9-2_10-23-19/leavesofgrass.txt','w',encoding="utf-16",newline='\n')
##source.write(text)
##source.close()


#%%

source1  = open("exercises/exercise-9-2_10-23-19/prideandprejudice.txt","r") 
pride = source1.read()

source2  = open("exercises/exercise-9-2_10-23-19/leavesofgrass.txt","r") 
leave = source2.read()


import re

presult = re.findall(r'\w*-\w*', pride)
len(presult)
lresult = re.findall(r'\w*-\w*', leave)
len(lresult)
#%%
