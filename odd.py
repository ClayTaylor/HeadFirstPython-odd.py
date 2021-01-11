from datetime import datetime #Importing the Library and then the SubModule in that Library

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, #odds is a list []
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute #right_this_minute is a variable and it is an assigned to datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")


print(odds[3])