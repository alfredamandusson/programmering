import random

# hej välkommen
print("välkommen till sten, sax, påse")
player_count = 0
computer_count= 0
play_again = "ja"
while play_again == "ja":
    # välj på sten sax eller påse
    user_choice=input("välj sten, sax eller påse")
    # datorn väljer
    # slumpa ett tal 0, 1, 2
    computer_choice =  random.choice(['sten','sax','påse'])
    # 0 sten
    # 1 sax
    # 2 påse
    # skriv ut vad datorn valde
    print(computer_choice)
    # vem vinner?
    if user_choice==computer_choice:
        print("draw")
    elif (user_choice == 'sten' and computer_choice == 'sax') or \
            (user_choice == 'sax' and computer_choice == 'påse') or \
            (user_choice == 'påse' and computer_choice == 'sten'):
        print("w")
        player_count = player_count+1
    else:
        print("förlust")
        computer_count = computer_count+1
    # om spelaren valde sten och datorn valde sten
    # lika
    # om spelaren valde sten och datorn valde sax
    # spelaran vann
    # om spelaren valde sten och datorn valde påse
    # datorn vann

    # spela igen
    print("dina poäng", player_count)
    print("datorpoäng" ,computer_count)
    play_again=input("vill du köra igen ja eller nej?")

    if play_again== 'ja':
        print("kul")
    