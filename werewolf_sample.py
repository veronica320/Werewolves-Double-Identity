import random
import sys

def has_jinbaobao(char_groups):
	if {"平民"} in char_groups or {"盗贼", "平民"} in char_groups:
		return True
	else:
		return False

if __name__ == "__main__":

	if len(sys.argv) < 2:
		print("Usage: python werewolf_sample.py n_players\nExample:python werewolf_sample.py 6")
		exit(1)
	n_players = int(sys.argv[1])

	if n_players not in [6,8]:
		print("n_players can only be 6 or 8.")
		exit(1)

	if n_players == 6:
		characters = ["狼人"] + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + \
					 ["盗贼"] + ["平民"]*5
	elif n_players == 8:
		characters = ["狼人"]*2 + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + ["白痴"] + ["禁言长老"] + \
					 ["盗贼"] + ["平民"]*8

	n_characters = len(characters)

	while(True):
		is_valid = True

		shuffled_indices = list(range(n_characters))
		random.shuffle(shuffled_indices)
		char_groups = [set([characters[shuffled_indices[i]], characters[shuffled_indices[i+1]]]) for i in range(0, n_characters, 2)]

		if not has_jinbaobao(char_groups):
			continue

		for char_group in char_groups:
			if char_group == {"狼人", "潜行狼"}:
				is_valid = False
				break
			if char_group == {"狼人", "预言家"} or char_group == {"潜行狼", "预言家"}:
				is_valid = False
				break

		if is_valid:
			break

	for player_id, char_group in enumerate(char_groups):
		char_group = list(char_group)
		if len(char_group) == 1:
			char_group = char_group * 2
		print(f"{player_id+1}号玩家身份: {char_group[0]} {char_group[1]}")
