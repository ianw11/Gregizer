name = 'Greg'
filename = "in.txt"

pronouns = {"i": 0, "me": 0, "my": 1, "i'm": 1}

with open(filename, 'r') as f:
   for line in f:
      words = line.split(' ')
      newline = ""
      for word in words:
         word = word.lower()
         
         if (word in pronouns):
            if (pronouns[word] == 1):
               newline += name + "'s "
            else:
               newline += name + " "
         else:
            newline += word + " "
      print(newline)