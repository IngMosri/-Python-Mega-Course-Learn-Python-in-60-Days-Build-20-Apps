#!/usr/bin/env python3
print("Enter a TO-DO list: ")

Userinput1 = "Enter what do you want to add in your TO-DO list:\n"

UserTodoList = []

while True:
    item = input(Userinput1)
    UserTodoList.append(item)
    print(UserTodoList)
