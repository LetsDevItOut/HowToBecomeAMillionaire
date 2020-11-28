import random
import sys


# global variable that increases with each question
question_number = 0
user_lost = False
user_score = 0


# to rindomize games 
diff_games = [0, 1]
current_game = random.choice(diff_games)


remove_call_fiend = False
remove_ask_audience = False
remove_fifty_fifty = False
# 50/50 is very special option that changes ABCD to only two options
# had to create this variable to show if it's beed used
used_fifty_fifty = None

questions1 = ["How many seconds are in a minute?", 'What makeup product makes eyelashes appear longer?',
"What city contains the Eiffel Tower?", "Which sport is also known as football?", 'How many continents are there?', 
'Who wasn\'t a member of the Beatles?', 'Which of the following is not a type of pasta?',
'Which state has cities named San Francisco and Hollywood?', 'Which instrument does not have strings?',
'What gas makes voices sound higher when inhaled?', 'What American holiday falls on July 4?',
'Which candy bar shares its name with a galaxy?', 'What is the capital of England?', 
'Which one of the following is not an Ivy League University?', 'What is someone who collects coins called?',]

questions2 = ["What are the names of the Super Mario Bros.?", 'Which princess lost a glass slipper?',
"Who was the first woman to fly solo across the Atlantic?", "Which U.S. city is home to the Liberty Bell and Independence Hall?",
'Which pop culture franchise has characters named Luke Skywalker and Han Solo?', 'How many days are in a leap year?',
'Who is the current British monarch?', 'What children\'s show features characters named Big Bird and Elmo?', 
'What is the smallest unit of American currency?', 'What is the first name of McDonald\'s mascot?',
'Who is the current host of "The Tonight Show?"', 'What is the first letter of the Greek alphabet?', 
'What is the term length for the president of the United States?', 'Which mode of transportation traditionally has two wheels?', 
'Which American car company makes the F-150 and Escape?',]

questions = [questions1, questions2]

one_of_four1 = [ 
['A) 30', 'B) 60', 'C) 1', 'D) 300 '], ['A) Mascara', 'B) Blush', 'C) Foundation', 'D) Lipstick'],
['A) Sydney', 'B) Los Angeles', 'C) New York City', 'D) Paris'], ['A) Soccer', 'B) Basketball', 'C) Baseball', 'D) Cricket'],
['A) 1', 'B) 6', 'C) 8', 'D) 7'], ['A) John Lennon', 'B) Justin Timberlake', 'C) Ringo Star', 'D) Paul McCartney'],
['A) Spaghetti', 'B) Escargot', 'C) Fettuccine', 'D) Ziti'], ['A) Utah', 'B) Hawaii', 'C) California', 'D) Florida'],
['A) Guitar', 'B) Bass', 'C) Trombone', 'D) Cello'], ['A) Oxygen', 'B) Nitrogen', 'C) Sulfur Hexafluoride', 'D) Helium'],
['A) Thanksgiving Day', 'B) Independence Day', 'C) Liberty Day', 'D) Presedents Day'], ['A) Milky Way', 'B) Snickers', 'C) 3 Musketeers', 'D) Almond Joy'],
['A) London', 'B) Moscow', 'C) Paris', 'D) Rome'], ['A) Harvard', 'B) Princeton', 'C) Columbia', 'D) Hogwarts'],
['A) Professor', 'B) Chef', 'C) Numismatist', 'D) Psychiatrist'], 
]

one_of_four2 = [ 
['A) Tim and Eric', 'B) Batman and Robin', 'C) Sonic and Tails', 'D) Mario and Luigi'], ['A) Snow White', 'B) Mulan', 'C) Cinderella', 'D) Belle'],
['A) Geraldine Ferraro', 'B) Martha Stewart', 'C) Amelia Earhart', 'D) Sally Ride'], ['A) Vancouver', 'B) Mexico City', 'C) Beijing', 'D) Philadelphia'],
['A) Harry Potter', 'B) Star Wars', 'C) James Bond', 'D) Star Trek'], ['A) 366', 'B) 367', 'C) 365', 'D) 364'],
['A) King Philippe', 'B) Queen Victoria', 'C) King George', 'D) Queen Elizabeth II'], ['A) Barney&Friends', 'B) Sesame Street', 'C) Spongebob Squarepants', 'D) The Wiggles'],
['A) Penny', 'B) Dime', 'C) Quarter', 'D) Dollar'], ['A) Susan', 'B) George', 'C) Ronald', 'D) Karl'],
['A) Jimmy Fallon', 'B) Oprah Winfrey', 'C) Anne Curry', 'D) Bob Barker'], ['A) E', 'B) Alpha', 'C) Omega', 'D) Zed'],
['A) 1', 'B) 5', 'C) 6', 'D) 4'], ['A) Car', 'B) Bicycle', 'C) Tricycle', 'D) Bus'],
['A) Ford', 'B) Dodge', 'C) Volkswagen', 'D) Nissan'], 
]

