import random
num=random.randint(0,100) 
#print(num)
guess=1
count=0
print("Guess the number between 1 and 100!")
while(guess):
    try:
        user = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    count+=1

    if user==num:
        print("\nGuessed Correctly!!!")
        print(f'You took {count} tries')
        guess=0
    else:
        if (user>num):
            print("Smaller")
        else:
            print("Greater")
        print("Try Again!")
    