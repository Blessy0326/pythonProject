import re
try:
 class test:
    def prefixTo(self,word):
        count = 0
        for i in word:
            if (i.startswith('to')):
                count = count + 1
        with open("output1.txt", "a") as f:
            f.write("The no of words that is prefixed with to:" + str(count)+"\n")
            f.close()
    def suffix(self,word):
        countsuffix = 0
        for i in word:
            if (i.endswith('ing')):
                countsuffix = countsuffix + 1

        with open("output1.txt", "a") as f:
            f.write("The no of words that is suffixed with ing:" + str(countsuffix)+"\n")
            f.close()

    def mostrepeated(self, word):
        countm = 0
        res = ""
        maxCount = 0
        for i in range(0, len(word)):
            countm = 1
            for j in range(i + 1, len(word)):
                if (word[i] == word[j]):
                    countm = countm + 1

            if (countm > maxCount):
                maxCount = countm
                res = text[i]
        with open("output1.txt", "a") as f:
            f.write("The most repeated word:" + res+"\n")
            f.close()
    def palidrome(self,word):
        out = []
        for s in word:
            s1 = s[::-1]
            if s1 == s and s1 != "":
                out.append(s1)
        with open("output1.txt", "a") as f:
            f.write("palindrome:" +str(out)+"\n")
            f.close()
    def uniquewords(self,word):
        distinct_words = []
        for l in word:
            if l not in distinct_words:
                distinct_words.append(l)
        with open("output1.txt", "a") as f:
            f.write("distinct words are:" +str(distinct_words)+"\n")
            f.close()
    def countervalues(self,word):
        dict = {}
        dict = (list(enumerate(word, 1)))
        with open("output1.txt", "a") as f:
            f.write("counter values:" + str(dict) + "\n")
            f.close()
    def splitvowels(self,word):
        out1 = []
        for i in word:
            result = re.split('a|e|i|o|u', i)
            out1.append(result)
        with open("output2.txt", "a") as f1:
            f1.write("split based on vowels:" + str(out1) + "\n")
            f1.close()
    def capitiliseThird(self,word):
        words = []
        for third_word in word:
            a = list(third_word)
            a[2::3] = [x.upper() for x in a[2::3]]
            i = ''.join(a)
            words.append(i)
        with open("output2.txt", "a") as f1:
            f1.write("Third letter capitalised:" + str(words) + "\n")
            f1.close()
    def fifthwordtoupper(self,word):
        for i in range(4, len(word), 5):
            word[i] = word[i].upper()
        with open("output2.txt", "a") as f1:
            f1.write("5th word capitilised:" + str(word) + "\n")
            f1.close()
    def blankspacetounderscore(self,word):
        w = " "
        w = w.join(word)
        w = w.replace(" ", "_")
        with open("output2.txt", "a") as f1:
            f1.write("After replacing space with _:" + w + "\n")
            f1.close()

 s=input(("Enter the file name:"))
 f= open(s)
 text = f.read()
 text=text.split()
 obj=test()
 obj.prefixTo(text)
 obj.suffix(text)
 obj.mostrepeated(text)
 obj.palidrome(text)
 obj.uniquewords(text)
 obj.countervalues(text)
 obj.splitvowels(text)
 obj.capitiliseThird(text)
 obj.blankspacetounderscore(text)
 obj.fifthwordtoupper(text)








except IOError:
    print("IO exception occured,file not found")