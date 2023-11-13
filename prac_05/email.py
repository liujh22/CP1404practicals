"""
Practice_05, get email from user and store in dictionary
return email and their names
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    """Ask for email, generate or request name, store in dictionary"""
    name = email.split("@")[0].title().split(".")
    name = " ".join(name)
    email_to_name[email] = name
    confirm = input(f"Is your name {name}? (Y/n) ")
    if confirm.upper() == "Y" or confirm.upper() == "":
        pass
    else:
        email_to_name[email] = input("Name: ")
    email = input("Email: ")

print()  # Blank line
for email, name in email_to_name.items():
    print(f"{name} ({email})")