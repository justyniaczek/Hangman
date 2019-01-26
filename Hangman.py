import random
HANGMAN= ("""
        _____
        |   |
        |
        |
       _|_

         """,
        """
        _____
        |   |
        |   O
        |
        |
       _|_

        """,
        """
          _____
         |    |S
         |    O
         |    |
         |
        _|_

        """,
        """
         _____
        |    |
        |    O
        |   /||
        |
       _|_
          """,
          """
        _____
       |    |
       |    O
       |   /||
       |   / |
      _|_
                   """)

MAX_TRIES= len(HANGMAN) -1
WORDS= ("MIETEK", "MASAKRA", 'SPLENDOR', 'PAPUGA')
print(len(WORDS))
word= random.choice(WORDS)
guessed= "-"*len(word)
wrong=0
used=[] # pusta tablica liter które użytkownik próbował zgadnąć

print(" \tZAGRAJMY W GRĘ")
while wrong< MAX_TRIES and word!=guessed:
    print(HANGMAN[wrong])
    print("wykorzystane litery:", used)
    print ("Słowo:", guessed)
    guess= input("wprowadz litere")
    guess=guess.upper()
    while guess in used:
        print("wykorzystales juz ta litere", guess)
        guess = input("wprowadz litere")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("Litera znajduje sie w słowie")
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new +=guess
            else:
                new+=guessed[i]
        guessed=new
    else:
        print("Ta litera",guess, "nie wystepuje w słowie")
        wrong+=1
    if wrong== MAX_TRIES:
        print("KonieC gry! Prawidłowe słowo to: ", word)
    else:
        print("Gratulacje! Słowo to: ", guess)