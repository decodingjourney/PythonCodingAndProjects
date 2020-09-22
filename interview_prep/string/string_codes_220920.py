string = input('Enter the string you want to test: ')
new_str = []
ch = string[0]
new_str.append(ch)
for n in range(1, len(string)):
  if string[n] == ch:
    new_str.append('$')
  else:
    new_str.append(string[n])
final = ''.join(new_str)
print(final)
Method 2
ch = string[0]

string = string.replace(ch, '$')
str1 = ch + string[1:]
print(str1)

***********************************************
string = input('Enter the string you want to test: ')
n_find = string.find('not')
p_find = string.find('poor')
if p_find > n_find and n_find != -1 and p_find != -1:
  final_str = string.replace(string[n_find:p_find+len('poor')], 'good')
  print(final_str)
else:
  print(string)


**************************************************Python program to find the first non-repeating character in given string*************************

def mycalc(string):
  mydict = {}
  mylist = []
  for c in mystring:
    if c in mydict:
      mydict[c] += 1
    else:
      mydict[c] = 1
      mylist.append(c)

  for n in mylist:
    if mydict[n] == 1:
      return n
mystring = input('Enter the string you want to test')
myresult = mycalc(mystring)
print(myresult)



*********************************Find the first repeated character in a given string************************************



def mycalc(string):
  mydict = {}
  dup_list = []

  for c in mystring:
    if c in mydict:
      mydict[c] += 1
      dup_list.append(c)
    else:
      mydict[c] = 1

  for n in dup_list:
    if mydict[n] > 1:
      return n


def mycalc1(str):
  for index, c in enumerate(str):
    if str[:index+1].count(c) > 1:
      return c

mystring = input('Enter the String to be tested : ')
final = mycalc1(mystring)
print(final)






