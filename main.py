import random

wordList = ['panda','giraffe','bunny','elephant','cat','dog','leopard','banana']
SECRET = random.choice(wordList)
abstractString = "_" * len(SECRET)


counter = 0
win = False
guessList = []
limit = len(SECRET) + 3

print('Welcome to Hangman')
while counter < limit and win == False:

    print(abstractString)
    guess = input("Please enter your guess: ")

    if guess in guessList:
        print('You have already entered this letter!')
        continue

    if guess in SECRET:

        print('Correct')

        indexes = []
        for index in range(len(SECRET)):
            if SECRET[index] == guess:
                indexes.append(index)
        
        temp = list(abstractString)

        for index in indexes:
            temp[index] = guess

        abstractString = "".join(temp)

    if abstractString.find('_') == -1:
        win = True
        print("Congratulations, YOU WIN!")
        continue

    guessList.append(guess)
    counter += 1

if win == False:
    print("YOU LOST!")