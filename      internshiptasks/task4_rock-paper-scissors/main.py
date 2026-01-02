import random
try:
    while True:
        choice=("rock","paper","scissors")
        user_choice=None
        bot=random.choice(choice)
        while user_choice not in choice:
            user_choice=input("Enter rock, paper or scissors: ").lower()
            if user_choice not in choice:
                print("Invalid choice, please try again.")
        print("Bot chose:", bot)
        if user_choice==bot:
            print("It's a tie!")
        elif (user_choice=="rock" and bot=="scissors") or (user_choice=="paper" and bot=="rock") or (user_choice=="scissors" and bot=="paper"):
            print("You win!")
        else:
            print("Bot wins!")  
        play_again=input("Do you want to play again? (yes/no): ").lower()
        if play_again=="yes":
            continue
        elif play_again=="no":
            print("Thanks for playing!")
            exit()


except Exception as e:
    print("An error occurred:", e)

