#memoryBeats_02.py - Exploratory program for rhythm-based memorization app.

#New in 01: Uses external data.txt file, keeps track of streak.
#02: Type 'q' to quit.  Print_streak(streak) function added.
#03: To do: Generalize functions so that they can call different dictionaries.
#04: Cause sets of correct and incorrect responses to compile new dictionaries.

import time, random, ast
print ('Type "q" to quit.')

with open ('hsk3_trans_dict2.txt', 'r', encoding='utf-8') as fin:
    s = fin.read()
    data = ast.literal_eval(s)

all_pairs = data
all_keys = list(all_pairs.keys())
all_values = list(all_pairs.values())

def generate_answers(correct_value, all_values):
    answers = [] #Make a blank list of answers
    answers.append(correct_value) #Add the correct answer
    all_values_copy = all_values.copy() #Copy all_values to avoid modifying the list.
    all_values_copy.remove(correct_value) #Remove the correct answer from the copy
    all_wrong_values = all_values_copy #Make a list of wrong answers.
    wrong_answers = random.sample(all_wrong_values, k= 3) #Get three wrong answers
    for i in range(len(wrong_answers)):
        answers.append(wrong_answers[i]) #Add each wrong answers
    answers = random.sample(answers, k = len(answers)) #Shuffle the list
    for i in range(len(answers)):
        print(str(i+1) +'. ' + str(answers[i]), end='  ')
    return answers

def get_response(correct_value, answers):
    while True:
        try:
            res = input()
            if res.lower() == 'q':
                quit()
            else:
                res = int(res)-1
                break
        except:
            print('Please use the number keys to select your response.')
    if correct_value == answers[res]:
        return True
        

def print_streak(streak):
    if streak != 0:
        feedback = streak % 4
        if feedback == 0:
            print (str(streak) + '!!!!')
        elif feedback == 1:
            print('bing!')
        elif feedback == 2:
            print ('bang!!')
        elif feedback == 3:
            print ('boom!!!')
    else:
        print ('blerg...')

streak = 0
for i in range (100):
    time.sleep(.33)
    correct_key = all_keys[random.randint(0,len(all_keys)-1)]
    correct_value = all_pairs[correct_key]
    print (correct_key)
    time.sleep(.66)
    answers = generate_answers(correct_value, all_values)
    if get_response(correct_value,answers):
        streak = streak + 1
        #print (streak)
    else:
        streak = 0
    print_streak(streak)
    #print (correct_value)
    print('\n')

    
