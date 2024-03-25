import random

def get_user_choice():
    while True:
        user_choice=input("välj sten, sax eller påse")
        if user_choice in ['sten', 'sax', 'påse']:
            return user_choice
        else:
            print("ogiltigt val. Var god välj sten, sax eller påse")  
        
def get_computer_choice():
    return random.choice(['sten','sax','påse'])

def determine_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        return "draw"
    elif (user_choice == 'sten' and computer_choice == 'sax') or \
         (user_choice == 'sax' and computer_choice == 'påse') or \
         (user_choice == 'påse' and computer_choice == 'sten'):
        return "full boxx nej nej nej vart ska brdern nex right hand peak fill pice 200"
    else:
        return " vänta vart e jag åhh gg blev fullboxad"
    
def main():
    print("welcome to rock paper scissors")
    while True:
        user_choise = get_user_choice()
        print(f"datorn valde: {'computer_choice'}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("u wanna play again? (ja/nej): ").lower()
        if play_again != 'ja':
            break

if __name__ == "__main__":
    main()
            