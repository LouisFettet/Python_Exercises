# Fettet, Louis
# Statistics on Famous Books
# 10/7/11

def readBook(filename):
   """
   Open filename, which is the name of a file containing a book
   in text format and returns a structure containing all words
   and their frequencies.
   """
   myfile = open(filename)
   mydict = {}
   wordlist = ()
   while (True):
       line = myfile.readline()
       if len(line) > 0:
          line = line.split()
          for word in line:
             word = word.strip(',.!?;:()$#"/-*')
             if word.endswith("'s"):
                word = word[:-2]
             if word.isupper():
                word = word.lower()
             if word.istitle():
                word = word.lower()
             if len(word) >= 5:
                if word in mydict:
                   mydict[word] += 1
                else: mydict[word] = 1
       else:
           break
   print (("Most Used Words of {0}").format(filename[:-4]))
   print ("{0:<10} {1:>12}".format("Word", "Frequency"))
   print ("-" * 23)
   wordlist=sorted(mydict, key=mydict.get, reverse=True)
   for i in wordlist[:20]:
      j = mydict[i]
      print ("{0:<10} {1:>12}".format(i, j))
   print ("-" * 23)

def twentyK():
   """
   Returns the 20 most used words and their frequencies of the book Twenty
   Thousand Leagues Under the Sea by Jules Verne.
   """
   return readBook("20k.txt")
