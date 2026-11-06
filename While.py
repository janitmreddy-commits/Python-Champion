total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")
completed_count = 4
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"
    answer = input(f"Have you finished:{next_chore}?(yes or no)")
    if answer == "yes":
        completed_count += 1
        chore_num +=1
        print("Greate job!")
    else:
        print("Okay, finish it and check again")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("Stopping here on purpose - a real infinite loop never stops on its own!")
        break

