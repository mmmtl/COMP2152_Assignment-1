"""
Author: Maria
Assignment: #1
"""


# ----- Question b -----
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # Float
highest_reps = 25 # Integer
membership_active = True # Boolean


# ----- Question c -----
# Dictionaries are data structures that store key value pairs
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 30, 15),
    "Taylor": (30, 90, 15)
}


# ----- Question d -----
i = 0
dict_length = len(workout_stats)
copy = workout_stats.copy()
keys = copy.keys()

while i < dict_length:
    for friend in keys:
        new_key = friend + "_Total"
        total = 0
        for minute in workout_stats[friend]:
            total += minute
        workout_stats[new_key] = total
    i += 1


# ----- Question e -----
# Lists are data structures that store values in square brackets
workout_list = []
values = workout_stats.values()

count = 0
for value in values:
    if count >= 3:
        break
    value = list(value)
    workout_list.append(value)
    count += 1


# ----- Question f -----
print("\n----- Question F -----")
print("Yoga and Running minutes from all friends")
for friend in workout_list:
    print(friend[0:2])

print("\nWeightlifting minutes from last two friends")
i = 0
last_two = len(workout_list) - 2
for friend in workout_list:
    if i >= last_two:
        print(friend[-1])
    i += 1


# ----- Question g -----
print("\n----- Question G -----")
for friend_name in workout_stats:
    subset = set("_Total")
    if subset.issubset(friend_name):
        if workout_stats[friend_name] >= 120:
            print(f"Great job staying active, {friend_name[:-6]}!")


# ----- Question h -----
print("\n----- Question H -----")
name = input("Enter a friend's name:")
flag = True
for friend in workout_stats:
    if (name.upper() == friend.upper()):
        key_total = friend + "_Total"
        print(f"This is {friend}'s Workout:")
        print(f"\t- Yoga: {workout_stats[friend][0]} minutes")
        print(f"\t- Running: {workout_stats[friend][1]} minutes")
        print(f"\t- Weightlifting: {workout_stats[friend][2]} minutes")
        print(f"Total: {workout_stats[key_total]} minutes")
        flag = True
        break
    else:
        flag = False
if flag == False: print(f"Friend {name} not found in the records.")


# ----- Question i -----
print("\n----- Question I -----")
total_high = 0
total_low = 0

for friend in workout_stats:
    subset = set("_Total")
    if subset.issubset(friend):
        if workout_stats[friend] > total_high:
            total_high = workout_stats[friend]
            friend_high = friend[:-6]
        else:
            total_low = workout_stats[friend]
            friend_low = friend[:-6]
print(f"Friend with highest total minutes: {friend_high}")
print(f"Friend with lowest total minutes: {friend_low}")
        