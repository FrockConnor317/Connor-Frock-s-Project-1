# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
x = int(raw_input("Enter a number that you want a list to end before:"))
for list1 in range(0,x):
    print list1









#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different size

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for item in b:
    for item_c in c:
        if item == item_c:
            print item





#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
z= "a"
for z in d:
    if z== "a":
        print "*"
    else:
        print z











#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.
j=str(raw_input("Type a word and I will determine if it's a palindrome"))
list_one = []
list_two = []
str = j
for letter in str:
   list_one.append(letter)
   list_two.append(letter)
list_two.reverse()
print list_one
print list_two
if list_one == list_two:
    print "your word is a palendrome!"
else:
    print "your word is not a palendrome"


