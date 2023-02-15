import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Welcome to the password generator")
nr_letters = int(input("Enter the number of letters you would like: "))
nr_numbers = int(input("Enter the number of numbers you would like: "))
password = " "

for char in range(1,nr_letters+1):
    random_char = random.choice(letters)
    password = password + random_char

for char in range(1,nr_numbers + 1):
    random_number = random.choice(numbers)
    password = password + random_number



print(password)