one_of_four = [one_of_four1, one_of_four2]
# random phrases, will show up if your answer correct
list_of_support = ['Great job', 'Well done', 'Nailed it', 'Good job', 'You are one step closer to your goal', 'Keep it up']

user_options = ['call friend', 'ask audience', '50/50']

correct_answer1 = (1, 0, 3, 0, 3, 1, 1, 2, 2, 3, 1, 0, 0, 3, 2)
correct_answer2 = (3, 2, 2, 3, 1, 0, 3, 1, 0, 2, 0, 1, 3, 1, 0)

correct_answer = [correct_answer1, correct_answer2]
# user score
dollars_per_question = (100, 100, 100, 200, 500, 1000, 2000, 4000, 8000, 16000,
	32000, 61000, 125000, 250000, 500000)




def start_game():
# basic intro
	print('Hello and welcome to the game of millionares.\nYou will have 15 questions before you can become very rich.\nI wish you luck. And don\'t forget, if you need help just type\n\'I need help\'')
	print()
	for question in questions[current_game]:
		ask_question()
		user_input()	
		check_user_input()
		check_if_lost()
		check_if_won()

	return




# takes argument to show new question each time
def ask_question():
	global question_number
	# prints question
	print(questions[current_game][question_number])
	# creates space between lines
	print()
	# prints options
	print(one_of_four[current_game][question_number])
	
	return




# takes user answer
def user_input():
# making this variable a global will allow me to use variable in other functions
	global user_answer
# for spacing
	print()
	user_answer1 = input('Your answer(A, B, C, or D): ')
# in case user need to use one of the hints he can call it here	
	user_answer = user_answer1.title()
# user won't need to type the whole answer into comand	
	if user_answer == 'I Need Help':
		user_help()
	elif user_answer == 'A':
# for some reason when i get number of the correct answer list it will give me [0] insdead of 0
# so I had to change it here to list 0 --- [0]		
		user_answer = [0]
		final_answer()
	elif user_answer == "B":
		user_answer = [1]
		final_answer()
	elif user_answer == 'C':
		user_answer = [2]
		final_answer()
	elif user_answer == 'D':
		user_answer = [3]
		final_answer()
	else:
		print("Wrong input.")
		user_input()




def final_answer():
	final_ans = input('Final answer?(y/n): ')
	if final_ans == 'y':
		pass
	elif final_ans == 'n':
		user_input()
	else:
		print("Wrong input.")
		final_answer()
			

	


def check_user_input():
	global user_answer
	global question_number
	global correct_answer
	global user_score
	global user_lost
	
	# question number provides me access to the right answer in one of four list
	if user_answer == [correct_answer[current_game][question_number]]:
		user_score = user_score + dollars_per_question[question_number]
		print(random.choice(list_of_support) + '!')
		print()
		if user_score < 1000000:
			print('You currently won $' + str(user_score) + ' dollars.')
			print()
		else:
			pass	
	else:
		user_lost = True
	# changes global question number to print new question
	question_number += 1
	return




def check_if_lost():
	global user_lost
# checks if global variable user_lost changed to true to stop game
	if user_lost:
		if user_score >= 32000:		
			print('Wrong answer.')
			print('You lost a change to become a millionare, but you still earned $32000.')
			print('Thank you for the game!')
			sys.exit()
		elif user_score >= 1000:		
			print('Wrong answer.')
			print('You lost a change to become a millionare, but at least you earned $1000.')
			print('Thank you for the game!')
			sys.exit()
		else:			
			print('Wrong answer.')
			print('You lost it.')
			print('Thank you for the game!')
			sys.exit()

	


def check_if_won():
	global user_score
	if user_score >= 1000000:
		print('Congradulations! You won $1,000,000 and became a millionare!!!')
	else:
		pass
	return




def user_help():
	# refers to a list with three options
	global user_options
	
	if user_options == []:
		print("Unfortunatelly, you have used all your options.")
		user_input()
		return	
	else:
		pass

	print()
	print('Your options:')
	print(user_options)

	user_option_input = input('Choose now: ')
