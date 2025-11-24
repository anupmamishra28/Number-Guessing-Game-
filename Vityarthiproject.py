import random
print(" WELCOME TO NUMBERS WORLD ")
print("Let's play a fun guessing game!")
print("Instructions:")
print(" I will think of a number between 1 and 100.")
print(" You have to guess it.")
print(" If you want to know the answer, type: answer")
secret_number = random.randint(1, 100)
while True:
    user_input = input("👉 Enter your guess: ")
    if user_input.lower() == "answer":
        print( "The secret number was:" , secret_number)
        print("Game Over!")
        break  
    guess = int(user_input)
    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break
    else:
        print("❌ Wrong guess, try again!")