from choice import random_choice
from art import logo
from art import stages

randlen = len(random_choice)

life = 6
game = False

display = []
for i in range(randlen):
    display+= "_"
print(display)

while not game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed{guess}")
        
    for i in range(randlen):
        let = random_choice[i]
        
        if let == guess:
            display[i] = let
    if guess not in random_choice:
        life -= 1
        print("the letter you guess does not meet in the word")
        
        if life == 0:
            print("You lose")
            game = True
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        print("You win")
        game = True
        
    print(stages[life])