import random

#simple conversion library
item_conversion = {
    "s": "scissors",
    "p": "paper",
    "r": "rock"
}
def play():
	
	#user input
	#first CPU choice is random and the rest are decided by the previous win/lose condition
	cpu = random.choice(['r', 'p', 's'])
	cpu_old = 'None'
	user_win_counter = 0
	user_lose_counter = 0
	gameover = False
	
	
	#loop for best_of_19 RPS game

	while gameover==False:

		user = input("[R]ock, [P]aper, [S]cissors?: ")
		#checking if the input is valid
		while user !='r' and user!= 's' and user!='p':
			user = input("Give me the corrent input this time. [R]ock, [P]aper, [S]cissors?: ")
		#strategy after the 1st set is complete
		if cpu_old != 'None':
			if winner == 1:
				if cpu_old == 'r':
					cpu = 's'
				elif cpu_old == 's':
					cpu = 'p'
				elif cpu_old == 'p':
					cpu = 'r'
			elif winner == 0:
				if cpu_old == 'r':
					cpu = 'p'
				elif cpu_old == 'p':
					cpu = 's'
				elif cpu_old == 's':
					cpu = 'r'
			else:
				cpu = random.choice(['r', 'p', 's'])

		

		#testing the game result
		cpu_old = cpu
		if (user == 'r' and cpu == 's') or (user == 's' and cpu == 'p') or (user == 'p' and cpu == 'r'):
			print(f"YOU WIN, CPU called " + (item_conversion[cpu]))
			winner = 1
			user_win_counter += 1
		elif (user == 's' and cpu == 'r') or (user == 'r' and cpu == 'p') or (user == 'p' and cpu == 's'):
			print(f"YOU LOSE, CPU called " + (item_conversion[cpu]))
			winner = 0
			user_lose_counter += 1
		else:
			print("TIE, you both called " + (item_conversion[cpu]))

		#win counter
		if user_lose_counter == 10:
			print(f"GAME LOST!!! {user_win_counter} to {user_lose_counter}")
			gameover = True
		elif user_win_counter == 10:
			print(f"GAME WON!!! {user_win_counter} to {user_lose_counter}")
			gameover = True
	
	
play()


