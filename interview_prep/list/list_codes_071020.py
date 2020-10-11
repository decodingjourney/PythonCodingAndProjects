import random

my_list = [1, 4, 5, 2, 7]
# Method 1:-
# print('original list is ', my_list)
# rand_num = random.choice(my_list)
# print('random num is ', rand_num)

#Method 2 :-
# rand_idx = random.randrange(len(my_list), step=2)
# rand_num1 = my_list[rand_idx]
# print('random num is ', rand_num1)

#Method 3 :-
# rand_idx = random.randint(0, len(my_list)-1)
# rand_num = my_list[rand_idx]
# print('random num is ',rand_num)

# #Method 4 :-
# rand_idx = int(random.random() * len(my_list))
# print(my_list[rand_idx])
