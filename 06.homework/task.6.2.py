while True:
    word = input("Enter a word that contains the letter 'h': ")
    if 'h' in word or 'H' in word:
        print("Thank you! You have entered the word:", word)
        break
    else:
        print("The word does not contain the letter 'h'. Try again.")