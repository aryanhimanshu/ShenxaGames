# Coding Challenge 3, hangman.py
# Name:
# Student No:

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    return random.choice(all_words)


# end of helper code
# -----------------------------------


def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    # TODO: Fill in your code here
    wordlist = []
    f = open("words.txt","r")
    if not f:
        print("Unable to open file")
        return wordlist
    print("Loading word list from file: words.txt")
    for line in f:
        for word in line.split(" "):
            wordlist.append(word)
    f.close()
    n = len(wordlist)
    print(str(n) + " words loaded.")
    return wordlist

# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function

# wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    # TODO: Fill in your the code here
    hassh = list(bytearray(26))
    for i in letters_guessed:
        num = ord(i) - 97
        hassh[num] = True
    
    n = len(word)
    for i in range(n):
        num = ord(word[i]) - 97
        if hassh[num] == False:
            return False
    return True

def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """
    # TODO: Fill in your code here
    progress = ""
    hassh = list(bytearray(26))
    for i in letters_guessed:
        num = ord(i) - 97
        hassh[num] = True
    
    n = len(guessword)
    for i in range(n):
        num = ord(guessword[i]) - 97
        if hassh[num] == True:
            progress += guessword[i]
        else:
            progress += "_ "
    return progress

def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here
    res = list(bytearray(26))
    for i in letters_guessed:
        num = ord(i) - 97
        res[num] = True
    rem = ""
    for i in range(26):
        if res[i] == False:
                rem += chr(i+97)
    return rem

def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    print("Welcome to Hangman Ultimate Edition")
    # TODO: Fill in your code here

    wordlist = load_words()
    n = len(wordlist)
    unichar = {}
    m = len(word)
    for i in range(m):
        unichar[word[i]] = 1
        
    unicount = len(unichar)
    print("Welcome to Hangman Ultimate Edition")
    letters_guessed = []
    flag = False
    
    
    lg = len(word)
    print("I am thinking of a word that is "+ str(lg) +" letters long")
    print("-------------")
    
    trial = 6
    
    letters_required = []
    for i in range(lg):
        letters_required.append(word[i])
    progress = get_guessed_word(word, letters_guessed)
    while(trial>0 and flag == False):
        print("You have "+ str(trial) + " guesses left.")
        remaining = get_remaining_letters(letters_guessed)
        alpha = input("Available letters: " + remaining +" Please guess a letter:")
        
        if alpha in letters_required:
            if alpha in letters_guessed:
                print("Oops! You've already guessed that letter:" + progress)
                print("------------")
            else:
                letters_guessed.append(alpha)
                progress = get_guessed_word(word, letters_guessed)
                print("Good guess: " + progress)
                print("------------")
                if is_word_guessed(word, letters_guessed):
                    print("Congratulations, you won!")
                    score = trial * unicount
                    print("Your total score for this game is: " + score)
                
        else:
            print("Oops! That letter is not in my word: " + progress)
            trial-=1
            print("------------")
        
    if not is_word_guessed(guessword, letters_guessed):
        print("Sorry, you ran out of guesses. The word was:" + word)
    
    




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    # Uncomment the line below once you have finished testing.
    # word = choose_random_word(wordlist)

    # Uncomment the line below once you have implemented the hangman function.
    hangman(word)
