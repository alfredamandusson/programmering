import random

def get_user_choise():
    while True:
        user_choise=input("välj sten, sax eller påse")
        if user_choise in ['sten', 'sax', 'påse']:
            return user_choise
else:
    print("ogiltigt val. Var god välj sten, sax eller påse")  
        
