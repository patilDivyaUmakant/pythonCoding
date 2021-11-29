import random
words = ["zodiac","kiwi","whistle","galaxy","pneumonia","fluffy","gossip","juicy","peekaboo","jelly",
"colonel","scissors","Mischievous","accommodate","accidentally","indispensable","jewelry",
"intelligence","immediate","humorous","guarantee","gauge","foreign","existence","experience",
"exhilarating","discipline","conscious","conscience","believe","acquired","justice"]

word = random.choice(words)
print (word)
print ("Guess the characters of the word, you have 12 chances !!")
guesses = ""
turns = 12
while turns > 0 :
    a = 0
    for char in word :
        if char in guesses :
            print(char)
        else :        
            print ("_")  
            a += 1
         
    if a == 0 :
        print ("Congratulations, You guessed the word correctly") 
        break

    guess = input("Guess a character of the word : ")
    guesses += guess
    if guess not in word :
        turns = turns - 1
        print ("Wrong, You have ",turns," turns left")
        if turns == 0 :
            print ("YOU LOSE , The word was ",word)
    else :
        print ("Your guess was right")

                