# if user wanted to reuse option it prevents it
	if user_option_input in user_options:
		pass
	else:
		print('You already used this option.')
		user_help()
# calls specific fuction based on user input
	if user_option_input == 'call friend':
		call_friend()
	
	elif user_option_input == 'ask audience':
		ask_audience()
	
	elif user_option_input == '50/50':
		fifty_fifty()
	
	else:
		print('Wrong input')
		user_help()
	return




def call_friend():
	global user_options
	global question_number
	global remove_call_fiend
	global used_fifty_fifty
	global new_list
# your friend computer and his random choice option	
# now it will give you right answer in 62.5%
	if used_fifty_fifty == question_number: 
		rand_option = random.choice(new_list)
	else:
		random_one = random.choice(one_of_four[current_game][question_number])
		random_two = random.choice(one_of_four[current_game][question_number][correct_answer[current_game][question_number]])
		random_list = [random_one, random_two]
		rand_option = random.choice(random_list)
			
	print('It\'s hard to say, but it can be ' + str(rand_option) + '.')
	print()
	if remove_call_fiend == False:
		user_options.remove('call friend')
		remove_call_fiend = True
	else:
		pass
	user_input()
# need to delete call friend from the list




def ask_audience():
	global user_options
	global question_number
	global remove_ask_audience
	global new_list
	global ff_sorted
# because of if staments some variables won't get values which causes an error
	answ1 = 0
	answ2 = 0
	answ3 = 0
	answ4 = 0
	answ5 = 0
	answ6 = 0
# assings random number to a variable	
	if used_fifty_fifty == question_number:
		answ5 = random.randint(1,50) + 10
		answ6 = random.randint(1,50) + 10
		
		if new_list[0] == ff_sorted[0]:
			answ5 = answ5 + (100 - answ6 - answ5)
		elif new_list[1] == ff_sorted[1]:
			answ6 = answ6 + (100 - answ6 - answ5)
		else:
			pass		
	else:
		answ1 = random.randint(1,25) + 5
		answ2 = random.randint(1,25) + 5
		answ3 = random.randint(1,25) + 5
		answ4 = random.randint(1,25) + 5		
	# if answer is correct this if statment will increase it's %	
		if correct_answer[current_game][question_number] == 0:
			answ1 = answ1 + (100 - answ1 - answ2 - answ3 - answ4)
		
		elif correct_answer[current_game][question_number] == 1:
			answ2 = answ1 + (100 - answ1 - answ2 - answ3 - answ4)
		
		elif correct_answer[current_game][question_number] == 2:
			answ3 = answ1 + (100 - answ1 - answ2 - answ3 - answ4)
		
		elif correct_answer[current_game][question_number] == 3:
			answ4 = answ1 + (100 - answ1 - answ2 - answ3 - answ4)
		else:
			print('Something went wrong, I\'m sorry.')

	second_list = [answ5, answ6]
	list_of_answ = [answ1, answ2, answ3, answ4] 
	
	print('Audience made their choice:')
	answ_number = 0
	
	if used_fifty_fifty == None:
		for item in one_of_four[current_game][question_number]:
			print(str(item) + " " + str(list_of_answ[answ_number]) + "%")
			answ_number += 1
	elif used_fifty_fifty == question_number:
		for item in new_list:
			print(str(item) + " " + str(second_list[answ_number]) + "%")
			answ_number += 1
	else:
		for item in one_of_four[current_game][question_number]:
			print(str(item) + " " + str(list_of_answ[answ_number]) + "%")
			answ_number += 1

	if remove_ask_audience == False:
		user_options.remove('ask audience')
		remove_ask_audience = True
	else:
		pass
	user_input()



	
def fifty_fifty():
	global user_options
	global question_number
	global correct_answer
	global remove_fifty_fifty
	global used_fifty_fifty
	global new_list
	global ff_sorted
# copies main list, so it won't delete poped items in main	
	ff_list = one_of_four[current_game][question_number].copy()
	new_list = []
# pops right answer and random another
	option1 = ff_list.pop(correct_answer[current_game][question_number])
	option2 = ff_list.pop()
	
	new_list.append(option1)
	new_list.append(option2)
# sorts list so options always start with 'a'	
	ff_sorted = sorted(new_list)
	print(ff_sorted)
	
	if remove_fifty_fifty == False:
		user_options.remove('50/50')
		remove_fifty_fifty = True
	else:
		pass
	
	if used_fifty_fifty == None:
		used_fifty_fifty = question_number
	else:
		pass	

	user_input()
	return


start_game()


