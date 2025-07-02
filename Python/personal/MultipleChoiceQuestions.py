def askQuestion(question):
    q = questions.get(question)
    print(f'{q[0]}\n')
    for i in range(len(q[1])):
        print(f'{i+1}) {q[1][i].get("a")}')
    
    while True:
        try:
            a = int(input('Answer number: '))
            if a > len(q[1]):
                raise ValueError
            break
        except ValueError:
            print('Please only enter a valid number.')

    if q[1][a-1].get('correct'):
        return True
    else:
        return False

questions = {
    1: ['question1', [{'a': 'answer1', 'correct': False}, {'a': 'answer2', 'correct': True}, {'a': 'answer3', 'correct': False}]],
    2: ['question2', [{'a': 'answer1', 'correct': False}, {'a': 'answer2', 'correct': False}, {'a': 'answer3', 'correct': True}]],
    3: ['question3', [{'a': 'answer1', 'correct': True}, {'a': 'answer2', 'correct': False}, {'a': 'answer3', 'correct': False}, {'a': 'answer3', 'correct': False}]],
}

for question in questions:
    print(askQuestion(question))
    
