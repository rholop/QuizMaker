print("This program will allow you to make a quiz. Users will answer questions and then based on their answers, the "
      "quiz will give them the result that matches the majority of the questions they answered. For example: if your "
      "quiz is to determine which Star Trek character the user is most like, if 40% of their answers map to 'Spock' "
      "but 60% of their answers map to Captain Kirk, the user's result will be Captain Kirk.")
print()


print("Great, your quiz will have five questions.")


def getAnsNum():
    ans_num = int(input("How many answer choices do you want your questions to have? Enter a number between 2-5: "))
    if 2 > ans_num or ans_num > 5:
        print('Invalid entry.')
        return getAnsNum()
    else:
        print("Great, your quiz will have", ans_num, "answer choices and possible outcomes.")
        return ans_num


ques_num = getQuesNum()
print()
ans_num = getAnsNum()
print()
print("Now, let's figure out what the", ans_num, "quiz results will be.")
ans_output = []


for x in range(1, ans_num+1):
    print("What will the description be for result ", x, "? (Ex: 'Captain Kirk')", sep='', end=' ')
    output = input()

