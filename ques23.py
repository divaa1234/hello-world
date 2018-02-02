def isWordGuessed(secretWord, lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    my_String = ''
    for x in secretWord:
        if x in lettersGuessed:
            my_String += x
        else:
            my_String += '_'
    return my_String


def getAvailableLetters(lettersGuessed):
    notGuessed = ''
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x not in lettersGuessed:
            notGuessed += x
    return notGuessed


def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
                continue