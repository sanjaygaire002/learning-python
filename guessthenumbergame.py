def guess_number():
    print("=====GUESS THE NUMBER GAME=====")
    import random
    computer_num= random.randint(1,100)
    while True:
        #to take input and show error in case of invalid input
        try:
            guess=int(input("Enter the guess ; "))
        except:
            print("-----INVALID INPUT-----") 
        #to check if the user guessed correctly
        if computer_num is guess:
            print("-----YOU WON----- ")
            break
        #condition in case the guess is less than the number and give appropriate hint 
        if computer_num> guess :
            diff= computer_num-guess
            if diff <10:
                print("-----GO HIGH-----")
            else:
                print("-----GO HIGHER-----")
        #condition in case the guess is higher than the number and give appropriate hint
        if guess>computer_num:
            diff= guess-computer_num
            if diff < 10:
                print("-----GO LOW-----")
            else:
                print("-----GO LOWER-----")
#calling the function            
guess_number()