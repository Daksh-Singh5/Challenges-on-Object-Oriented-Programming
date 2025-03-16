#Write a program to create a quiz related to multiple fruits using object-oriented programming in Python. Create a class that consists of - 1. a constructor with a dictionary of fruits and respective colours 2. a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly.
import random as r
class fruitgame:
    def __init__(self,):
        self.fruit = {"Apple" : "red","Orange":"orange","Watermelon":"green","Banana" : "yellow","guava":"green"}

    def quizz(self):
        while True:
            fruit,colour = r.choice(list(self.fruit.items()))
            print("What is the colour of",fruit)
            answer = input(":")
            if answer.lower() == colour:
                print("Your Right")
            else:
                print("Your Wrong")
            chance = int(input("Enter 0 to play again else enter 1: "))
            if(chance):
                break

print("welcome to fruit quiz")
fq = fruitgame()

fq.quizz()
