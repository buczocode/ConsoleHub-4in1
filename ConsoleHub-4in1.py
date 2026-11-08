#____________________________________________________________
# PYTHON MINI PROJECT (ConsoleHub-4in1)
#____________________________________________________________


# STEP 1; (LOGIN PAGE)

def login():

    print(" ")
    print("                              === LOGIN PAGE ===")
    print(" ")

    # Demo credentials only (NOT real account security)
    correct_username = "python"
    correct_password = "@python"

    username = input(" • Enter the username : ").strip().lower()
    print(" ")

    password = input(" • Enter the password : ").strip()
    print(" ")

    if username == correct_username and password == correct_password:

        print(" ")
        print("                         ---🎉 Login Successful !! ---")
        print(" ")
        print(" ")
        print("        username : python  ✅")
        print("        password : @python ✅ ")
        print("_" * 83)
        return True

    else:

        print(" ")
        print("             ____Invalid detail____")
        print(" ")
        print("_" * 83)
        return False


# STEP 2; (CHOOSING THE OPTION)

def main_menu():

    while True:

        print(" ")
        print("          • Choose the options :")
        print(" ")
        print("      - opt 1: Guess Game")
        print("      - opt 2: Funny Fake News")
        print("      - opt 3: Random Password Generator")
        print("      - opt 4: Age Calculator")
        print("      - opt 5: Quit")
        print(" ")

        option_choice = input(" • Choose the option : ").strip().lower()

        print(" ")

        if option_choice == "quit" or option_choice == "5":

            print(" ")
            print("          ___Program completely End___")
            print("_" * 83)
            break

        elif option_choice == "1":

            guess_game()

        elif option_choice == "2":

            funny_fake_news()

        elif option_choice == "3":

            password_generator()

        elif option_choice == "4":

            age_calculator()

        else:

            print(" ")
            print("          ____Invalid detail____")
            print(" ")


# STEP 3; (GUESS GAME)

def guess_game():

    import random

    print(" ")
    print("                 !! Guess Game !!")
    print(" ")
    print("             ____________________")
    print(" ")

    print("Loading...")

    target = random.randint(1, 10)

    while True:

        user_choice = input(" • Enter the choice (1-10 or quit) : ").strip().lower()

        if user_choice == "quit":

            print(" ")
            print("                 --- GAME OVER ---")
            print(" ")
            print("       The correct number was:", target)
            print("_" * 83)
            break

        # Handle non-numeric input
        try:
            user_choice = int(user_choice)

        except ValueError:

            print(" ")
            print("       Please enter a valid number!")
            print(" ")
            continue

        # Handle numbers outside the game range
        if user_choice < 1 or user_choice > 10:

            print(" ")
            print("       Enter a number between 1 and 10!")
            print(" ")
            continue

        if target > user_choice:

            print(" ")
            print("       You chose a smaller number. Try again!")
            print(" ")

        elif target < user_choice:

            print(" ")
            print("       You chose a greater number. Try again!")
            print(" ")

        elif target == user_choice:

            print("\n")
            print("               === CONGRATULATION🎉 !!!, You won it ===")
            print(" ")
            print("_" * 83)
            break


# STEP 4; (FUNNY FAKE BREAKING NEWS)

def funny_fake_news():

    import random

    print(" ")
    print("              !! Funny Fake News !!")
    print(" ")
    print("       ______________________________")
    print(" ")

    subjects = [
        "The Boy",
        "The Bollywood Actress",
        "The School's Principal",
        "The Police Woman",
        "The Maths Teacher"
    ]

    actions = [
        "did the poti",
        "failed the exam",
        "snake dancing",
        "is crying",
        "started loving"
    ]

    objects = [
        "in their pant",
        "with '0' marks",
        "on the tree",
        "for just one chocolate",
        "to dog"
    ]

    while True:

        subject = random.choice(subjects)
        action = random.choice(actions)
        object = random.choice(objects)

        headline = f" BREAKING NEWS : {subject} {action} {object}"

        print("\n" + headline)

        user_input = input(
            " • Do you want more? (yes / no or quit) : "
        ).strip().lower()

        if user_input == "yes":

            continue

        elif user_input == "quit" or user_input == "no":

            print(" ")
            print(" ")
            print("                 === NEWS End ===")
            print("_" * 83)
            break

        else:

            print(" ")
            print("       Please enter yes, no or quit.")
            print(" ")


# STEP 5; (RANDOM PASSWORD GENERATOR)

def password_generator():

    import secrets
    import string

    print(" ")
    print("          !! Random Password Generator !!")
    print(" ")
    print("       ______________________________")
    print(" ")

    letters_A = list(string.ascii_uppercase)
    letters_a = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    all_char = letters_A + letters_a + numbers + symbols

    while True:

        try:

            pass_length = input(
                " • Enter password length (minimum 8 and maximum 20) : "
            ).strip()

            pass_length = int(pass_length)

        except ValueError:

            print(" ")
            print("       Please enter a valid number!")
            print(" ")
            continue

        if pass_length < 8:

            print(" ")
            print("       Minimum password length is 8!")
            print(" ")
            continue
        if pass_length > 20:
            print(" ")
            print("      Maximum password length is 20!")
            print(" ")
            continue

   
        password_chars = [
            secrets.choice(all_char)
            for i in range(pass_length)
        ]

        password = "".join(password_chars)

        print(" ")
        print("       Loading...")
        print(" ")
        print("       ... Your generated password is :", password, "...")
        print(" ")

        user_choice = input(
            " • Wanna More or Quit? (more / quit / no) : "
        ).strip().lower()

        if user_choice == "more":

            continue

        elif user_choice == "quit" or user_choice == "no":

            print(" ")
            print("          === Password Generator OFF ===")
            print("_" * 83)
            break

        else:

            print(" ")
            print("       Invalid detail. Returning to menu.")
            print(" ")
            break


# STEP 6; (AGE CALCULATOR)

def age_calculator():

    from datetime import date

    print(" ")
    print("                 === Age Calculator ===")
    print(" ")
    print("       ______________________________")
    print(" ")

    try:

        year = int(input(" • Enter your birth year (A.D) : "))
        print(" ")

        month = int(input(" • Enter your birth month : "))
        print(" ")

        day = int(input(" • Enter your birth day : "))
        print(" ")

        today = date.today()

        # Validate the entered birth date
        birth_date = date(year, month, day)

        # Prevent future birth dates
        if birth_date > today:

            print(" ")
            print("       Birth date cannot be in the future!")
            print(" ")
            return

        age = today.year - birth_date.year

        # Check whether the birthday has happened this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):

            age = age - 1

        print("_" * 83)
        print(" ")
        print(f" • Current date is : {today}")
        print(" ")
        print(f" • Your birth date is : {birth_date}")
        print(" ")
        print(f"       ... You are now {age} years old ...")
        print(" ")
        print("_" * 83)

    except ValueError:

        print(" ")
        print("       ____Invalid date! Please try again.____")
        print(" ")
        print("_" * 83)

print(" ")
print("_" * 83)

if login():

    main_menu()

else:

    print(" ")
    print("       Program stopped because login failed.")
    print(" ")
    print("\n")
    print("_"*83)

#____________________________________________________________
# END OF PYTHON MINI PROJECT HUB
#____________________________________________________________
