from getpass import getpass as gp
print("ROCK 🪨  PAPER📄 SCISSORS ✂️ " )
print("-----------------------------------")
counter=0
print()
times=int(input("how many time you want to play a game "))
print()
while counter<times:
    print("select your move (R,P or S)")
    print ()
    player1=gp("player1 >>")
    print()
    player2=gp("player2 >>")
    print()
    if player1=="R":
       if player2=="R":
         print("you both choosed rock, it's a tie")
       elif player2=="P":
         print("player2 wins  hurrayyy!!")
       elif player2=="S":
        print("player1 wins  hurrayyy!!")
       else:
        print("invalid move by player2")
    elif player1=="P":
       if player2=="P":
         print("you both choosed paper, it's a tie")
       elif player2=="R":
         print("player1 wins  hurrayyy!!")
       elif player2=="S":
         print("player2 wins  hurrayyy!!")
       else:
         print("invalid move by player2")
    elif player1=="S":
       if player2=="S":
          print("you both choosed scissors, it's a tie")
       elif player2=="R":
         print("player2 wins  hurrayyy!!")
       elif player2=="P":
         print("player1 wins  hurrayyy!!")
       else:
         print("invalid move by player2")
    else:
      print("invalid move by player1")
counter+=1

