import sys
import re
#words prefixed with to
s=input(("Enter the file name"))
f= open(s)
text = f.read()
text=text.split()
count=0
for i in text:
    if(i.startswith('to')):
        count=count+1
#words ending with ing
countsuffix=0
for i in text:
    if(i.endswith('ing')):
        countsuffix=countsuffix+1
#most repeated word
countm = 0;
word = "";
maxCount = 0;
for i in range(0, len(text)):
    countm = 1;
    for j in range(i + 1, len(text)):
        if (text[i] == text[j]):
            countm = countm + 1;


    if (count > maxCount):
        maxCount = countm;
        word = text[i];
#palindrome
out=[]
for s in text:
    s1=s[::-1]
    if s1==s and s1!="":
        out.append(s1)
#unique words
distinct_words = []
for l in text:
    if l not in distinct_words:
        distinct_words.append(l)
#counter with vaues
dict={}
dict=(list(enumerate(text,1)))
#split the words based on vowels
out1=[]
for i in text:
    res=re.split('a|e|i|o|u',i)
    out1.append(res)
print(str(out1))
#Capitalise 3rd letter
words=[]
for third_word in text:
    a=list(third_word)
    a[2::3]=[x.upper() for x in a[2::3]]
    i = ''.join(a)
    words.append(i)
print(words)

#Capitilise 5th word
for i in range(4,len(text),5):
    text[i]=text[i].upper()
print(text)
# Use – in place of blank space
w=" "
w=w.join(text)
w=w.replace(" ","_")
print(w)
with open("outputfile", "w") as f:
    f.write("The no of words that ends with ing:"+str(countsuffix))
    f.write("The no of words that is prefixed with to:" + str(count))
    f.write("The most repeated word is:"+word)
    f.write("palindrome words are"+str(out))
    f.write("unique words are:"+str(distinct_words))
    f.write("counter with values"+str(dict))

