import random
import time

die_amount = int(input("How many dice are you using?\n"))
if die_amount == 1:
	die_type = int(input("How many sides does your die have?\n"))
	rando_single = random.randint(1, die_type)
	print("The die is cast!")
elif die_amount > 1:
	dice_types = int(input("How many sides do your dice have?\n"))
	print("The dice are cast!")
time.sleep(.75)

if die_amount == 1: 
	print(f"It reads: {rando_single}")
	time.sleep(.75)
	print("Press Enter to roll again.")

elif die_amount > 1:
	dice_list = []
	for i in range(die_amount):
		dice_list.append((str((random.randint(1, dice_types)))))
	print(f"They read: {dice_list}")
	time.sleep(.75)
	print("Press Enter to roll again.")

while True:
	input()
	time.sleep(.4)
	if die_amount == 1:
		print(f"The die reads: " + (str((random.randint(1, die_type)))))
	elif die_amount > 1:
		loop_dice_list = []
		for i in range(die_amount):
			loop_dice_list.append(str((random.randint(1, dice_types))))
		print(f"The dice read: {loop_dice_list}")
