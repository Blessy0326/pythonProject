try:
 f= open('myfile')

 text = f.read()

 text = text.lower()
 words = text.split()
 words = [word.strip('.,!;()[]') for word in words]
 words = [word.replace("'s", '') for word in words]

 distinct_words = []
 for word in words:
    if word not in distinct_words:
        distinct_words.append(word)

 distinct_words.sort(key=len)
 with open("output", "w") as f1:
  for l in distinct_words:
   f1.write(l+str(len(l))+" ");
except ValueError:
   print("Value error occured")
except (TypeError, ZeroDivisionError):
   print("Divided by 0 or type exception occured")
except IOError:
    print("IO exception occured")
except NameError:
    print("Invalid variable")
except:
    print("Some other exception has occured")



