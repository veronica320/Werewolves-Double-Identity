# -*- coding: UTF-8 -*-

import random
import sys

def num_jinbaobao(char_groups):
	return len([char_group for char_group in char_groups if char_group in [{"平民"}, {"盗贼", "平民"}]])

if __name__ == "__main__":

	if len(sys.argv) < 2:
		print("Usage: python assign_roles.py n_players(5-11)\nExample:python assign_roles.py 6")
		exit(1)
	n_players = int(sys.argv[1])

	if n_players < 5 or n_players > 11:
		print("n_players can only be between 6-11.")
		exit(1)
	if n_players == 5:
		characters = ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["白痴"] + \
					 ["盗贼"] + ["平民"]*4
	elif n_players == 6:
		characters = ["狼人"] + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + \
					 ["盗贼"] + ["平民"]*5
	elif n_players == 7:
		characters = ["狼王"] + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + \
					 ["盗贼"] + ["平民"]*7
	elif n_players == 8:
		characters = ["狼人"]*2 + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + ["白痴"] + ["禁言长老"] + \
					 ["盗贼"] + ["平民"]*6
	elif n_players == 9:
		characters = ["狼王"] + ["狼人"] + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + ["白痴"] + ["禁言长老"] + \
					 ["盗贼"] + ["平民"]*8
	elif n_players == 10:
		characters = ["恶灵骑士"] + ["狼人"] + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + ["白痴"] + ["禁言长老"] + \
					 ["盗贼"] + ["平民"]*10
	elif n_players == 11:
		characters = ["狼王"] + ["恶灵骑士"] + ["潜行狼"] + \
					 ["预言家"] + ["女巫"] + ["猎人"] + ["守卫"] + ["白痴"] + ["禁言长老"] + \
					 ["盗贼"] + ["平民"]*12

	n_characters = len(characters)
	assert n_characters == 2*n_players

	while(True):
		is_valid = True

		shuffled_indices = list(range(n_characters))
		random.shuffle(shuffled_indices)
		char_groups = [set([characters[shuffled_indices[i]], characters[shuffled_indices[i+1]]]) for i in range(0, n_characters, 2)]
		# print(char_groups)

		if num_jinbaobao(char_groups) == 0:
			continue

		ratio_jinbaobao = num_jinbaobao(char_groups) / n_players
		if ratio_jinbaobao < 0.15 or ratio_jinbaobao > 0.40:
			continue

		for char_group in char_groups:
			if char_group == {"狼人", "潜行狼"} or char_group == {"狼王", "潜行狼"} or char_group == {"恶灵骑士", "潜行狼"}:
				is_valid = False
				break
			if char_group == {"狼人", "预言家"} or char_group == {"潜行狼", "预言家"} or char_group == {"狼王", "预言家"} or char_group == {"恶灵骑士", "预言家"}:
				is_valid = False
				break

		if is_valid:
			break

	for player_id, char_group in enumerate(char_groups):
		char_group = list(char_group)
		if len(char_group) == 1:
			char_group = char_group * 2
		print(f"{player_id+1}号玩家身份: {char_group[0]} {char_group[1]}")