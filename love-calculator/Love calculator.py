# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53



def calculate_love_score(name1, name2):
    name1=name1.lower()
    name2=name2.lower()

    names = name1+name2

    x = names.count("t")+names.count("r")+names.count("u")+names.count("e")            

    y = names.count("l")+names.count("o")+names.count("v")+names.count("e")

    score = str(x)+str(y)
    print(score)   

calculate_love_score("angela yu","jack bauner")

