########################################
# NATALIE MASSARO-KOON
# ROWAN HOLOP
#
# Introduction to Python: Final Project
#     * Quiz Builder - this program allows the user to build a quiz that can be taken afterwards!
#
# File 2/3 - Quiz function file
#
########################################


# This function lets us get the user's answer
def GetAnswer(answer_choices, user_answers):
    """Takes two parameters, lists 'answer_choices' and 'user_answers' to prompt the user to input an answer. The answer
        is then added to 'user_answers.'"""
    ans = input('Your answer: (Enter the corresponding letter, ex: a) ')
    if ans in answer_choices:  # If the answer is one of the acceptable letters, it adds that letter to our list
        user_answers.append(ans)
    else:
        print('Invalid answer.')  # Otherwise, tells the user to try again and returns to the function
        return GetAnswer(answer_choices, user_answers)
    print()


# This function figures out which of the possible letter answers occurs the most in our answer list
def GetResultCount(answer_choices, user_answers):
    """Takes two parameters, 'answer_choices' and 'user_answers.' This counts up the highest occurrence of answers in
        'user_answers' and outputs the most frequent result(s)."""
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
def GetResult(x, result_names):
    """Takes two arguments, the first should be the output(s) of the GetResultCount function and the second is the
        list 'result_names.' Converts the user's answer(s) from their letters to their descriptive names."""
    code = ord(x) - 97
    return result_names[code]


# This function takes the winning result's name and finds the value for it's key in our description dictionary
def GetDescription(x, result_description):
    """Takes two arguments, the first should be output(s) of the GetResult function and the second is the dictionary
        'result_description'. Provides the descriptions for each user result."""
    return result_description[f'{x}']


