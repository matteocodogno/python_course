# types & variables
print("#### Types ####")
x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(z))
print()

# list
print("#### List ####")
monday_temperatures = [9.1, 8.8, 7.5]
print(f"list {monday_temperatures}")
monday_temperatures.append(3.3)
print(f"append {monday_temperatures}")
print(f"index {monday_temperatures.index(8.8)}")
print(f"slice[1:3] {monday_temperatures[1:3]}")
print(f"slice[:3] {monday_temperatures[:3]}")
print(f"slice[2:] {monday_temperatures[2:]}")
print(f"slice[-1] {monday_temperatures[-1]}")
monday_temperatures.clear()
print(f"clear {monday_temperatures}")
print()

# string slice
print("#### String Slice ####")
mystring = 'hello'
print(f"slice[-1]{mystring[-1]}")
print()

# Dictionary (Map)
print("#### Dictionary ####")
student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}
avg = sum(student_grades.values()) / len(student_grades)
print(f'avg {avg}')
print(f"access {student_grades['Sim']}")
data = [["name", "John"], ["surname", "smith"]]
print(f"from list to dict {dict(data)}")
print()

# tuple - are immutable
print("#### Tuple ####")
tuple = (1, 4, 5)
print()

# function
print("#### Functions ####")


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


print(f"mean function {mean([1, 2, 4, 7])}")
print(f"mean function dict {mean(student_grades)}")
print()

# User input
print("#### User Input ####")


def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))

name = "matteo"
# name = input("Enter your name: ")
surname = "Codogno"
# surname = input("Enter your surname ")
# works with python 2 and python 3
message1 = "Hello %s %s!" % (name, surname)
print(message1)
message2 = f"Hello {name} {surname}"
print(message2)
print()

# for loop
print("#### for loop ####")
monday_temperatures = [9.1, 8.8, 7.6]
for temperature in monday_temperatures:
    print(f"for loop {round(temperature)}")

for letter in 'hello':
    print(letter.title())

for name, grade in student_grades.items():
    print(f"Name: {name} - {grade}")
print()

# while loops
print("#### while loops ####")
username = ''
while username != 'pypy':
    username = input("Enter username: ")

# More readable?
while True:
    password = input("Enter password: ")
    if password == 'pypy':
        break
    else:
        continue

