import random

def play():
	user = input ("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
	ai = random.choice(['r', 'p', 's'])

	if user == ai:
		return 'It\'s a tie'
	if is_win(user, ai):
		return 'You won!'

	return 'you lost!'

def is_win(player, opponent):
	if (player == 'r' and opponent == 's') or ('player' == 's' and opponent == 'p')\
		or (player == 'p' and opponent == 'r'):
		return True
print(play())