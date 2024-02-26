import random as rd
print("""
      
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀█░█▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ 
      ▐░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌    ▐░▌     
      ▐░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌    ▐░▌     
      ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌    ▐░▌     
      ▐░▌    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌    ▐░▌     
      ▐░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌    ▐░▌     
 ▄▄▄▄▄█░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄ 
▐░░░░░░░▌    ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀      ▀         ▀  ▀         ▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                             
 ▄▄▄▄▄▄▄▄▄▄   ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄             
▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌            
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌            
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌      ▐░▌    ▐░▌       ▐░▌            
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌      ▐░▌    ▐░█▄▄▄▄▄▄▄█░▌            
▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌      ▐░▌    ▐░░░░░░░░░░░▌            
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀       ▐░▌    ▐░█▀▀▀▀▀▀▀█░▌            
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌        ▐░▌    ▐░▌       ▐░▌            
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌  ▄▄▄▄▄█░▌    ▐░▌       ▐░▌            
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░▌    ▐░▌       ▐░▌            
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀      ▀         ▀             
                                                                             

      """)
remaining_money=1000
print("""
      WELCOME 
      TO OUR CASINO
      NOW,YOU ARE GOING TO PLAY 'JHANDI BURJA'
      IT IS A VERY COMMON GAME IN NEPAL
      I Ran Dekoc Horo WILL BE GUIDING YOU 
      THROUGH THE GAME.
      
      
      ENJOY THE GAME
      
      
      BEST OF LUCK
      """)
def dices_roll(bet_dice):
    winrate=0
    dice=['JHANDI','BURJA','ITTA','PAAN','HUKUM','CHIDI']
    d1=rd.choice(dice)
    d2=rd.choice(dice)
    d3=rd.choice(dice)
    d4=rd.choice(dice)
    d5=rd.choice(dice)
    d6=rd.choice(dice)    
    print(f"""
          THE DICES ARE:
          {d1}
          {d2}
          {d3}
          {d4}
          {d5}
          {d6}
          """)
    
    random_dice_set=[d1,d2,d3,d4,d5,d6]
    for i in random_dice_set:
        if bet_dice== i:
            winrate+=1
    print(winrate)
    return winrate
def check():
        pass



def play_again():
    check()
    yesno=input("DO YOU WANT TO BET AGAIN   ").upper()
    if yesno=="Y":
        global remaining_money
        main()
    else:
        print(""""
              THANK YOU FOR PLAYING
              PLAY AGAIN SOON
               ---JHANDI BURJA------
              CREATED BY SANJAY GAIRE
              """)


def bet():
    global remaining_money
    print("""
          Jhandi
          Burja
          Itta
          Paan
          Hukum 
          Chidi
        """)
    dice=['JHANDI','BURJA','ITTA','PAAN','HUKUM','CHIDI']
    bet_dice=None
    while bet_dice not in dice:
        bet_dice=input("WHAT DO YOU WANT TO BET ON???---  ").upper()
    while True :
        bet_money=int(input("HOW MUCH WOULD YOU LIKE TO BET ON IT?---   "))
        if bet_money < 0:
            print("DON'T TRY TO SCAM ME")
            print("I am going to ask again")
            continue
        elif bet_money> remaining_money:
            print("""YOU DONT HAVE ENOUGH FUNDS
                  PLEASE ENTER AGAIN """)
            continue
        elif bet_money==0:
            print("YOU COWARD!")
            break
        else:
            remaining_money= remaining_money- bet_money
            break
        
    return bet_dice,bet_money


def main():
    global remaining_money
    if(remaining_money==0):
        print("""
              you lost all your money
              you loose.
              I think you are out of luck this time.
              Better luck next time
              """)
        return
    while remaining_money>0: 
        winrate=0
        print(f"REMAINING MONEY=  {remaining_money}")     
        bet_dice,bet_money=bet()
        
        winrate=dices_roll(bet_dice)
        win= winrate*bet_money
        if winrate>1:
            print(f"REMAINING MONEY AFTER BET=  {remaining_money}") 
            print(f"""
                Congratulation you win
                you bet Rs.{bet_money} on {bet_dice} and 
                it came out {winrate} times.
                so you get Rs.{win} in return.""")
            remaining_money=remaining_money + win
            print(f"REMAINING MONEY=  {remaining_money}") 
        elif winrate==1:
            print(f"REMAINING MONEY AFTER BET=  {remaining_money}")
            print(f"""
                
                
                It seems like {bet_dice} came out
                only once. so you will not get any money
                in return.
                better luck next time
                
                """)
            print(f"REMAINING MONEY=  {remaining_money}") 
            
        else:
            print(f"REMAINING MONEY AFTER BET=  {remaining_money}")
            print("""
                
                
                It seems that your dice is not in the roll
                so,
                    Best of luck for next time.
                    
                    
            """)
            print(f"REMAINING MONEY=  {remaining_money}") 
        play_again()
    
main()
