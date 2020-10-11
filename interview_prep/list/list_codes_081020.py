from collections import Counter
# def is_sublist(l, s):
#     sub_set = False
#     if s == []:
#         sub_set = True
#     elif s == l:
#         sub_set = True
#     elif len(s) > len(l):
#         sub_set = False
#     else:
#         for i in range(len(l)):
#             if l[i] == s[0]:
#                 n = 1
#                 while n < len(s) and l[i + n] == s[n]:
#                     n += 1
#                 if n == len(s):
#                     sub_set = True
#     return sub_set


# Wrong Code :-
# def sublist(lst1,lst2):
#     for i in range(len(lst1)):
#         if lst1[i] not in lst2:
#             return False
#         for j in range(len(lst2)):
#             if (lst1[j] in lst2) and (lst2.index(lst1[i+1]) > lst2.index(lst1[i])):
#                 return True

# Second Method
# def removeElement(sub, lst):
#     for i in range(len(lst) - len(sub) + 1):
#         for j in range(len(sub)):
#             if lst[i + j] != sub[j]:
#                 break
#         else:
#             return True
#     return False

# Third Method :-
# def removeElements(sub, lst):
#     n = len(sub)
#     return any(sub == lst[i:i+n] for i in range(len(lst) - n + 1))

# Forth Method
# def removeElements(sub, lst):
#     return ','.join(map(str, sub)) in ','.join(map(str, lst))


# my_list = [2,4,3,5,7]
# # count_list = Counter(my_list)
# # print(count_list)
# my_sublist = [4,3]
#
# my_sec_sublist = [4,7]
#
# # True Statement
# print(removeElements(my_sublist, my_list))
#
# # False Statement
# print(removeElements(my_sec_sublist, my_list))