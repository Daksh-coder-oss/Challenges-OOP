#Write a program to create a quiz related to multiple fruits using object-oriented programming in Python.
#  Create a class that consists of - 
# 1. a constructor with a dictionary of fruits and respective colours 
# 2. a function to execute the quiz. 
# Here, the fruit will be chosen at random from the dictionary.
#  Then ask the user to enter the colour of that fruit. 
# Evaluate the answer and display the result accordingly.
import random
class Fruits:
    def __init__(self):
        self.fruit={"apple":"red","orange":"orange","banana":"yellow","watermelon":"green and black"}
    def quiz(self):
        while True:
            fruit,colour=random.choice(list(self.fruit.items()))
            answer= input(f"What is the colour of the {fruit}")
            if answer.lower()==colour:
                print("Correct answer")
            else:
                print("Wrong answer")
            option=int(input("If you want to continue press 0,if you want to exit press 1"))
            if option:
                break
print("Welcome to fruit quiz")
fr=Fruits()
fr.quiz()
            
