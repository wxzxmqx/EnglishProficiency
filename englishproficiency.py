# Greeting

print("\n       English Profiency Test       ")
print("   20 questions to check your level       ")
print("         Difficulty: Medium\n")

# Questionnaire
name = input('What\'s your name?\n'
             'Answer: ')
print(f'\nNice to meet you, {name}. Let\'s get started!\n')

# Rules of test
print('Here is a 20-question English fluency test designed'
      '\nto assess someone`s level. It covers grammar,'
      '\nvocabulary, sentence structure, and comprehension.'
      '\nAfter each question, I`ll include an explanation'
      '\nof the correct answer.')

# Statistic
score = 0
all_questions = 20

# Question 1
print('\n\n1. Choose the correct sentence.')
print('\n A. I has been working here for two years.')
print(' B. I have been working here for two years.')
print(' C. I have working here for two years.')
print(' D. I working here for two years.')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: The correct sentence uses'
          '\nthe present perfect tense ("have been working"),'
          '\nwhich is used to describe actions that started'
          '\nin the past and continue in the present.')

# Question 2
print('\n\n2. Which word is a synonym of "happy"?')
print('\n A. Sad.')
print(' B. Angry.')
print(' C. Joyful.')
print(' D. Tired.')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Joyful" is a synonym of "happy".'
          '\nBoth words describe a positive emotion or state.')

# Question 3
print('\n\n3. Fill in the blank: "She ________ a book right now.')
print('\n A. reads')
print(' B. is reading')
print(' C. read')
print(' D. has read')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: The present continuous tense ("is reading")'
          '\nis used for actions happening right now.')

# Question 4
print('\n\n4. Choose the correct sentence.')
print('\n A. I like reading books more than watching TV.')
print(' B. I like more reading books than watching TV.')
print(' C. I reading books more than watching TV.')
print(' D. I more like reading books than watching TV.')
answer = input('\n Your answer: ')

if answer == "a" or answer == "A":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "More than" is placed after the object'
          '\n("reading books") to show preference in comparison.')

# Question 5
print('\n\n5. Which of these sentences is in the past tense?')
print('\n A. She eats lunch at 12:00 PM.')
print(' B. She will eat lunch at 12:00 PM.')
print(' C. She is eating lunch at 12:00 PM.')
print(' D. She ate lunch at 12:00 PM.')
answer = input('\n Your answer: ')

if answer == "d" or answer == "D":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: The past simple tense ("ate") is used'
          '\nto describe an action that has already happened.')

# Question 6
print('\n\n6. Choose the correct preposition: "She is good ______ playing tennis."')
print('\n A. in')
print(' B. on')
print(' C. at')
print(' D. with')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: We use "at" when referring to a skill'
          '\nor ability (e.g., good at playing tennis).')

# Question 7
print('\n\n7. Which of the following is the correct form of the verb?')
print('\n A. I will going to the store.')
print(' B. I going to the store.')
print(' C. I am going to the store.')
print(' D. I will go to the store.')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Am going" is the present continuous tense, which is used'
          '\nto describe an action that is happening right now or is planned'
          '\nfor the near future.')

# Question 8
print('\n\n8. Choose the correct sentence.')
print('\n A. The book is on the table.')
print(' B. The book are on the table.')
print(' C. The books is on the table.')
print(' D. The books are in the table.')
answer = input('\n Your answer: ')

if answer == "a" or answer == "A":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "The book" is singular, so we use "is."')

# Question 9
print('\n\n9. What is the past participle of "go"?')
print('\n A. Went')
print(' B. Gone')
print(' C. Goes')
print(' D. Going')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Gone" is the past participle of "go," which is used'
          '\nwith auxiliary verbs like "have."')

# Question 10
print('\n\n10. Choose the correct word: "Can you _______ the door?"')
print('\n A. close')
print(' B. closed')
print(' C. to close')
print(' D. closing')
answer = input('\n Your answer: ')

if answer == "a" or answer == "A":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "The base form "close" is used after "can."')

