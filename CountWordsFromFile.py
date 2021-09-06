def countWords():
    fileName = input("fileName")
    file = open(fileName,'r')
    words = 0
    for line in file:
        wordsarray = line.split()
        words = words+len(wordsarray)
    print("total number of words are")
    print(words)
     

countWords()