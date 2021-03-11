#Hangman

#given code
lives = 10 # = # of incorrect guesses
word = "orange"

#project brief
#if you guess a letter correct, it does NOT subtract a life
#if you guess incorrect, decrement lives.
#can the user guess all the letters before running out of lives

print("WELCOME TO \n💀HANGMAN.PY💀"+
"\n😱😟🤯😰🧟‍😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️♂️"+
"\n_ _ _ _ _ _ "+
" \nYOU MUST GUESS MY SECRET WORD🔮")
wordList = list(word)


while len(wordList) != 0:
    guess = input("Please guess a leter from my secret word: ")
    if guess =="correct": #TODO: the letter guessed DOES exist in the secret wordList
        #TODO: print the word with blanks on letters unguessed.
        #TODO: get us back to line 20 for another guess
    elsif guess=="allreadyguessedletter": #todo: the letter was already unguessed
        #TODO: get us back to line 20 for anoither Guess
    else : #TODO: guess is incorrect
        #TODO: decrement lives
        #TODO: print lives left
        #TODO: if lives<=0: break, you are out of lives