# Question 11
print('\n\n11. Choose the correct article: "______ apple a day keeps the doctor away."')
print('\n A. A')
print(' B. An')
print(' C. The')
print(' D. No article')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "An" is used before words that start '
          '\nwith a vowel sound ("apple").')

# Question 12
print('\n\n12. Which of the following sentences is in the future tense?')
print('\n A. I study every day.')
print(' B. I will study tomorrow.')
print(' C. I studied yesterday.')
print(' D. I am studying now.')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: The future tense is formed with "will" + base verb ("will study").')

# Question 13
print('\n\n13. Choose the correct sentence.')
print('\n A. We didn’t went to the party.')
print(' B. We don’t went to the party.')
print(' C. We didn’t go to the party.')
print(' D. We don’t go to the party.')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Didn’t" is followed by the base verb ("go").')

# Question 14
print('\n\n14. Which of the following is a question?')
print('\n A. I am going to the park.')
print(' B. Do you like pizza?')
print(' C. He is reading a book.')
print(' D. She watches TV every day.')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: The sentence with "Do" at the beginning is a question.')

# Question 15
print('\n\n15. Fill in the blank: "I _______ some coffee."')
print('\n A. drink')
print(' B. drinks')
print(' C. drinking')
print(' D. drunk')
answer = input('\n Your answer: ')

if answer == "a" or answer == "A":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Drink" is the correct form for the present tense ("I drink").')

# Question 16
print('\n\n16. Choose the correct conjunction: "I wanted to go to the beach ______ it started raining."')
print('\n A. and')
print(' B. but')
print(' C. or')
print(' D. because')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "But" is used to contrast two ideas, showing a change or an obstacle (rain).')

# Question 17
print('\n\n17. "She _______ a beautiful song yesterday."')
print('\n A. sings')
print(' B. singing')
print(' C. sang')
print(' D. sing')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Sang" is the past form of "sing," used for actions '
          '\nthat happened in the past.')

# Question 18
print('\n\n18. What is the plural of "child"?')
print('\n A. childs')
print(' B. childes')
print(' C. children')
print(' D. childer')
answer = input('\n Your answer: ')

if answer == "c" or answer == "C":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Children" is the irregular plural form of "child."')

# Question 19
print('\n\n19. Choose the correct sentence.')
print('\n A. There is many books on the shelf.')
print(' B. There are many books on the shelf.')
print(' C. There is much books on the shelf.')
print(' D. There are much books on the shelf.')
answer = input('\n Your answer: ')

if answer == "b" or answer == "B":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Many" is used with countable nouns (like books), '
          '\nand we use "are" for plural subjects.')

# Question 20
print('\n\n20. Which of the following is the correct form of the verb?')
print('\n A. He has ate the pizza.')
print(' B. He eat the pizza.')
print(' C. He eaten the pizza.')
print(' D. He has eaten the pizza.')
answer = input('\n Your answer: ')

if answer == "d" or answer == "D":
    score += 1
    print(' You are right. Next question..\n\n')
else:
    print(' Oops... It\'s wrong!\n')
    print('Explanation: "Eaten" is the past participle of "eat," which is used with "has."')

# Estimating level of proficiency

if score >= 16 and score <= 20:
    advanced = 'Advanced (C1)'
    print(f'\nYour level of English might be {advanced}.')
    print(f'Total questions: {score}/{all_questions}.')
elif score >= 11 and score <= 15:
    intermediate = 'Intermediate (B1-B2)'
    print(f'\nYour level of English might be {intermediate}.')
    print(f'Total questions: {score}/{all_questions}.')
elif score >= 6 and score <= 10:
    preintermediate = 'Pre-Intermediate (A2)'
    print(f'\nYour level of English might be {preintermediate}.')
    print(f'Total questions: {score}/{all_questions}.')
else:
    beginner = 'Beginner (A1)'
    print(f'\nYour level of English might be {beginner}.')
    print(f'Total questions: {score}/{all_questions}.')
