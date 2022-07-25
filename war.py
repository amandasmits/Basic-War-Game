import random

player1 = input("please enter the name of player 1") 
player2= input("please enter the name of player 2")



cont = True #while loop condition

def displayname(playercard):
    '''renames the card if it's a face card or an ace'''
    if playercard == 11:
        playercard= "J"
    elif playercard == 12:
        playercard = "Q"
    elif playercard == 13:
        playercard = "K"
    elif playercard == 14:
        playercard = "A"
    elif playercard == 15:
        playercard = "Joker"
    return playercard

def player1win():
    print(player1, "wins this round")
    

def player2win():
    print(player2, "wins this round")
    

def warfunction():
    print()

player1score = int(0) #initializes the score for player 1 
player2score = int(0) #initializes the score for player 2 

deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15]
while (cont ==True):


    player1index=random.randint(0, (len(deck)-1)) #chooses an index to pick from the deck
    player1card=deck[player1index] #pick card from deck using randomly generated index
    player1cardfinal = displayname(player1card) #renames the card if it's a face card
    print(player1, ": your card is a(n)", player1cardfinal) #prints what player 1's card is

    player2index=random.randint(0, (len(deck)-1)) #chooses an index to pick from the deck  
    player2card=deck[player2index] #pick card from the deck using randomly generated index
    player2cardfinal = displayname(player2card) #renames card if it's a face card
    print(player2, ": your card is a(n)", player2cardfinal) #prints what player 2's card is 

    if (player1card>player2card):
        player1win()
        player1score +=1
        print(player1, "has", player1score, "points, and", player2, "has", player2score, "points" )
    elif (player2card>player1card):
        player2win()
        player2score +=1
        print(player1, "has", player1score, "points, and", player2, "has", player2score, "points" )
    else:
        war = True
        warcounter =1 #counts how many rounds the war went
        while (war == True):
            player1index=random.randint(0, (len(deck)-1))
            player1card=deck[player1index]
            player1cardfinal = displayname(player1card)
            print(player1, ": your card is a(n)", player1cardfinal)

            player2index=random.randint(0, (len(deck)-1))
            player2card=deck[player2index]
            player2cardfinal = displayname(player2card)
            print(player2, ": your card is a(n)", player2cardfinal)

            if (player1card >player2card):
                print(player1, "you win this war!!!! Rub it in", player2, "'s face")
                player1score+=5
                war = False
            elif(player2card>player1card):
                print(player2, "wins this war!!!!! You suck", player1)
                player2score+=5
                war=False
            else:
                print("THE WAR CONTINUES")
                warcounter+=1
        print("phew, the war only took", warcounter, "rounds")
        print(player1, "has", player1score, "points, and", player2, "has", player2score, "points" )

    
    keepgoing = input("do you want to keep playing?")
    if (keepgoing == "no") or (keepgoing == "n") or (keepgoing =="nope"):
        break

print("the final score was ", player1score, "for", player1, "and", player2score, "for", player2) 
if (player1score>player2score):
    print(player1, "won!!!! Sucks 2 be", player2)
elif(player2score>player1score):
    print(player2,"won!!! I bet",player1, "is really jealous")
else:
    print("YOU'RE TIED! I guess the war will have to continue some other way")
