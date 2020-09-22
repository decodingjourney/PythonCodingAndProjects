# ********************Last occurence of a delimeter in a string***********
# my_string = input('Enter the string you want to test: ')
# res = my_string.rsplit(' ', 1)
# split_res = my_string.split()
# print('original string is ', my_string)
# print('splitted string is ', res)
# print('Splitted string is ', split_res)

#******************display the vowels and counts of vowel in a text********

# my_string = input('Enter the string you want to test: ')
# vowel_list = ['a', 'e', 'i', 'o', 'u']
# vowel_counts = 0
# vowel_present = []
# for n in my_string:
#   if n.lower() in vowel_list:
#     vowel_present.append(n)
#     vowel_counts += 1

# vowels = list(set(vowel_present))
# print('total vowel present is ', vowels)
# print('vowel conts are ', vowel_counts)

#************Python program to swap characters in a string ************


# my_string = input('Enter the string you want to test: ')

# # my_string_lst = my_string.split()
# my_string_lst = list(my_string)
# dot_index = my_string.find('.')
# comma_index = my_string.find(',')
# if dot_index != -1 and comma_index != -1:
#   # temp = my_string_lst[dot_index]
#   # my_string_lst[dot_index] = my_string_lst[comma_index]
#   # my_string_lst[comma_index] = temp

#   my_string_lst[dot_index], my_string_lst[comma_index] = my_string_lst[comma_index], my_string_lst[dot_index]

# final_string = ''.join(my_string_lst)

# print(final_string)

#**************Python program to check if a string contains all letters of the alphabet*****************

# import string

# alphabet = set(string.ascii_lowercase)
# my_string = input('Enter the string you want to test: ')
# print(set(my_string.lower()) >= alphabet)

#***************Python program to count repeated characters in a string.*******

# my_string = input('Enter the string you want to test: ')
# mydict = {}

# for n in my_string:
#   if n in mydict:
#     mydict[n] += 1
#   else:
#     mydict[n] = 1
# lst = sorted(mydict, key=mydict.get, reverse=True)
# for c in lst:
#   if mydict[c] > 1:
#     print(c+' : ',mydict[c])

#*******************Python program to reverse words in a string**************************
# string_lst = my_string.split()

# reversed_string = ' '.join(reversed(string_lst))

# print(reversed_string)

# for str in my_string:
#   print(str)

#**********takes a list of words and returns the length of the longest one*******************************

# my_list = ["PHP", "Exercises", "Backend"]
# calculate_list = []

# for word in my_list:
#   calculate_list.append((len(word), word))

# calculate_list.sort(reverse=True)
# print(calculate_list[0][1])


  



