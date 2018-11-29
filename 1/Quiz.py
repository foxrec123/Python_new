correct_answers = 0

answer = input('Which language are we learning?\n')

if answer.lower() == 'python':
    print('You are right!')
    correct_answers += 1
else:
    print('You are wrong!')

answer = input('Which country do you live?\n')

if answer.lower() == 'russia':
    print('You are right!')
    correct_answers += 1
else:
    print('You are wrong!')

print('Answers in total: ', correct_answers)
