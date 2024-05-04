# CUSTOMER *************************************************************************************************************
def menu():
    print("{:^30}{:^100}".format("Service type", "Service fee"))
    print("{:>67}{:>35}".format("Normal", "Urgent"))
    print("{:<15}{:^62}{:^8}".format("1.Remove virus, malware or spyware", "RM50.00", "RM80.00"))
    print("{:<15}{:^42}{:^28}".format("2.Troubleshoot and fix computer running slow", "RM60.00", "RM90.00"))
    print("{:<15}{:>42}{:>35}".format("3.Laptop screen replacement", "RM380.00", "RM430.00"))
    print("{:<15}{:>41}{:>35}".format("4.Laptop battery replacement", "RM180.00", "RM210.00"))
    print("{:<15}{:>27}{:>35}".format("5.Operating System Format and Installation", "RM100.00", "RM150.00"))
    print("{:<15}{:>42}{:>36}".format("6.Data backup and recovery", "RM80.00", "RM130.00"))

def description(username, password):
    with open("description.txt", "r") as f2:
        for line in f2:
            input_username, input_password, service_type, service_fee, service_fee_amount, date_collection = line.strip().split(",")
            if input_username == username and input_password == password:
                print(f"Username:{username}\nService type:{service_type}\nService fee:{service_fee}\nService fee amount:{service_fee_amount}\nDate collection:{date_collection}\n")
                break
        else:
            print("Your description are still pending...")


def update_customer_data(username, password, new_username, new_password, new_gender, new_city, new_postcode, new_telephone):
    with open("customers_information.txt", "r") as f:
        lines = f.readlines()

    user_updated = False

    for i, line in enumerate(lines):
        current_username, current_password, service_type, service_fee, service_fee_amount, gender, city, postcode, telephone, day, month, year, paid_amount = line.strip().split(",")

        if current_username == username and current_password == password:
            lines[i] = f"{new_username},{new_password},{service_type},{service_fee},{service_fee_amount},{new_gender},{new_city},{new_postcode},{new_telephone},{day},{month},{year},{paid_amount}\n"
            user_updated = True
            break

    with open("customers_information.txt", "w") as f:
        f.writelines(lines)

    return user_updated

def update_customer_details():
    print("Enter your current username and password")
    input_username = input("Username: ")
    input_password = input("Password: ")
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")

    while True:
        new_gender = input("male/female: ").lower()
        if new_gender in ("male", "female"):
            break
        else:
            print("Invalid choice. Please enter 'male' or 'female'.")

    new_city = input("Enter new city:")

    while True:
        new_postcode = input("Enter new postcode:")
        if new_postcode.isdigit():
            break
        else:
            print("Invalid input. Please enter digits.")

    while True:
        new_telephone = input("Enter new contact number:")
        if new_telephone.isdigit() and len(new_telephone) == 10:
            break
        else:
            print("Invalid input. Please enter a 10-digit number.")

    user_updated = update_customer_data(input_username, input_password, new_username, new_password, new_gender, new_city, new_postcode, new_telephone)

    if user_updated:
        print("Profile updated successfully.")
    else:
        print("User not found. Profile not updated.")

