import random
cnum=list(str(random.randint(100,999)))
#print(cnum)
life=12
logo3="""
                      _                      
                     | |                     
  _   _  ___  _   _  | | ___   ___  ___  ___ 
 | | | |/ _ \| | | | | |/ _ \ / _ \/ __|/ _ \
 | |_| | (_) | |_| | | | (_) | (_) \__ \  __/
  \__, |\___/ \__,_| |_|\___/ \___/|___/\___|
   __/ |                                     
  |___/                                      
"""


logo4="""
                               _       
                              (_)      
  _   _  ___  _   _  __      ___ _ __  
 | | | |/ _ \| | | | \ \ /\ / / | '_ \ 
 | |_| | (_) | |_| |  \ V  V /| | | | |
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_|
   __/ |                               
  |___/                                
"""


logo="""   
  ____                _____   ______   _      
 |  _ \      /\      / ____| |  ____| | |     
 | |_) |    /  \    | |  __  | |__    | |     
 |  _ <    / /\ \   | | |_ | |  __|   | |     
 | |_) |  / ____ \  | |__| | | |____  | |____ 
 |____/  /_/    \_\  \_____| |______| |______|
                                              
                                              
"""

logo2="""
   _____ ____  _   _  _____ _____        _______ _    _ _            _______ _____ ____  _   _ 
  / ____/ __ \| \ | |/ ____|  __ \    /\|__   __| |  | | |        /\|__   __|_   _/ __ \| \ | |
 | |   | |  | |  \| | |  __| |__) |  /  \  | |  | |  | | |       /  \  | |    | || |  | |  \| |
 | |   | |  | | . ` | | |_ |  _  /  / /\ \ | |  | |  | | |      / /\ \ | |    | || |  | | . ` |
 | |___| |__| | |\  | |__| | | \ \ / ____ \| |  | |__| | |____ / ____ \| |   _| || |__| | |\  |
  \_____\____/|_| \_|\_____|_|  \_/_/    \_|_|   \____/|______/_/    \_|_|  |_____\____/|_| \_|
                                                                                               
      
      
                                                                                               
"""
print(logo)
print("""
              =====WELCOME TO BAGEL GAME=====
      IN THIS GAME YOU, I WILL RANDOMLY SELECT A WORD BETWEEN ONE(1)
      AND THOUSAND(1000) AND YOU WILL HAVE TO GUESS THE NUMBER.
      YOU WILL BE  GIVEN 12 CHANCES TO FIND OUT THE NUMBER.
      BASED ON YOUR INPUT I WILL PROVIDE YOU WITH HINTS ACCORDING TO
      YOUR PREVIOUS GUESS.
      
      1). PICO= ONE DIGIT IS CORRECT BUT IN WRONG PLACE
      
      2). FERMI= ONE DIFIT IS IN CORRECT PLACE
      
      3). BAGELS = NO DIGIT IS CORRECT 
      
      
      """)
       
def main(cnum):
    global life
    while life!=0:
        life-=1
        unum=list(str(input("ENTER YOUR GUESS;-   ")))
        print(unum)
        fermi=0
        pica=0
        '''for i in range(3):
            if int(unum[i])==int(cnum[i]):
                fermi +=1
            for j in range(3):
                if i!=j:
                    if int(unum(i))==int(cnum(j)):
                        pico+=1'''
        
        i=0 
        j=0
        for c in cnum:
            i+=1
            j=0
            for u in unum:
                j+=1
                if c == u and i==j:
                    fermi+=1  
                elif c ==u:
                    pica += 1
                
                    

       
              
        if fermi>=1:
            print("=====FERMI")
            print(f"====LIFE= {life}")
        elif pica>=1:
            print("=====PICO")
            print(f"====LIFE= {life}")
        else:
            print("=====BEGELS")
            print(f"====LIFE= {life}")
        '''print(fermi)
        print(pica)'''
        if (fermi==3):
            print(logo2)
            print(logo4)
            break         
        if life==0:
            print(f"====THE ANS WAS {cnum}")
            print(logo3)
            break
        
    
main(cnum)
