 # Declare some necessary variables #
questioncount = 0  # How many questions in total Default 0
corquestions = 0   # How many correct questions Default 0


 # Function to display and check questions #
def question(q, a1, a2, a3, cora):  # Make a function with all the arguments needed
    global questioncount  # Makes variable able to use in a subroutine by making it global
    questioncount += 1  # Adds one to the question count because the function has been called meaning there is a question
    print(q, "A:", a1, "B:", a2, "C:", a3)  # Prints the question options
    ans = str(input("What is your answer?\n\t")).lower()  # Asks for the users answer
    if ans == cora.lower():  # Checks the answer
        print("CORRECT! \n")
        global corquestions  # Makes variable able to use in a subroutine by making it global
        corquestions += 1  # Adds one to correct questions because the answer matched the imputed answer
    else:
        print("INCORRECT!")  # If it is incorrect

 # Write questions in this order question("Question", "Option a", "Option b", "Option c", "Correct option: A, B, C (or in lowercase)") #
question("What is the capital of france?", "London", "Paris", "Epre", "b")
question("What is 9 + 10?", "11", "19", "21", "c")
question("What is the correct way to call a function?", "func_name()", "()func_name", "func_name():", "a")
question("Whats the best song ever?", "Circles - Post Malone", "These Days - Rudimental", "Road Rage - Little T", "b")

 # Prints the statement of how many questions you got right out of how many. This changes based on if the amount of questions you got right is more than one. #
if corquestions == 1:  # If the correct question count is one then it shouldn't be plural questions
    print("You got", corquestions, "question right out of", questioncount)
else:  # If the correct question count is more than one then it should be plural questions
    print("You got", corquestions, "questions right out of", questioncount)
