title = ''
prompt = ''

a = 'Tom Nook'
b = 'Dr. Shrunk'
c = 'Isabelle'
d = 'Blathers'

a_count = []
b_count = []
c_count = []
d_count = []

questions = {
}
user_questions = []
answer_choices = 5
user_answers = []

if answer_choices == 5:
    user_answers = ['a', 'b', 'c', 'd', 'e']
elif answer_choices == 4:
    user_answers = ['a', 'b', 'c', 'd']
elif answer_choices == 3:
    user_answers = ['a', 'b', 'c']
else:
    user_answers = ['a', 'b']

user_questions = ["What's your favorite thing to do on the weekend?", "What's your favorite color?"]

question_length = 5

for q in range(1, question_length+1):
    questions[f"question{q}"] = list({})
    for ans in user_answers:
        questions[f"question{q}"].append(ans)

''''
for key, n_key in zip(questions.keys(), user_questions):
    questions[n_key] = questions.pop(key)'''
print(questions)

'''for q in user_questions:
    for t in range(1, question_length+1):
        print(user_questions[])'''



'''
input_question1 = "What's your favorite thing to do on the weekend?"
answer1_1 = "a. Weekend? I'm too busy for those!"
answer1_2 = "b. Just making my friends laugh, having a good time."
answer1_3 = "c. Well, I'm so busy, but I do try to make some time to go see nature - the beach is always great!"
answer1_4 = "d. I love enriching myself with some culture!"

input_question2 = "What's your favorite color?"
answer2_1 = 'a. Brown'
answer2_2 = 'b. Pink'
answer2_3 = 'c. Yellow'
answer2_4 = 'd. Gold'

questions[question1] = [answer1_1, answer1_2, answer1_3, answer1_4]


def GetAnswer():
    quest1ans = input('Choose a, b, c, or d:')
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
for question in questions:
    i += 1
    answers = questions[question]
    print('Question #', i, ':', sep='', end=' ')
    print(question)
    for answer in answers:
        print(answer)
    print()
    GetAnswer()

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
    print('Your result is', d)
'''