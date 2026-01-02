import random,string
try:
    
    while True:
        def generate_password(level,length):
            if level == "easy":
                chars = string.ascii_letters
                password=''.join(random.choice(chars) for i in range(length))
            elif level == "medium":
                chars = string.ascii_letters + string.digits
                password=''.join(random.choice(chars) for i in range(length))
            elif level == "hard":
                chars = string.ascii_letters + string.digits + string.punctuation
                password=''.join(random.choice(chars) for i in range(length))  
            else:
                return "Invalid level. Please choose (easy||medium||hard)"
            return password 

        length = int(input("Enter the desired password length: "))
        level = str(input("Choose password complexity level (easy||medium||hard): "))
        print("Generated Password :", generate_password(level,length))
        while True:
            cont = input("Do you want to generate another password? (yes/no): ").lower()

            if cont == 'yes':
                break          
            elif cont == 'no':
                print("Thank you for using the password generator!")
                exit()         
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


except Exception as e:
    print("An error occurred:", e)