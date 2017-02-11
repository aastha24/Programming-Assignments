word = input("Enter a word in English ")

while (not word.isalpha()):
    print ("You have not entered a word!")
    word = input("Enter a word in English ")   
    
first = word[0]
newword = word[1:len(word)] + first + 'ay'
    
print (newword) 