user_1 = "User1"
user_2 = "User2"
user_3 = "User3"
user_4 = "User4"
user1_pass = "1234"
user2_pass = "1221"
user3_pass = "1889"
user4_pass = "1334"


user_input = input("what is your user name : ")
ask_user_pass = input("what is your pass for the account")

while True:

    if user_input == user_1.lower():
        print(ask_user_pass)

    if user_input == user_2.lower():
        print(ask_user_pass)

    if user_input == user_3.lower():
        print(ask_user_pass)

    if user_input == user_4.lower():
        print(ask_user_pass)

    else:
        print("unidentified")
        break

    if ask_user_pass == user1_pass:
        print("Welcome to your account user1")
        break
    if ask_user_pass == user2_pass:
        print("Welcome to your account user2")
        break
    if ask_user_pass == user3_pass:
        print("Welcome to your account user3")
        break
    if ask_user_pass == user4_pass:
        print("welcome to your account user4")
        break
    else:
        print("wrong pass try again")
        continue
