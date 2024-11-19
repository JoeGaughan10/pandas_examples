#----- Truthy / Falsy Examples (Value / No Value) -----------

# music = "classical"
# shopping_list = []
# num = 0
# name = ""
# my_name = "Dave"

# print(bool(music))
# print(bool(shopping_list))
# print(bool(num))
# print(bool(name))
# print(bool(my_name))

#--------------------- Truthy / Falsey Application ----------------------

user_name = input("Please enter your chosen username. ")

if user_name:
    print(f"Welcome to your new account, {user_name}")
else:
    print("You did not enter anything")