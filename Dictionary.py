import json
import pyttsx3

# initialisation 
engine = pyttsx3.init('sapi5')
voiceDecision = (input('do you want voice support? \nyes : y\nno : n\n')).lower()


def read(line):
    if voiceDecision == 'y':
        engine.say(line)
        engine.runAndWait()
    else:
        pass


def update_meaning(word):
    read('Will you provide the meaning to our database')
    decision = input('Will you provide the meaning to our database: \nyes : y\nno : n\n')

    if decision.lower() == 'y':
        read('Please type the meaning')
        mean = input('Please type the meaning\n')
        print('Thanks for your feedback')
        read('Thanks for your feedback')
        x[word] = [mean]
        print('The meaning of {} is {}'.format(my, x[word]))
        read('The meaning of {} is {}'.format(my, x[word]))
        with open('my_dictionary_database.json', 'w') as f:
            json.dump(x, f, indent=2, sort_keys=True)

    else:
        print('Maybe next time!!Thanks for using!')
        read('Maybe next time!!Thanks for using!')


with open('my_dictionary_database.json') as f:
    x = json.load(f)  # open the database

read('please type the word')
my = input('your word: ')  # taking the input from user
word = my.lower()
if word not in x:
    print('Sorry we dont have the word in our database.')
    read('Sorry we dont have the word in our database.')
    update_meaning(word)  # update the database

else:
    print('The meaning of {} is {}\n'.format(my, x[word]))
    read('The meaning of {} is {}\n'.format(my, x[word]))

    read('is this meaning ok?')
    feedback = input('Is this meaning ok?\nyes:y\nno:n\n')

    if feedback.lower() == 'y':
        print('thanks for you feedback')
        read('thanks for you feedback')

    elif feedback.lower() == 'n':
        update_meaning(word)

    else:
        print('Wrong input!!Maybe next time!!Thanks for using!')
        read('Wrong input!!Maybe next time!!Thanks for using!')

read('press enter to quit')
a = input()
