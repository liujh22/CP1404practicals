
password = input("Enter your password: ")

while len(password) < 10:
    print("Too Short")
    password = input("Enter your password: ")

password_length = len(password)

for i in range(password_length):
    print("*", end="")

