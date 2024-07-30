a= "rock"           #1
b= "scissor"         #2
c = "paper"          #3
while True:
    print("choose: \n a \n b \n c \n")
    x= input("Player 1 choice:")  #user one
    y= input("Player 2 choice:")  #user two1
    if  x== "a":
        if y== "c":
            print(" Paper covers Rock ! Player 2 wins")
        elif y== "b":
            print(" Rock smashes Scissor ! Player 1 wins")
        else:
            print("TIE")
    elif x=="b":
        if y=="c":
            print(" Scissor cuts Paper ! Player 1 wins")
        elif y=="a":
            print(" Rock smashes Scissor ! Player 2 wins")
        else:
            print("TIE")
    elif x=="c":
        if y=="a":
            print(" Paper covers Rock ! Player 1 wins")
        elif y=="b":
            print(" Scissor cuts Paper ! Player 21 win")
        else:
            print("TIE")
    p=input("Play Again? (Y/N)")
    if p.lower()== "n":
        break

    
