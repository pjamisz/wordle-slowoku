# wordle-slowoku
Project for PPY university course. Wordle-like command line game in Polish for 5-letter long words using dictionary from sjp.pl (CC-BY 4.0))
1. Files
  main.py - Main script with whole game logic, opens "words_five_letters.txt"
  words_five_letters.txt - text file consisting of all five letter words in polish,
       generated in dictionary.py by filtering from dictionary of polish words from sjp.pl (Licence CC-BY 4.0)
  dictonary.py - filters dictionary slowa.txt, leaving only 5-letter words, not necessary to run the game
  slowa.txt - list of all polish words according to sjp.pl, not included here as the file is too big

2. How to run: Download main.py and words_five_letters.txt
    python3 -m main.py
