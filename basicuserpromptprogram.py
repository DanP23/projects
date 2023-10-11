class User():
    def __init__(self, userid: 0, username, email):
        self.userid = userid
        self.username = username
        self.email = email
users = []
while True:
    print("User List Menu:")
    print("1. Add User")
    print("2. Delete User")
    print("3. List Users")
    print("4. Search User")
    print("5. Quit")

    menu_selection = int(input("Enter Your Choice: "))

    if menu_selection == 1:
        username = input("Enter your username: ")
        email = input("email: ")
        users.append(User(len(users) + 1, username, email))
        


        
    elif menu_selection == 2:
        userid = int(input("user ID to delete: "))
        for user in users:
            if user.userid == userid:
                users.remove(user)
                print(f"user with Id: {userid} deleted\n")
            else:
                print("user not found\n")
    elif menu_selection == 3:
        for user in users:
            for user in users:
                print(f"User ID: {user.userid}, Username: {user.username}, Email: {user.email}")
    
    elif menu_selection == 4:
        username_to_search = input("Enter the username to search: ")
        user_found = False
        for user in users:
            if user.username == username_to_search:
                print(f"User found - User ID: {user.userid}, Email: {user.email}")
                user_found = True
                break
        if not user_found:
            print("User not found.")

    elif menu_selection == 5:
        break


            
                

