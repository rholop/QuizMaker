# This section gives the user some introduction to what the program is all about
print('Welcome!')
print()
print("This program will let you make a fun quiz with a few simple steps. The quiz is a personality style quiz, so each"
      " answer choice maps to one specific result. The result with the most matching answers will be printed for the"
      " user.\n"
      "   1. Name your program (Ex: ‘Which Star Trek Character are You?’)\n"
      "   2. Give a description of your quiz that’ll print at the top (Ex: ‘This quiz will tell you whether you’re most"
      " like Spock, Captain Kirk, Scotty, or Bones.’)\n"
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
questions = int(input('How many questions do you want your quiz to have? '))
print()


# Some variables for later
result_names = []  # Creates a list to store the result names
answer_choices = []  # Creates a list to store letters (a, b, etc.) for later quiz formatting
user_answers = []  # Creates a list to store the users answers (a, b, etc.)
question_answer_dictionary = {}  # Creates a dictionary to store the inputted questions and answers
result_description = {}  # Creates a dictionary to store the optional result descriptions


# This loop populates the answer choices list with letters
choice = 'a'  # Creates a variable so our loop starts at little a
for r in range(results):
    answer_choices.append(choice)
    choice = chr(ord(choice) + 1)  # The 'chr' and 'ord' functions allow us to count up from a to b and so on


# This loop asks the user to describe each possible answer choice
has_dscrpt = ''  # Creates an empty variable for the loop to modify
for r in range(1, results + 1):
    print(f'What do you want result #{r} to be? ', end='')
    result = input()
    result_names.append(result)
    if r == 1:  # This if statement makes sure we don't ask the user if they want descriptions every iteration
        has_dscrpt = input('   Do you want to provide descriptions for your results? ("Y" for yes or "N" for no): ')
        while has_dscrpt != 'Y' and has_dscrpt != 'N':  # This makes sure the input is Y or N
            has_dscrpt = input('Invalid. Try again: ')  # If neither, keeps asking the user to try again
        if has_dscrpt == 'N':  # If the user doesn't want the description, we just delete the empty dictionary
            del result_description
    if has_dscrpt == 'Y':  # If yes, this adds to the dictionary, the description is the value and the result is key
        description = input(f'* Enter a description for {result}: ')
        result_description[result] = description
    print()


# This function lets us get the user's answer
def GetAnswer():
    ans = input('Your answer: ')
    if ans in answer_choices:  # If the answer is one of the acceptable letters, it adds that letter to our list
        user_answers.append(ans)
    else:
        print('Invalid answer.')  # Otherwise, tells the user to try again and returns to the function
        return GetAnswer()


# This function figures out which of the possible letter answers occurs the most in our answer list
def GetResultCount():
    counts = {
    }
    highest_count = 0
    final_output = ''
    for c in answer_choices:  # Maps each possible answer to an integer - the amount of times in appears in answer list
        counts[c] = user_answers.count(c)
    for key, value in counts.items():
        # Keeps replacing the highest count with the new highest number & assigns final output with the appropriate key
        if value > highest_count:
            final_output = key
            highest_count = value
        elif value == highest_count:  # If there's more than one equivalent 'top' answer, this will add it to our output
            final_output = final_output + ',' + key
    return final_output


# This function converts the small letter into unicode and then subtracts the base of "a' (97) from it so we can index
# our result list to find what the name of the winning result is
def GetResult(x):
    code = ord(x) - 97
    return result_names[code]


# This function takes the winning result's name and finds the value for it's key in our description dictionary
def GetDescription(x):
    return result_description[f'{x}']


# This loop populates our dictionary with tuples based on the amount of questions and answers the user selected, since
# the dictionary is not in order, we have to create keys that allow us to access everything in order
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


# Some formatting for the start of the quiz
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
print("                           Now let's start the quiz!")
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
print()
print(quiz_name)
print('  *', quiz_description)
print()
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
print()


# This loop prints out our questions and answers by accessing the dictionary using our tuple system and asks for the
# user to input their answer
for q in range(questions):
    answer_key = 'a'
    for r in range(results + 1):
        if r == 0:  # When r is 0, the dictionary result is a question so we format for that
            print(f'Question #{q + 1}:', question_answer_dictionary[(q, r)])
        else:  # Otherwise, it's an answer so we format for that
            print(f'{answer_key}. {question_answer_dictionary[(q, r)]}')
            answer_key = chr(ord(answer_key) + 1)  # Again this let's us start at a and go to b, etc
    GetAnswer()


# Formatting for the end
print()
print('... adding up your results...')
print()
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
print()


# This function call gives us the little letter that got the most answers
final_result = GetResultCount()


# This if, else statement addresses what happens if there is a "tie" between multiple answer choices
if ',' in final_result:
    # This checks for a comma in our string, since the GetResultCount function uses them join "tie" answers

    final_result_list = final_result.split(',')  # Makes a new list by splitting up the comma
    result_numbers = len(final_result_list)  # Counts the length of the list for further formatting

    print(f'You tied between {result_numbers} different results!')
    print()

    # For however many ties, calls the functions to print the results and descriptions if applicable
    for r in range(result_numbers):
        result_name = GetResult(final_result_list[r])
        print(f'Result #{r+1} is {result_name}!')
        if has_dscrpt == 'Y':
            print('    *', GetDescription(result_name))
            print()

# If no tie, prints the winning result
else:
    result = GetResult(final_result)
    print(f'Your result is {result}.')
    if has_dscrpt == 'Y':
        print('    *', GetDescription(result))

# More formatting
print()
print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')