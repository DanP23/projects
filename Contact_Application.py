Contact_list = {}

# Function to create new contact 
def new_contact():
    phone_number = int(input("Phone #: "))
    adress = input("Adress: ")
    name = input("Name: ")
    details = [] # using list to store more then one value in dictioinary
    details.append(phone_number)
    details.append(adress)
    Contact_list[name] = details # assigning details list as contact_list dict value
    answr = input("do you have another contact? (y/n): ")
    if answr.lower() == 'y':
        new_contact()
    elif answr.lower() == "n":
        print(Contact_list)
        opening_menu()
    else:
        opening_menu()

# Function to delete contact
def delete_contact():
    selected_contact = input("Who do you want removed: ")
    if selected_contact in Contact_list.keys():
        del Contact_list[selected_contact]
        print(Contact_list)
        answr2 = input("would you like to delete a contact(1), create a new contact(2) or end session(3)")
        if answr2 == "1":
            delete_contact()
        elif answr2 == "2":
            new_contact()
        elif answr2 == "3":
            opening_menu()

        
# "main menu" created to keep program alive throughout navigation
def opening_menu():
    menu_answr = input("Welcome to your contact list. would you like to Add a contact(1) or would you like to remove a contact(2) or end session(3): ")
    if menu_answr == "1":
        new_contact()
    elif menu_answr == "2":
        delete_contact()
        print(Contact_list)

# initializing program through calling main menu function
opening_menu()