def change_services(username):
    menu()
    services = {
        '1': ("Remove virus malware or spyware", {"normal": 50.00, "urgent": 80.00}),
        '2': ("Troubleshoot and fix computer running slow", {"normal": 60.00, "urgent": 90.00}),
        '3': ("Laptop screen replacement", {"normal": 380.00, "urgent": 430.00}),
        '4': ("Laptop battery replacement", {"normal": 180.00, "urgent": 210.00}),
        '5': ("Operating System Format and Installation", {"normal": 100.00, "urgent": 150.00}),
        '6': ("Data backup and recovery", {"normal": 80.00, "urgent": 130.00}),
    }

    while True:
        service_choice = input("Enter the service number (1-6): ")
        service_fee_type = input("Enter service fee type (normal/urgent): ") .lower()

        if service_choice in services and service_fee_type in ('normal', 'urgent'):
            new_service_fee = services[service_choice][1][service_fee_type]
            new_service_fee_amount = float("{:.2f}".format(new_service_fee))

            while True:
                day = (input("Day register change:"))
                if day.isdigit() and "1" <= day <= "31":
                    break
                else:
                    print("Invalid input. Please enter 1-30/31")
            while True:
                month = input("Month register change: ").lower()
                valid_months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
                if month.lower() in valid_months:
                    break
                else:
                    print("Invalid input. Please enter a valid month (e.g., january).")
            while True:
                year = input("Year register change:")
                if year.isdigit() and len(year) == 4:
                    break
                else:
                    print("Invalid input.")
            paid_amount = 0
            while paid_amount < new_service_fee_amount:
                paid_amount = float(input("Enter your payment amount: RM"))
                if paid_amount >= new_service_fee_amount:
                    break
                else:
                    print("Invalid choice. Please enter an amount equal to or greater than RM{:.2f}".format(new_service_fee_amount))
            print("Payment accepted. Thank you!")
            with open("customers_information.txt", "r") as f:
                lines = f.readlines()

            with open("customers_information.txt", "w") as f:
                for line in lines:
                    user_data = line.strip().split(",")
                    if user_data[0] == username:
                        line = f"{username},{user_data[1]},{services[service_choice][0]},{service_fee_type},{new_service_fee_amount},{user_data[5]},{user_data[6]},{user_data[7]},{user_data[8]},{day},{month},{year},{paid_amount}\n"
                    f.write(line)

            print(f"Service for '{username}' changed successfully to '{services[service_choice][0]}' ({service_fee_type}): RM{new_service_fee_amount}")
            break
        else:
            print("Invalid service choice or service fee type. Please try again.")


def signin_customer():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    menu()
    while True:
        service_choice = input("Enter the service number (1-6): ")
        if service_choice in ('1', '2', '3', '4', '5', '6'):
            break
        else:
            print("Invalid service choice. Please try again.")
    while True:
        service_fee = input("Enter service fee type (normal/urgent): ").lower()
        if service_fee in ('normal', 'urgent'):
            break
        else:
            print("Invalid service fee type. Please try again.")
    services = {
        '1': ("Remove virus malware or spyware", {"normal": 50.00, "urgent": 80.00}),
        '2': ("Troubleshoot and fix computer running slow", {"normal": 60.00, "urgent": 90.00}),
        '3': ("Laptop screen replacement", {"normal": 380.00, "urgent": 430.00}),
        '4': ("Laptop battery replacement", {"normal": 180.00, "urgent": 210.00}),
        '5': ("Operating System Format and Installation", {"normal": 100.00, "urgent": 150.00}),
        '6': ("Data backup and recovery", {"normal": 80.00, "urgent": 130.00}),
    }
    service_type = services[service_choice][0]
    service_fee_amount = services[service_choice][1][service_fee]
    while True:
        gender = input("male/female:").lower()
        if gender in ("male", "female"):
            break
        else:
            print("Invalid choice. Please try again.")

    city = input("Current city:")

    while True:
        postcode = (input("Current postcode:"))
        if postcode.isdigit():
            break
        else:
            print("Invalid input. Please enter digits.")
    while True:
        telephone = input("Contact number:")
        if telephone.isdigit() and len(telephone) == 10:
            break
        else:
            print("Invalid input. Please enter a 10-digit number.")
    while True:
        day = (input("Day register:"))
        if day.isdigit() and "1" <= day <= "31":
            break
        else:
            print("Invalid input. Please enter 1-30/31")
    while True:
        month = input("Month register: ").lower()
        valid_months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november","december")
        if month in valid_months:
            break
        else:
            print("Invalid input. Please enter a valid month (e.g., january).")
    while True:
        year = input("Year register:")
        if year.isdigit() and len(year) == 4:
            break
        else:
            print("Invalid input.")
    paid_amount = 0
    while paid_amount < service_fee_amount:
        paid_amount = float(input("Enter your payment amount: RM"))
        if paid_amount >= service_fee_amount:
            break
        else:
            print("Invalid choice. Please enter an amount equal to or greater than RM{:.2f}".format(service_fee_amount))
    print("Payment accepted. Thank you!")
    f = open("customers_information.txt", "a")
    f.write(
        f"{username},{password},{service_type},{service_fee},{service_fee_amount},{gender},{city},{postcode},{telephone},{day},{month},{year},{paid_amount}\n")
    f.close()
    print("Record added. Thank you!")


