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
" \nYOU MUST GUESS MY SECRET WORD🔮")
wordList = list("orange")

guess = input("please guess one letter of the secret word: ")
