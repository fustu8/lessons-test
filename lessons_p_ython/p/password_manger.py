user_1 = "User1"
user_2 = "User2"
user_3 = "User3"
user_4 = "User4"
user1_pass = "1234"
user2_pass = "1221"
user3_pass = "1889"
user4_pass = "1334"


while True: 


    user_input = input("\nwhat is your user name : ")
    ask_user_pass = input(f"what is your pass for the account {user_input} : ")


    if user_input.lower() == user_1.lower():

        if ask_user_pass == user1_pass:
             print(f"welcome to your account, {user_1}")
             break
        else:
           print("Incorrect password.try again.")
           continue
        

    elif user_input.lower() == user_2.lower():

        if ask_user_pass == user2_pass :
            print(f"welcome to your account, {user_2}")
            break 
        else: 
            print("Incorrect password. Try again.")
            continue     


    
    elif user_input.lower() == user_3.lower():

        if ask_user_pass == user3_pass : 
            print(f"Welcome to your account,{user_3}")
            break
        else:
            print("Incorrect password. Try again.")
            continue 
    

    elif user_input.lower() == user_4.lower():
        
        if  ask_user_pass == user4_pass : 
            print(f"Welcome to your account , {user_4}")
            break

        else:
            print("Incorrect password . Try again.")
            continue 
    

    else:
        print("user name not found ")



###############################################################################################################################

 #profitional way 

user_database = {
    "user1": "1234",
    "user2": "1221",
    "user3": "1889", 
    "user4": "1334"
}



while True:

    user_input = input("\nEnter your username (or type 'exit to quit): ")

    if user_input.lower() == 'exit' : 
        print ("Goodbye!")
        break



    if user_input.lower() in user_database : 

        ask_user_pass = input(f"Enter the password for {user_input}: ")

        
        if ask_user_pass == user_database[user_input.lower()]:
            print(f"\nWelcome to your account, {user_input}!")
            break
        else: 
            print("Incorrect password. try again. ")

    else:
        print("User not found. Please try again")                







