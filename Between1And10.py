'''
Between 1 and 10
Pawelski
2/2/2025

Instructions:
1.  What does this program do?
2.  When you enter a number less than 1, the program
    displays the message "That number is not between
    1 and 10.". Yet, when you enter a number greater
    than 10, the program displays no message. Why? If
    you cannot figure it out, add a breakpoint on line 21,
    run the program in debugging mode, enter a number
    bigger than 10, and step through the program.
3.  Modify the program by adding an else on the inner if
    statement that also prints the message "That number is
    not between 1 and 10.".
'''

number = input("Enter a number >> ")
if number >= 1:
    if number <= 10:
        print("That number is between 1 and 10.")
else:
    print("That number is not between 1 and 10.")