#Hangman

#given code
lives = 7# = # of incorrect guesses
word = "apple"

#project brief
#if you guess a letter correct, it does NOT subtract a life
#if you guess incorrect, decrement lives.
#can the user guess all the letters before running out of lives


wordList = list(word)

def hello():
    print("😱😟🤯😰🧟‍😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️♂️"+
    "\nWELCOME TO \n💀HANGMAN.PY💀"+
    "\n😱😟🤯😰🧟‍😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️♂️"+
    "\n_ _ _ _ _  "+
    " \nYOU MUST GUESS MY SECRET WORD🔮")

def getRevealedString(guessSet):
    revealed = ""
    for letter in wordList:
        if letter in guessSet:
            revealed += letter+" "
        else:
            revealed+= "_ "
    return revealed

hello()
guessSet = set([])

while lives >= 0:
    guess = input("Please guess a leter from my secret word: ")
    if guess in wordList:#guess =="correct":
        print("CORRECT :)")
    else: #guess is incorrect
        lives -=1
        print("this letter does not exist in my secret word.")
        print("LIVES REMAINING: {}".format(lives))

        if lives<=0 :
            print("😱😟🤯😰🧟‍😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️"+
            "\n💀you lost! 💀"+
            "\n😱😟🤯😰🧟‍😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️😱😟🤯😰🧟‍♂️")
            break
    guessSet.add(guess.lower())
    revealed = getRevealedString(guessSet)
    if revealed == "a p p l e ":
        print("🤩💃💎🤩💃💎🤩💃💎🤩💃💎"+
        "\nyou win!"+
        "\n🤩💃💎🤩💃💎🤩💃💎🤩💃💎")
        break
    print(revealed)
