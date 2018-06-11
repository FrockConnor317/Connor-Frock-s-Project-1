# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

Name = raw_input('What is your name?')
Grade = int(raw_input("what grade are you in?"))
print  str(Name[0].upper() + Name[1:6].lower()) + ",you will graduate from high school in " + str(13- Grade) + " years"
# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

current_day = 11
current_month= 6
user_month = int(raw_input("Enter the number of your birth month: "))
user_day = int(raw_input("enter the number of your birth day: "))
q= user_month-current_month
a= 12-(current_month-user_month)
b= user_day-current_day
d= 30 - (current_day-user_day)
if user_month > current_month:
    print str(q) + "months and"
else:
    print str(a) + " months and"
if user_day >= current_day:
   print str(b) + " days until birthday"
else:
    print str(d) + "days until birthday"



# If you complete extensions, describe your extensions here!