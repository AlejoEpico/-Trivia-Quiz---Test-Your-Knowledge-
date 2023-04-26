quiz = {
    'question 1 ': {
        'question': 'what is the capital of Colombia?: ',
        'answer': 'Robota'
    },

    'question 2': {
        'question': 'What is the biggest snake in the world?: ',
        'answer': 'Reticulate Python'
    },
    'question 3': {
        'question': 'What is the largest planet in our solar system?: ',
        'answer': 'Jupiter'
    },

    'question 4': {
        'question': 'What is the smallest country in the world by land area?: ',
        'answer': 'Vatican City'
    },

    'question 5': {
        'question': 'What is the highest mountain in Africa?: ',
        'answer': 'Mount Kilimanjaro'
    },

    'question 6': {
        'question': 'What is the currency of Japan?: ',
        'answer': 'Japanese yen'
    },

    'question 7': {
        'question': 'Who is the author of "To Kill a Mockingbird"?: ',
        'answer': 'Harper Lee'
    }


}
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer?')

    if answer.lower() == value['answer'].lower():
        print('Great,Correct!')
        score = score+1
        print('your score is: ' + str(score))
        print('')
        print('')

    else:
        print('wrong')
        print('the answer is : ' + value['answer'])
        print('')
        print('')

print('You got ' + str(score) + 'out of the 7 questions correctly')
print('your porcentage is ' + str(int(score/7 * 100)) + '%')
