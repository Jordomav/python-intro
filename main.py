# print 'Hello World'
# name = raw_input('Your name: ')
# print name
# if the robot runs into an object have the robot stop and back up
# if hitsObject():
    # goBack()
#if 1 == 1:
#     print 'Yes'
# def myFirstFunction():
#     print 'Function ran'
# myFirstFunction()
# def functionWithInput(name, age):
#     print name
#     print age
# functionWithInput('Jordan', 21)
# numbers = [1,2,3,4,5,6,7,8,9,10]
# colors = ['red', 'blue', 'green']
# print numbers[0]
# for number in numbers:
#     if number % 2 == 0:
#         print number
# for color in colors:
#     if color == 'red':
#         print 'You printed red'
#     elif color == 'blue':
#         print 'You printed blue'
#     elif color == 'green':
#         print 'You printed green'
#     else:
#         print 'Color not found'

noun1 = raw_input('Please enter a noun:')
verb1 = raw_input('Please enter a verb:')
noun2 = raw_input('Please enter another noun:')
verb2 = raw_input('Please enter another verb:')

def check_input(user_input):
    if user_input != '' or user_input != ' ':
        return user_input
    else:
        print 'You entered an incorrect input!'
        return

def start_game():
    print 'You were walking along one day, when you heard a faint noise from overhead. You looked up and a giant %s was floating in the sky. You panicked, because well, why is a giant %s floating in the sky? Seconds later, it started to %s. You started to run in fear, but it was gaining on you. Your only hope was a %s' %(noun1, noun1, verb1, noun2)
    
start_game()