def login_customer():
    attempts = 0
    while attempts < 3:
        print("Log in")
        input_username = input("Username: ")
        input_password = input("Password: ")
        found = False
        with open("customers_information.txt", "r") as f:
            for line in f:
                username, password, service_type, service_fee, service_fee_amount, gender, city, postcode, telephone_number, day, month, year, paid_amount = line.strip().split(",")
                if input_username == username and input_password == password:
                    found = True
                    print("You have successfully logged in")
                    print(f"Your current requested services: {service_type}, {service_fee}, RM{service_fee_amount}")
                    while True:
                        print("1) Edit Service\n2) Edit Profile\n3) View Description")
                        choose2 = input("Choose your page (1/2/3):")
                        if choose2 == "1":
                            change_services(input_username)
                        elif choose2 == "2":
                            update_customer_details()
                        elif choose2 == "3":
                            description(input_username, input_password)
                        else:
                            print("Invalid answer")
                            continue
                        while True:
                            continue_choice = input("Do you want to continue? (yes/no): ").lower()
                            if continue_choice in ["yes", "no"]:
                                break
                            else:
                                print("Invalid choice. Please enter 'yes' or 'no'.")
                        if continue_choice == "no":
                            break
                    break
        if found:
            break
        else:
            print("Incorrect username or password, please try again")
            attempts += 1
    if attempts == 3:
        print("Maximum login attempts reached. Exiting.")
    else:
        print("Thanks for using our application")

def mainpage():

    print("Main Page")
    choose = "1" and "2"
    print("1) Login\n2) Sign in")
    while choose != "1" and "2":
        choose = input("Login / Sign in (Enter Number):")
        if choose == "1":
            login_customer()
        elif choose == "2":
                signin_customer()
                log = "yes" and "no"
                while log != "yes" and "no":
                    log = input("Do you want to login?(yes/no):") .lower()
                    if log == "yes":
                        login_customer()
                    elif log == "no":
                        print("Thanks for the registration.")
                        break
                    else:
                        print("Invalid answer")
                break
        else:
            print("Invalid number!!")

