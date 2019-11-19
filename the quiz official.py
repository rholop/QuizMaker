# Creates empty spaces for users to put in titles and prompts
title = ' '
prompt = ' '

# Creates some empty spaces for future user options
a = ' '
b = ' '
c = ' '
d = ' '
e = ' '

# Creates some empty lists to keep track of answer counts
a_count = []
b_count = []
c_count = []
d_count = []
e_count = []

# Empty dictionary for future question inputs
questions = {
}

# Some more variables the main program will alter
answer_choices = 4
question_length = 5
user_answers = []
user_questions = []

# This if-else statement restates user_answers depending on how many answer choices the user selects
if answer_choices == 5:
    user_answers = ['a', 'b', 'c', 'd', 'e']
elif answer_choices == 4:
    user_answers = ['a', 'b', 'c', 'd']
elif answer_choices == 3:
    user_answers = ['a', 'b', 'c']
else:
    user_answers = ['a', 'b']

# This loop modifies the dictionary 'questions' to create the same number of keys as number of questions the user
# inputted. These keys are called 'question1', 'question2, etc. Each key is assigned a value of a new list.
# Then, the new list is populated with a-e, depending on the user's inputted number of answer choices. The values for
# each of these keys are arbitrarily assigned 'x' to be modified later.
for q in range(1, question_length+1):
    questions[f"question{q}"] = list({})
    for ans in user_answers:
        questions[f"question{q}"].append(ans)
print(questions)
print(user_answers)

# The rest of this stuff is unfinished stuff I wrote. Mostly dealing with trying to find the "end result"
# I bet I'll have to edit this a toooooon, but wanted to share.
'''def GetAnswer():
    quest1ans = input('Choose a, b, c, or d:')  # FIXME - needs to not rely on these variables, but counts answers
    if quest1ans == 'a':
        a_count.append(1)
    elif quest1ans == 'b':
        b_count.append(1)
    elif quest1ans == 'c':
        c_count.append(1)
    elif quest1ans == 'd':
        d_count.append(1)
    else:
        print('Invalid answer, try again.')
        return GetAnswer()


print(title)
print()
print(prompt)
print()
i = 0


#### This basic loop makes some sense, probably needs to be corrected waaay later.

for question in questions:
    i += 1
    answers = questions[question]
    print('Question #', i, ':', sep='', end=' ')
    print(question)
    for answer in answers:
        print(answer)
    print()
    GetAnswer()


### Just to count final scores... hm.

final_a = len(a_count)
final_b = len(b_count)
final_c = len(c_count)
final_d = len(d_count)

final_scores = [final_a, final_b, final_c, final_d]
final_scores.sort(reverse=True)
if final_scores[0] == final_a:
    print('Your result is', a)
elif final_scores[0] == final_b:
    print('Your result is', b)
elif final_scores[0] == final_c:
    print('Your result is', c)
else:
    print('Your result is', d)'''