from datetime import datetime  # Importing the Library and then the SubModule in that Library

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,  # odds is a list [], but also a variable
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range (5):
    right_this_minute = datetime.today().minute  # right_this_minute is a variable and it is an assigned to datetime.today().minute

    if right_this_minute in odds:  # if will evaluate to true or false. 'in' operator checks if one thing is inside another
        print("This minute seems a little odd.")  # print function displays a standard output
    else:  # if 'if' is false, then else will execute
        print("Not an odd minute.")

    # There is no 'elseif' in Python, only 'elif'. i can have as many 'elif's as I would like.

checkDay = datetime.today().weekday()  # Create a variable checking the day of the week using the function weekday() from the library datetime, imported at the top of the file
today = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
         'Sunday']  # create a List variable called today and assign it the days of the week.

if checkDay in today == 'Saturday':  # if the Day in the list(variable) today is Saturday, print the following
    print("Have a Party!")
elif checkDay == 'Sunday':  # if the Day in the list(variable) today is Sunday, print the following
    print('Rest & Relax')
else:  # if the Day is neither Saturday nor Sunday, print the following.
    print('Go to Work')
