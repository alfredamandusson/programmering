import random

def get_user_choice():
    while True:
        user_choice = input("Välj sten, sax eller påse: ").lower()
        if user_choice in ['sten', 'sax', 'påse']:
            return user_choice
        else:
            print("Ogiltigt val. Var god välj sten, sax eller påse.")

def get_computer_choice():
    return random.choice(['sten', 'sax', 'påse'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "lika din donut"
    elif (user_choice == 'sten' and computer_choice == 'sax') or \
         (user_choice == 'sax' and computer_choice == 'påse') or \
         (user_choice == 'påse' and computer_choice == 'sten'):
        return "enkel vinst!"
    else:
        return "Förlust du e skit"

def main():
    print("Välkommen till Sten, sax, påse!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Datorn valde: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Vill du spela igen? (ja/nej): ").lower()
        if play_again != 'ja':
            break

if __name__ == "__main__":
    main()
