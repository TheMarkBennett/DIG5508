#%%
import random

randomNumber = random.randint(1,100)
print(randomNumber)

def numberChoice(userNumber):
    if userNumber > randomNumber:
        answer = 'Your guess is too high'
    if userNumber < randomNumber:
         answer = 'Your guess is too low'
    if userNumber == randomNumber:
        answer = 'You guessed the correct answer'
    return answer
    

#%%
