"""String Manipulation"""
import re
import logging
import config4 as cfg

logging.basicConfig(
    filename="test4.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)
class TestA():
    """Parent Class"""
    #def __init__(self, filename):
     #   self.filename = filename
    filename = "inputfile4.txt"

    def readfile(self):
        """ Read file method"""
        inputfile = open(self.filename)       #pylint: disable=consider-using-with
        text = inputfile.read()
        text = text.split()
        return text

    def writefile(self, word):            #pylint: disable=no-self-use
        """ Write file method"""
        with open(Y, "a") as f_1:
            f_1.write(str(word) + "\n")
            f_1.close()

class TestB(TestA):   #pylint: disable=too-many-public-methods
    """Derived Class"""
    #def __init__(self, filename):
       # A.__init__(self, filename)

    def prefix(self):
        """ Find prefix method"""
        text = self.readfile()
        count = 0
        for i in text:
            if i.startswith('To'):
                count = count + 1
        self.printmeth(count)
        self.writefile(count)
        logging.info(count)
        return count

    def suffix(self):
        """ Find suffix method"""
        text = self.readfile()
        countsuff = 0
        for i in text:
            if i.endswith("ing"):
                countsuff = countsuff + 1
        self.printmeth(countsuff)
        self.writefile(countsuff)
        logging.info(countsuff)
        return countsuff
    def maximum(self):
        """ To find maximum occured word method"""
        text = self.readfile()
        word = ""
        maxcount = 0
        for i in range(0, len(text)):         #pylint: disable=consider-using-enumerate
            countm = 1
            for j in range(i + 1, len(text)):
                if text[i] == text[j]:
                    countm = countm + 1

            if countm > maxcount:
                maxcount = countm
                word = text[i]
        self.printmeth(word)
        self.writefile(word)
        logging.info(word)
        return word
    def palindrome(self):
        """ Find palindrome method"""
        text = self.readfile()
        pal = []
        for s_1 in text:
            s_2 = s_1[::-1]
            if s_2 == s_1 and s_1 != "":
                pal.append(s_1)
        self.printmeth(pal)
        self.writefile(pal)
        logging.info(pal)
        return pal
    def uniquewords(self):
        """ Find uniquewords method"""
        text = self.readfile()
        unique = []
        for word in text:
            if word not in unique:
                unique.append(word)
        self.printmeth(unique)
        self.writefile(unique)
        logging.info(unique)
        return unique
    def counterindex(self):
        """ Find counterindex method"""
        text = self.readfile()
        diction = {}
        diction = list(enumerate(text))
        self.printmeth(diction)
        self.writefile(diction)
        logging.info(diction)
        return diction
    def splitwords(self):
        """ Find splitwords method"""
        text = self.readfile()
        split = []
        for i in text:
            res = re.split('a|e|i|o|u', i)
            split.append(res)
        self.printmeth(split)
        self.writefile(split)
        logging.info(split)
        return split
    def capitalizecharacter(self):
        """ To capitilise third letter method"""
        text = self.readfile()
        cap = []
        for i in text:
            a_1 = list(i)
            a_1[2::3] = [x.upper() for x in a_1[2::3]]
            i = ''.join(a_1)
            cap.append(i)
        self.printmeth(cap)
        self.writefile(cap)
        logging.info(cap)
        return cap
    def capitalize5thword(self):
        """ To capitilise fifth word method"""
        text = self.readfile()
        for i in range(4, len(text), 5):
            text[i] = text[i].upper()
        self.printmeth(text)
        self.writefile(text)
        logging.info(text)
        return text
    def replacespace(self):
        """ To replace space with underscore method"""
        text = self.readfile()
        listtostr = ' '.join([str(i) for i in text])
        listtostr = listtostr.replace(" ", "_")
        self.printmeth(listtostr)
        self.writefile(listtostr)
        logging.info(listtostr)
        return listtostr
    def printmeth(self, x_1):          #pylint: disable=no-self-use
        """ Print method"""
        print(x_1)
    # def test_prefix(self):
    #     """ test prefix method"""
    #     t_1 = self.prefix()
    #     t_2 = 2
    #     assert t_1 == t_2
    # def test_suffix(self):
    #     """ test suffix method"""
    #     t_3 = self.suffix()
    #     t_4 = 2
    #     assert t_3 == t_4
    # def test_maxcount(self):
    #     """ test maxcount method"""
    #     t_5 = self.maximum()
    #     t_6 = "do"
    #     assert t_5 == t_6
    # def test_palindrome(self):
    #     """ test palindrome method"""
    #     t_6 = self.palindrome()
    #     t_7 = ['madam', 'mam']
    #     assert t_6 == t_7
    # def test_uniquewords(self):
    #     """ test uniquewords method"""
    #     t_8 = self.uniquewords()
    #     t_9 = ['Today', 'Tommorrow', 'pulling', 'pushing', 'do', 'madam', 'mam', 'the', 'then']
    #     assert t_8 == t_9
    # def test_counter(self):
    #     """ test counter method"""
    #     t_10 = self.counterindex()
    #     t_11 = [(0, 'Today'), (1, 'Tommorrow'), (2, 'pulling'), (3, 'pushing'), (4, 'do'),
    #             (5, 'do'),(6, 'do'), (7, 'madam'), (8, 'mam'), (9, 'the'), (10, 'then')]
    #     assert t_10 == t_11
    # def test_splitwords(self):
    #     """ test splitwords method"""
    #     t_12 = self.splitwords()
    #     t_13 = [['T', 'd', 'y'], ['T', 'mm', 'rr', 'w'], ['p', 'll', 'ng'], ['p', 'sh', 'ng'],
    #             ['d', ''], ['d', ''], ['d', ''], ['m', 'd', 'm'], ['m', 'm'],
    #             ['th', ''], ['th', 'n']]
    #     assert t_12 == t_13
    # def test_capitilise(self):
    #     """ test capitilise method"""
    #     t_14 = self.capitalizecharacter()
    #     t_15 = ['ToDay', 'ToMmoRroW', 'puLliNg', 'puShiNg', 'do', 'do', 'do',
    #             'maDam', 'maM', 'thE', 'thEn']
    #     assert t_14 == t_15

    # def test_capitilise5thword(self):
    #     """ test capitise fifth word method"""
    #     t_16 = self.capitalize5thword()
    #     t_17 = ['Today', 'Tommorrow', 'pulling', 'pushing', 'DO', 'do',
    #             'do', 'madam', 'mam', 'THE', 'then']
    #     assert t_16 == t_17

    # def test_replacespace(self):
    #     """ test replace space method"""
    #     t_18 = self.replacespace()
    #     t_19 = "Today_Tommorrow_pulling_pushing_do_do_do_madam_mam_the_then"
    #     assert t_18 == t_19

#obj = B("inputfile3.txt")
#x = cfg.names["inputfilename"]
obj = TestB()
Y = cfg.names["outputfilename"]

obj.prefix()
obj.suffix()
obj.maximum()
obj.palindrome()
obj.uniquewords()
obj.counterindex()
obj.splitwords()
obj.capitalizecharacter()
obj.capitalize5thword()
obj.replacespace()
