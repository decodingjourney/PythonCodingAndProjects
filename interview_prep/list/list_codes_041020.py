################ sorting a list based on the tuple element inside the list ##################
# def sort_list_tuple(lst):
#     '''
#     Method 1
#     :param lst:
#     :return:
#     '''
#     # lst.sort(key= lambda x : x[1], reverse=True)
#
#     '''
#     Method 2
#     '''
#     length = len(lst)
#     for i in range(length):
#         for j in range(length - i - 1):
#             if lst[j][1] > lst[j + 1][1]:
#                 temp = lst[j]
#                 lst[j] = lst[j + 1]
#                 lst[j + 1] = temp
#     return lst

########################Removing duplicates from the list ################
# '''
# Method 1
# using set and list
# '''
# '''
# Method 2
# again using set and list
# '''
# def remove_dup(lst):
#     unique_list = set()
#     dup_list = []
#     for num in lst:
#         if num not in unique_list:
#             unique_list.add(num)
#             dup_list.append(num)
#     return dup_list
######################## print a specified list after removing the 0th, 4th and 5th ################
# '''
# method 1
# '''
# def specific_list(lst):
#     mylist = [num  for inde,num in enumerate(lst) if inde not in [0,4,5]]
#     return mylist

########################## convert a list of characters into a string #####################
# def convert_list_string(lst):
#     return ''.join(lst)


########################## Flatten the shalow list ##########################
# def flatten_list(lst):
#     final_list = []
#     for item in lst:
#         for i in range(len(item)):
#             final_list.append(item[i])
#     return final_list

#####################  Largest, Smallest, Second Largest, Second Smallest in a List #################
def calculate(lst):
    largest = lst[0]
    smallest = lst[0]
    largest2 = None
    smallest2 = None
    for item in lst[1:]:
        if item >largest:
            largest2 = largest
            largest = item
        elif largest2 == None or largest2 < item:
            largest2 = item
        if item < smallest:
            smallest2 = smallest
            smallest = item
        elif smallest2 == None or smallest2 > item:
            smallest2 = item

    print("Largest element is:", largest)
    print("Smallest element is:", smallest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", smallest2)

list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
calculate(list1)