#=====importing libraries===========
# Import datetime module to retrieve current date
from datetime import date
# datetime object containing current date and time
today = date.today()
# dd/mm/YY format
current_date = today.strftime("%d-%m-%Y")

#====Login Section====
# Open file and assign to an empty dictionary
usernames = open('user.txt', 'r+')
username_dict = {}

# Assign to variable 'username' and 'password' with keys, values from username_dict
for username in usernames:
    key, value = username.split(", ")
    username_dict[key] = value.strip("\n")

# Use a while loop to validate username login and password
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Retrieve user value from dictionary using get method
    correct_pass = username_dict.get(username)
    # If statement condition to check if password entered is the same as dictionary value
    if correct_pass == password:
        print(f"You are logged in as {username}.\n")
        break
    print("Incorrect login details.")

# Separating menus for both admin and other users using an if statement condition
while True:
    # Compulsory task 2: Only the user with the username ‘admin’ is allowed to register
    # users and display statistics. Separate different menus.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
d - display statistics
e - Exit
: ''').lower()
    else:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    # Bar all users except "admin" to registering users and displaying statistics
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    # Compulsory task 2: add admin user privilege.
    if menu == 'r':
        if username != "admin":
            print("You do not have user privilege.\n")
            continue
        password_confirm = ""
        # Prompt admin user to enter new user details
        while True:
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            password_confirm = input("Confirm new password: ")
            # Check if password entered is the same using an if statement condition
            if password_confirm == new_password:
                print("User has been registered. \n")
                usernames.write("\n" + new_username + ", " + new_password)
                break
            else:
                print("Passwords do not match. Please try again.")
                continue

    elif menu == 'a':
        # Open tasks.txt to write new tasks. Prompt user for new details
        with open('tasks.txt', 'a+') as add_to_file:
            assignee = input("Enter the username which the task is assigned to: ")
            task_title = input("Enter title of the task: ")
            task_description = input("Enter description of the task: ")
            due_date = input("Enter due date: ")
            task_completion = "No"
            current_date = current_date

            # Assign new details to a variable 'new_details'
            new_details = f"\n{assignee}, {task_title}, {task_description}, {current_date}, {due_date}, {task_completion}"
            # Write to file
            add_to_file.write(new_details)

    elif menu == 'va':
        pass
        # Read from tasks.txt file and assign to
        tasks_write = open('tasks.txt', 'r')
        data = tasks_write.readlines()

        for pos, line in enumerate(data, 1):
            split_data = line.split(", ")

            output = f"————————————————————————{pos}—————————————————————————————\n"
            output += f"Task:\t\t\t\t{split_data[1]}\n"
            output += f"Assigned to: \t\t{split_data[0]}\n"
            output += f"Date assigned: \t\t{split_data[3]}\n"
            output += f"Due Date:\t\t\t{split_data[4]}\n"
            output += f"Task Description: \t{split_data[2]}\n"
            output += "——————————————————————————————————————————————————————\n"
            print(output)

    elif menu == 'vm':
        # Open task.txt to read from.
        with open('tasks.txt', 'r') as task_write:
            for options in task_write:
                split_data = options.split(", ")
                # Split data to format data.

                if split_data[0] == username:
                    output = f"Task:\t\t\t\t{split_data[1]}\n"
                    output += f"Assigned to: \t\t{split_data[0]}\n"
                    output += f"Date assigned: \t\t{split_data[3]}\n"
                    output += f"Due Date:\t\t\t{split_data[4]}\n"
                    output += f"Task Description: \t{split_data[2]}\n"
                    # output += "——————————————————————————————————————————————————————\n"
                    print(output)

    elif menu == 'd':
        # Bar users except admin for this option
        if username != "admin":
            print("You do not have user privilege.\n")
            continue

        # Declare empty variable for iteration
        total_tasks = 0
        total_users = 0

        # 'With' statement avoids the need for closing file
        with open("tasks.txt", "r") as tasks:
            # For loop to iterate through each line in tasks.txt file
            for task in tasks:
                total_tasks += 1
        print(f"\nTotal number of tasks: {total_tasks}")

        with open("user.txt", "r") as usernames:
            for username in usernames:
                total_users += 1
        print(f"Total number of users: {total_users}\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

    usernames.close()