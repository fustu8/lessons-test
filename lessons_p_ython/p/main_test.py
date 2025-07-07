# # password = "1234"
# # attempts = 5

# # while True :

# #     if attempts == 0 :
# #         print ("you have used all your attempts")

# #     user_input = input("what is the password: ")
# #     if user_input == password:
# #         print("correct password ")
# #         break

# #     elif  user_input != password:
# #         attempts = attempts - 1
# #         print("incorret password try again",attempts)
# #         continue
# #     elif attempts >= 0 :
# #         print ("done")


# # password = "1234"
# # attempts = 5

# # while True :

# #     if attempts == 0 :
# #         print ("you have used all your attempts")
# #         break

# #     user_input = input(f"what is your password you have {attempts} attempts remeaing: ")

# #     if user_input == password :
# #         print("correct password ")
# #         break

# #     else :
# #         attempts = attempts - 1
# #         print("incorrect password")


# # hello_1= "my name is mohammed"

# # print(hello)


# # value = (5 - 1) * ((7 + 1) / (3 - 1))
# # print(value)

# # value2 = (6 - 1) * ((8 + 2) / (4-1))
# # print (value2)

# # value_3 = 10/3

# # store_the_data = (value_3 + 2)

# # print (store_the_data)

# # print(type(store_the_data))

# # str_string_1 = "12"
# # str_string = int(str_string_1)
# # print(type(str_string))


# # int_integer_1 = 12
# # int_integer = str(int_integer_1)
# # print(int_integer + "2")
# # print(int_integer_1 + 2)

# # float_Floating_point_number = 1.2
# # float_2 = int(float_Floating_point_number)
# # print(type(float_2))
# # print(float_2)


# # who is avilable for today

# # john = "not available"
# # sara = "not available"
# # ahmad = "available"

# # while True:

# #     name1 = "john"
# #     name2 = "sara"
# #     name3 = "ahmad"
# #     print("\npeople in the group :")
# #     print(name1)
# #     print(name2)
# #     print(name3)

# #     user_input = input("\nwho is available for today ")

# #     if user_input.lower() == name2 :
# #         print(f"sara is {sara} for today")
# #         continue

# #     if user_input.lower() == name3:
# #         print(f"ahmad is {ahmad} today")
# #         break

# #     if user_input.lower() == name1 :
# #         print(f"John is {john} today")
# #         continue

# #     else:
# #         print("there is no one with this name in the group")
# #         continue


# # --- Data Setup ---
# # Instead of separate variables, we use one dictionary to hold all our data.
# # The name is the "key" and their status is the "value".
# # This is much easier to read and update. If we want to add a new person,
# # we just add a new line here.
# people_availability = {
#     "john": "not available",
#     "sara": "not available",
#     "ahmad": "available",
# }

# # --- Main Program Loop ---
# while True:
#     # --- Printing the Names ---
#     # Instead of printing each name manually, we can use a loop.
#     # The .keys() method gives us a list of all the names in our dictionary.
#     print("\nPeople in the group:")
#     for name in people_availability.keys():
#         print(f"- {name.title()}")  # .title() capitalizes the name nicely

#     # --- Getting User Input ---
#     user_input = input(
#         "\nWhose availability do you want to check? (Type 'exit' to quit) "
#     )

#     # Add a way to exit the loop
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break

#     # --- Checking Availability (The Smart Way) ---
#     # We check if the name the user typed exists as a key in our dictionary.
#     # We use .lower() to make it case-insensitive.
#     if user_input.lower() in people_availability:
#         # If the name is in the dictionary, we can get their status directly.
#         name_key = user_input.lower()
#         status = people_availability[name_key]
#         print(f"--> {name_key.title()} is {status} today.")

#         # This checks if the person is the one available to end the program
#         if status == "available":
#             print("--> Found someone available! Program will now exit.")
#             break
#     else:
        
#         print("--> There is no one with this name in the group.")







text = 'Hello World'
# r = text[10]
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])
# print(text[6])       
# print(text[7])
# print(text[8])
# print(text[-9])
# print(len(text))          
# index = text.find(text[0])
# print(index)
# print(text.lower())
# print(text.title())
# print(text.upper())







        















