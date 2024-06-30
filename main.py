#!/usr/bin/env python3
print("Enter a TO-DO list: ")
Userinput1 = input( "Enter what do you want to add in your TO- DO list:\n")
Userinput2 = input( "Enter what do you want to add in your TO- DO list:\n")
Userinput3 = input( "Enter what do you want to add in your TO- DO list:\n")
inputlist = [Userinput1,Userinput2,Userinput3]

for valores, user_input in enumerate(inputlist):
     print(f"{valores}: {user_input}")
print ("Your task was save correctly :D")

   

