user_1 = "user1"
user_2 = "user2"
user_3 = "user3"
user_4 = "user4"
user1_pass = "1234"
user2_pass = "1221"
user3_pass = "1889"
user4_pass = "1334"

while True:

    user_input = input("what is your user name : ") 
    
    if user_input == user_1.title():
        print("what is your password for user_1")
        
    if user_input == user_2.title():
        print("what is your password for user_2 ")
        
    if user_input == user_3.title(): 
        print("what is your password for user_3")
        
    if user_input == user_4.title():
        print("what is your password for user_4") 
    
    else :
        print("user unidentified try again") 
        continue

    pass_input = input("")

    if pass_input == user1_pass : 
        print("welcome the your account")



    
