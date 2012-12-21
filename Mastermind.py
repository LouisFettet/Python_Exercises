# Louis Fettet
# Mastermind Game
# 11/4/11

from random import choice,sample

colors = ['R', 'O', 'Y', 'G', 'B', 'I', 'V', 'W']

def mastermind(Computer, Length, N):
    """
    Computer is True when the computer chooses the code.  The code is 
    pf length Length chosen from a set of N colours. 
    The function returns True when the computer wins and False otherwise.
    """
    print ("Hello, I am Hal, I like to play mastermind.  Thank you for playing with me.")
    while True:    
        if Computer == True:
            rules = input("If you would like to read the rules and input instructions, please type 'RULES', else press return. : ")
            if rules.lower() == "rules":
                print("I will generate a code of length " + str(Length) + " and of a certain set of colors.  Once I generate this code, you will be able to start making guesses.  When you make a guess, make sure you input it like so: 'RBYG'." )
            print("I am choosing a code ... (thinking...)")
            code = ""
            colorset = sample(colors, N)
            for i in range(Length):
                code = code + choice(colorset)
            print("OK. I am ready.  The color choice is " + str(colorset))               
            guessleft = Length*N*1//2
            for i in range(guessleft):
                guess = input("What code do you choose? (You have " + str(guessleft - i) + " guesses left.) ")     
                if guess == code:
                    print("Congratulations! You win! YEAH YOU'RE AWESOME!!!")
                    break
                if len(guess) is not Length:
                    guessleft += 1
                    print("Please input your answer in the correct format.")
                else:
                    correct = 0
                    for i in range(Length):
                        if code[i] == guess[i]:
                            correct += 1                        
                    print("You have " + str(correct) + " colors in the correct positions.")
            playagain = input("Would you like to play again? (Y/N): ")
            if playagain == "Y":
                quit
            else:
                break
        else:
            colorset = sample(colors,N)
            rules = input("Please think of a code of length " + str(Length) + " and of colors " + str(colorset) + ". If you would like to read the syntax rules, type 'RULES', else press return.: ")
            if rules.lower() == "rules":
                print("""Okay, I will start guessing codes. When I guess a code, you must type either 'YES' or an integer depending on whether or not the code is correct.  If the code is incorrect, the integer you give me should be the number of colors I have in the correct positions.""")
            guessleft = Length * N * 1 // 2
            codelist = []
            for i in range(guessleft):
                code = ""
                for i in range(Length):
                    code = code + choice(colorset)
                if code in codelist:
                    continue
                else:
                    codelist.append(code)
                guess = input("Is " + code + " your code? ")
                if guess == "YES":
                    print ("I win!")
                    break
                else:
                    quit
            playagain = input("Would you like to play again? (Y/N): ")
            if playagain == "Y":
                quit
            else:
                break
