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
    ask_user_pass = input ("what is your pass for")
    
    if user_input == user_1.title():
        print(ask_user_pass,user_input)
        
    if user_input == user_2.title():
        print(ask_user_pass,user_input)
        
    if user_input == user_3.title(): 
        print(ask_user_pass,user_input)
        
    if user_input == user_4.title():
        print(ask_user_pass,user_input)
        
    
    else :
        print("user unidentified try again") 
        continue

   
    



    
