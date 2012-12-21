# Louis Fettet
# Flashcard Project
# 11/23/11

def run():
    print("Welcome to my Flashcard program.  This program can test your knowledge on a variety of subjects.")
    while (True):
        testChoice = input("What subject would you like to study? The current subjects supported by this program are PYTHON, U.S. CAPITALS, and MARTIAL ARTS. ")
        if testChoice.lower() == "u.s. capitals":
            myfile = open("uscaps.txt")
            break
        if testChoice.lower() == "python":
            myfile = open("python.txt")
            break
        if testChoice.lower() == "martial arts":
            myfile = open("taekwondo.txt")
            break
        else:
            print("Sorry, your input was invalid.  Please try again.")
    correct = 0
    incorrect = 0
    scorefile = open('scorefile.txt', 'w')
    question = []
    incq = []
    inca = []
    yourans = []
    for line in myfile:
        line = line.strip("\n")
        if line.startswith("---> Answer") == False:
            question.append(line)
        if line.startswith("---> Answer"):
            for i in question:
                print(i)
            b = input()
            nextline = myfile.__next__()
            answer = nextline.strip("\n")
            if b == answer:
                print ("Correct!")
                correct += 1
            else:
                print("Sorry, the correct answer was " + str(answer) + ".")
                incorrect += 1
                incq.append(question)
                inca.append(answer)
                yourans.append(b)
            question = []
    score=int(correct / (correct + incorrect) * 100)
    scorefile.write("Your score on flashcard quiz " + str(a) + " was " + str(score) +" out of 100.")
    scorefile.write("\nThe following questions were answered incorrectly:\n")
    for i in range(len(incq)):
        for j in incq[i]:
            scorefile.write("\n" + j)
        scorefile.write("\nYour answer was " + yourans[i] +".")
        scorefile.write("\nThe correct answer was " + inca[i] + ".")
    scorefile.close
    print("Congratulations, you finished the " + str(a) + " flashcard quiz! A text file will now open to show you your score.")
    import os
    os.startfile("scorefile.txt")
