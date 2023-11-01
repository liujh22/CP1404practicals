# 1
file_out = open("name.txt", "w")
name = input("Enter your name: ")
file_out.write(name)
file_out.close()

# 2
file_in = open("name.txt", "r")
reading = file_in.read().strip()
file_in.close()
print(f"Your name is {reading}")

# 3
file_in = open("numbers.txt", "r")
number1 = int(file_in.readline())
number2 = int(file_in.readline())
file_in.close()
print(number1+number2)

# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
