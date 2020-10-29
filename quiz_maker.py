########################################
# NATALIE MASSARO-KOON
# ROWAN HOLOP
#
# Introduction to Python: Final Project
#     * Quiz Builder - this program allows the user to build a quiz that can be taken afterwards!
#       1. First the program will display the instructions for the person using it
#       2. Then, the program will ask the user to name their quiz and give it a description
#       3. Then, the program asks the user how many possible results they want to their quiz to have and how many
#       questions
#       4. Then using the number the user selected for possible results, the program will ask them to give each result
#       a name and will also ask if they want to add descriptions
#       5. After the results are named, the program will go through and ask for names for each question based on how
#       many questions the user originally said they wanted
#           - Each question will also generate and ask for corresponding answer choices for each result
#       6. After everything for the quiz has been collected from the user, the program will write a series of files
#           - One file will hold the quiz itself
#           - Another holds the names of the possible answers
#           - Another holds the list of answer choices a-whatever
#           - Another will hold the descriptions of the results if those were created
#           - Another will hold the variable that says there will be user descriptions
#
# File 1/3 - Quiz maker file
#
########################################

from colorama import Fore

result_names = []  # Creates a list to store the result names
answer_choices = []  # Creates a list to store letters (a, b, etc.) for later quiz formatting
result_description = {}  # Creates a dictionary to store the optional result descriptions
if_description = ''

print('Welcome!')
print()
print(
    "This program will let you make a fun quiz with a few simple steps. The quiz is a personality style quiz, so "
    "each answer choice maps to one specific result. The result with the most matching answers will be printed for "
    "the user.\n"
    "   1. Name your program (Ex: ‘Which Star Trek Character are You?’)\n"
    "   2. Give a description of your quiz that’ll print at the top (Ex: ‘This quiz will tell you whether you’re "
    "most like Spock, Captain Kirk, Scotty, or Bones.’)\n"
    "   3. Tell the program how many possible results you want (Ex: 4)\n"
    "   4. Tell the program how many questions you want\n"
    "   5. Tell the program what each of your four results are named (Ex: ‘Spock, Captain Kirk, Scotty, Bones’)\n"
    "   6. Decide whether you want to enter descriptions for each of your results. These will print at the end for "
    "the user to read.\n"
    "   7. Enter your questions and corresponding answer choices.")
print()
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')

# This asks the user to give the quiz a name and description and assigns it to corresponding variables
quiz_name = input('What do you want the name of your quiz to be? ')
quiz_description = input('* Tell the user what your quiz is about: ')
print()

# This asks the user to decide how many possible results or answers the quiz will have and how many questions
results = int(input('How many possible results do you want? (This will also determine how many answer choices each '
                    'question has.) '))
while results < 1:
    results = input('Please type in a valid number of questions. ')


questions = int(input('How many questions do you want your quiz to have? '))
print()

# Some variables for later
question_answer_dictionary = {}  # Creates a dictionary to store the inputted questions and answers

# This loop populates the answer choices list with letters
choice = 'a'  # Creates a variable so our loop starts at little a
for r in range(results):
    answer_choices.append(choice)
    choice = chr(ord(choice) + 1)  # The 'chr' and 'ord' functions allow us to count up from a to b and so on

# This loop asks the user to describe each possible answer choice
for r in range(1, results + 1):
    print(f'What do you want result #{r} to be? ', end='')
    result = input()
    result_names.append(result)
    if r == 1:  # This if statement makes sure we don't ask the user if they want descriptions every iteration
        if_description = input('   Do you want to provide descriptions for your results? ("Y" for yes or "N" for no): ')
        while if_description != 'Y' and if_description != 'N':  # This makes sure the input is Y or N
            if_description = input('Invalid. Try again: ')  # If neither, keeps asking the user to try again
        if if_description == 'N':  # If the user doesn't want the description, we just delete the empty dictionary
            del result_description
    if if_description == 'Y':  # If yes, this adds to the dictionary, the description is the value and the result is key
        description = input(f'* Enter a description for {result}: ')
        result_description[result] = description
    print()

# This loop populates our dictionary with tuples based on the amount of questions and answers the user selected,
    # since the dictionary is not in order, we have to create keys that allow us to access everything in order
for q in range(questions):
    for r in range(results + 1):
        if r == 0:  # Questions are stored when r is zero
            print(f'What do you want Question #{q + 1} to be? ', end='')
            question = input()
            question_answer_dictionary[(q, r)] = question
        else:  # Answers are stored in the same 'q' value as their questions
            print(f'* Enter an answer for {result_names[r - 1]}: ', end='', )
            question_ans = input()
            question_answer_dictionary[(q, r)] = question_ans
    print()

# Here we will write the quiz into a new file for export to the quiz_reader program
f = open('the_quiz.txt', 'w')

# Some formatting for the start of the quiz
f.write('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n' + Fore.MAGENTA)
f.write(f'                            {quiz_name}\n' + Fore.LIGHTBLUE_EX)
f.write(f'                         {quiz_description}\n')
f.write(Fore.BLACK + 'To answer a question, type in the letter ( a, b, c, etc.) that corresponds to your answer!\n')
f.write('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n')
f.write('\n')

# This loop f.writes out our questions and answers by accessing the dictionary using our tuple system and asks for
# the user to input their answer
for q in range(questions):
    answer_key = 'a'
    for r in range(results + 1):
        if r == 0:  # When r is 0, the dictionary result is a question so we format for that
            ques = question_answer_dictionary[(q, r)]
            f.write(f'Question #{q + 1}: {question_answer_dictionary[(q, r)]}\n')
        else:  # Otherwise, it's an answer so we format for that
            f.write(f'{answer_key}. {question_answer_dictionary[(q, r)]}\n')
            answer_key = chr(ord(answer_key) + 1)  # Again this let's us start at a and go to b, etc

f.close()  # Close the file we wrote the quiz into

# This file will store our list "result_names" into a new file for use in the quiz_reader
p = open('result_names.txt', 'w')
for name in result_names:
    p.write(f'{name}\n')
p.close()

# This file will store our list "answer_choices" into a new file for use in the quiz_reader
c = open('answer_choices.txt', 'w')
for ans in answer_choices:
    c.write(f'{ans}\n')
c.close()

# This file will store our variable "if_description" into a new file for use in the quiz_reader
d = open('if_description.txt', 'w')
d.write(f'{if_description}')
d.close()

# If we made descriptions, we also write a new file to store the dictionary "result_description" for use in quiz_reader
if if_description == 'Y':
    rd = open('result_description.txt', 'w')
    for key, value in result_description.items():
        rd.write(f'{key}:')
        rd.write(f'{value}\n')
    rd.close()