#ADMIN *****************************************************************************************************************
def StaffLogin():
    count = 0
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    count += 1
    with open("workers_information.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            stored_username = data[1]
            stored_password = data[2]
            if stored_username == Username and stored_password == Password:
                print("Login Success")
                return Username
        print("Login Failed")

def ChangePassword(Username):
    NewPass = input("Enter the new password that you want to set: ")
    with open("workers_information.txt", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        data = lines[i].strip().split(',')
        stored_username = data[1]

        if stored_username == Username:
            data[2] = NewPass
            lines[i] = ','.join(data) + '\n'

            with open("workers_information.txt", "w") as file:
                file.writelines(lines)

            print("Password updated successfully.")
            return

    print("Username not found. Password not updated.")

def TotalSalesByMonth():
    month = input("Enter the month (e.g., February) to calculate total income for: ")
    total = 0
    with open("customers_information.txt", "r") as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 13:
                service_month = values[10].strip()
                if service_month.lower() == month.lower():
                    income = float(values[4])
                    total += income
    return total

def MonthlyReport():
    month = input("Month (e.g., February): ")
    service_data = {}
    summary = {}

    with open("customers_information.txt", "r") as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 12:
                service_type = values[2].strip()
                service_month = values[10].strip()

                if service_month.lower() == month.lower():
                    name = values[0]
                    day = values[9]
                    year = values[11]

                    entry = f"Name: {name}   Date: {day} {service_month} {year}"

                    if service_type in service_data:
                        service_data[service_type].append(entry)
                    else:
                        service_data[service_type] = [entry]

                    if service_type in summary:
                        summary[service_type] += 1
                    else:
                        summary[service_type] = 1

    for service, data in service_data.items():
        if data:
            print(f"Service: {service}")
            for entry in data:
                print(entry)
            print()

    print("------------------Summary--------------------")
    for service, count in summary.items():
        print(f"{service} = {count}")

def admin():
    while True:
        print('''           Choose your services
---------------------------------------------
1. New worker register
2. View service report / total income
3. Update password
4. Logout''')

        choice = int(input("Enter your choice :"))
        if choice == 1:
            print('''1. New technician register
2. New receptionist register''')
            sec_choice = int(input("Enter the position that you want to register :"))
            while sec_choice == 1:
                account = "Technician"
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                gender = input("Enter Gender:")
                city = input("Enter City:")
                postcode = input("Enter Postcode:")
                phone_number = input("Enter Phone Number: ")

                data = f"{account},{username},{password},{gender},{city},{postcode},{phone_number}"
                with open("workers_information.txt", "a") as f:
                    f.write(data + "\n")
                    print("Register Successfully")
                    break

            while sec_choice == 2:
                account = "Receptionist"
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                gender = input("Enter Gender:")
                city = input("Enter City:")
                postcode = input("Enter Postcode:")
                phone_number = input("Enter Phone Number: ")

                data = f"{account},{username},{password},{gender},{city},{postcode},{phone_number}"
                with open("workers_information.txt", "a") as f:
                    f.write(data + "\n")
                    print("Register Successfully")
                    break

        while choice == 2:
            sec_choice = int(input("1. Service report(monthly)\n2. Total Income (monthly)\nEnter your choice: "))
            if sec_choice == 1:
                MonthlyReport()
                break

            if sec_choice == 2:
                total_income = TotalSalesByMonth()
                print(f"Total income for the specified month: RM{total_income}")
                break

        while choice == 3:
            Username = StaffLogin()
            ChangePassword(Username)
            break
        if choice == 4:
            print("Log out")
            break

#TECHNICIAN ************************************************************************************************************
def update_workers_data(username, password, new_username, new_password, new_gender, new_city, new_postcode, new_telephone):
    with open("workers_information.txt", "r") as f:
        lines = f.readlines()

    user_updated = False

    for i, line in enumerate(lines):
        account, current_username, current_password, gender, city, postcode, telephone = line.strip().split(",")

        if current_username == username and current_password == password:
            lines[i] = f"{account},{new_username},{new_password},{new_gender},{new_city},{new_postcode},{new_telephone}\n"
            user_updated = True
            break

    with open("workers_information.txt", "w") as f:
        f.writelines(lines)

    return user_updated

def update_workers_details():
    print("Enter your current username and password")
    input_username = input("Username: ")
    input_password = input("Password: ")
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")

    while True:
        new_gender = input("male/female: ").lower()
        if new_gender in ("male", "female"):
            break
        else:
            print("Invalid choice. Please enter 'male' or 'female'.")

    new_city = input("Enter new city:")

    while True:
        new_postcode = input("Enter new postcode:")
        if new_postcode.isdigit():
            break
        else:
            print("Invalid input. Please enter digits.")

    while True:
        new_telephone = input("Enter new contact number:")
        if new_telephone.isdigit() and len(new_telephone) == 10:
            break
        else:
            print("Invalid input. Please enter a 10-digit number.")

    user_updated = update_workers_data(input_username, input_password, new_username, new_password, new_gender, new_city, new_postcode, new_telephone)

    if user_updated:
        print("Profile updated successfully.")
    else:
        print("User not found. Profile not updated.")

#view customer details
def read_customer_details():
    with open("customers_information.txt", "r") as f1:
        for line_number, line in enumerate(f1, start=1):
            username, password, service_type, service_fee, service_fee_amount, gender, city, postcode, telephone, day, month, year, paid_amount = line.strip().split(",")
            print(f"Line {line_number}:")
            print(f"Username: {username}\nService type: {service_type}\nService fee: {service_fee}\nService fee amount:RM{service_fee_amount}\nRegister date:{day}{month}{year}\n")
# add date collection in description.txt
def add_description(username, collection_date):
    with open("customers_information.txt", "r") as f1:
        found = False
        for line in f1:
            current_username, password, service_type, service_fee, service_fee_amount, gender, city, postcode, telephone, day, month, year, paid_amount = line.strip().split(",")
            if current_username == username:
                found = True
                with open("description.txt", "a") as f2:
                    f2.write(f"{username},{password},{service_type},{service_fee},{service_fee_amount},{collection_date}\n")
                print("Record added. Thank you!")
                break

        if not found:
            print("Username not found in customer information. Record not added.")

def technician(username,password):
    while True:
        print("1) Edit Profile\n2) Add Description\n")
        choose2 = input("Choose your page (1/2):")
        if choose2 == "1":
            update_workers_details()
        elif choose2 == "2":
            read_customer_details()
            input_username = input("Enter the username: ")
            input_collection_date = input("Enter the collection date: ")
            add_description(input_username, input_collection_date)
        else:
            print("Invalid answer")
            continue
        while True:
            continue_choice = input("Do you want to continue? (yes/no): ").lower()
            if continue_choice in ["yes", "no"]:
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        if continue_choice == "no":
            break

#RECEPTIONIST **********************************************************************************************************
def receptionist(username, account, password):
    while True:
        profile_update = False
        print("""           Menu
+++++++++++++++++++++++++++++++++++++++++
1. Register Customer and Assign Service
2. Accept Payment and Generate Receipt
3. Update Profile
4. Exit
+++++++++++++++++++++++++++++++++++++++++""")
        selection = input("Selection:")
        if selection == "4":
            exit("Logout Success")
        while selection == "1":
            print("Fill in Customer information, or type q to end")
            cusername = input("Register username:")
            if cusername == "q":
                print("Return to the main page\n")
                break
            cpassword = input("Register password:")
            menu()
            while True:
                service_choice = input("Register service (1-6)         :")
                if service_choice.isdigit():
                    if service_choice in ("1","2","3","4","5","6"):
                        break
                    else:
                        print("Enter service number in 1-6")
                        continue
                else:
                    print("Enter service number in digits")
                    continue

            while True:
                service_fee = input("Urgent/Normal                  :")
                service_fee = service_fee.capitalize()
                if service_fee != "Urgent" and service_fee != "Normal":
                    print("Please select Urgent or Normal Only")
                    continue
                else:
                    break
            services = {
    '1': ("Remove virus malware or spyware", {"Normal": 50.00, "Urgent": 80.00}),
    '2': ("Troubleshoot and fix computer running slow", {"Normal": 60.00, "Urgent": 90.00}),
    '3': ("Laptop screen replacement", {"Normal": 380.00, "Urgent": 430.00}),
    '4': ("Laptop battery replacement", {"Normal": 180.00, "Urgent": 210.00}),
    '5': ("Operating System Format and Installation", {"Normal": 100.00, "Urgent": 150.00}),
    '6': ("Data backup and recovery", {"Normal": 80.00, "Urgent": 130.00}),
}
            service_type = services[service_choice][0]
            service_fee_amount = services[service_choice][1][service_fee]
            while True:
                gender = input("Gender                         :").capitalize()
                if gender != "Female" and gender != "Male":
                    print("Please enter female or male")
                    continue
                else:
                    break
            city = input("City                           :").capitalize()
            postcode = input("Postcode                       :")
            while True:
                telephone = input("Telephone                      :")
                if telephone.isdigit() and len(telephone) == 10:
                    break
                else:
                    print("Please enter telefon number in 10-digits")
                    continue

            while True:
                day = input("Day                            :")
                month = input("Month  (e.g.:January)          :").lower()
                year = input("Year                           :")
                if month not in ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"):
                    print("Please type month in full name ^_^")
                    continue
                else:
                    break
            while True:
                paid_amount = input("Amount paided by customer      :")
                if float(paid_amount) < float(service_fee_amount):
                    print(f"Money insufficient, the fee is RM{float(service_fee_amount)}")
                    continue
                else:
                    break
            file1 = open("customers_information.txt", 'a+')
            file1.write(f"{cusername},{cpassword},{service_type},{service_fee},{service_fee_amount},{gender},{city},{postcode},{telephone},{day},{month},{year},{paid_amount}\n")
            file1.close()
            continue

        while selection == "3":
            choice = input("1. Update Profile\n2. View Profile\n3. Quit\nChoice:")
            if choice == "3":
                break
            elif choice == "1":
                print("Add Information, or type q to quit")
                while True:
                    new_username = input("New Username:")
                    if new_username == "q":
                        break
                    new_password = input("New Password:")
                    while True:
                        gender = input("Gender:").lower()
                        if gender not in ("female","male"):
                            print("Please enter female or male only")
                            continue
                        else:
                            break
                    city = input("City:")
                    postcode = input("Postcode:")
                    while True:
                        telephone = input("Telephone:")
                        if telephone.isdigit and len(telephone) == 10:
                            break
                        else:
                            print("Please enter telephone number in 10-digits")
                            continue
                    file2 = open("workers_information.txt", "r")
                    file2 = file2.readlines()
                    newfile = account + "," + new_username + "," + new_password + "," + gender + "," + city + "," + postcode + "," + telephone
                    for a,text in enumerate(file2):
                        index = text.split(",")

                        if account == index[0] and username == index[1] and password == index[2]:
                            file2[a] = newfile + "\n"
                            profile_update = True
                            break
                    with open("workers_information.txt", "w") as file3:
                        file3.writelines(file2)
                        print("Update Profile Successfully.")
                        file3.close()
                        break

            elif choice == "2":
                with open("workers_information.txt", "r") as file:
                    if profile_update:
                        username = new_username
                        password = new_password
                    for line in file:
                        index1 = line.strip().split(",")
                        if username in index1:
                            if len(index1) >= 7:
                                print(f"Role: {account}\nUsername: {username}\nPassword: {password}\nGender: {index1[3]}\nCity: {index1[4]}\nPostcode: {index1[5]}\nTelephone: {index1[6]}")
                            break
                continue
            else:
                print("! ! ! Out of Range ! ! !")
                continue
        while selection == "2":
            print("Customer List")
            print("+++++++++++++++++++++++++++++++++++++++++")
            with open("customers_information.txt", 'r') as file1:
                num = 1
                for line in file1.readlines():
                    line = line.split(",")
                    print(f"{num}.{line[0].capitalize()}")
                    num += 1
                c = num
                print(f"{c}.Back To Menu")
                action = int(input("Choose number:"))
                if action == c:
                    break

            with open("customers_information.txt", 'r') as file2:
                lines = file2.readlines()
                if 1 <= action <= len(lines):
                    action -= 1
                    desired_line = lines[action]
                    desired_line = desired_line.rstrip().split(',')
                    balance = float(desired_line[12])- float(desired_line[4])
                    print("{:>35}".format("|Receipt|"))
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
                    print("{:<30}{:<43}{:>}".format(f"|Payment Date", "|Payment Method", "|"))
                    print("{:<30}{:<43}{:>}".format(f"|{desired_line[9]}-{desired_line[10]}-{desired_line[11]}","|Cash", "|"))
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
                    print("{:<30}{:<43}{:>}".format(f"|From:","|Sold to:", "|"))
                    print("{:<30}{:<43}{:>}".format(f"|{desired_line[0].capitalize()}","|Laptop Service Store", "|"))
                    print("{:<30}{:<43}{:>}".format(f"|{desired_line[6]}","|KL", "|"))
                    print("{:<30}{:<43}{:>}".format(f"|{desired_line[7]}","|43300", "|"))
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
                    print("{:<30}{:<43}{:>}".format("|Service Type", f":{desired_line[2]}", "|"))
                    print("{:<30}{:<43}{:>}".format("|Service Speed", f":{desired_line[3]}", "|"))
                    print("{:<30}{:<43}{:>}".format("|Paid Amount", f":RM{float(desired_line[12])}", "|"))
                    print("{:<30}{:<43}{:>}".format("|Service Fee", f":RM{desired_line[4]}", "|"))
                    print("{:<30}{:<43}{:>}".format("|Balance", f":RM{balance}", "|"))
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

                else:
                    print("Invalid number")
                    continue
def login():
    count = 0
    while count < 3:
        account = input("Please enter your roles (Receptionist, Admin, Technician):").capitalize()
        username = input("Please enter your username:")
        password = input("Please enter your password:")
        for stafflog in open("workers_information.txt", "r").readlines():
            staffindex = stafflog.strip().split(",")
            if account == staffindex[0] and username == staffindex[1] and password == staffindex[2]:
                if account == "Receptionist":
                    receptionist(username, account, password)
                    return True

                elif account == "Admin":
                    print("Login Success")
                    admin()
                    return True

                elif account == "Technician":
                    print("Login Success")
                    technician(username,password)
                    return True

        count += 1
        chance = 3 - count
        if chance > 0:
            print(f"Invalid Synxtax {chance} Entry Remaining")
            continue
        else:
            print("Please check your role, username and password")
            exit("Reach Maximum attempt, Exiting...")

while True:

    print("- - - - Laptop Service Provider - - - -")
    type = input("Are you a Customer or Staff?\nAnswer:").lower()
    if type == "customer":
        mainpage()
        break
    elif type != "staff" and type != "customer":
        continue
    elif type == "staff":
        login()
        break