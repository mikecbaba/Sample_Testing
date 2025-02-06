## exercise 1-8.2 - "Python print string"
strings = ["", "H", "Hello", "Amazing"]

for s in strings:
    print(f"{s}    :   {len(s)}")
print(f"\n")


## exercise 1-8.4 - "Print the character at specific index"
strings = ["Hello", "Pizza", "", "World"]
indices = [2, 4, 3, 15]

for s, index in zip(strings, indices):
        if not s:
            print(f"     {s} : {index} : Empty string.")
        elif index < 0 or index >= len(s):
            print(f"{s} : {index} : Index out of range")
        else:
            print(f"{s} : {index} : {s[index]}")
print(f"\n")


## exercise 1-8.6 - "Reverse a string"
strings = ["Hello", "Wo", ""]

for s in strings:
        print(f"{s} : {s[::-1]}")
print(f"\n")


## exercise 1-8.8 - "first and last three characters of a string"
strings = ["Blue", "Wonderful", "Amazing"]

for s in strings:
    if len(s) < 6:
        print(f"{s} : ")
    else:
        print(f"{s} : {s[:3]}{s[-3:]}")
print(f"\n")


## exercise 1-8.11 - "remove characters at even indices"
strings = ["Coding", "Pizza", "Python", "A", ""]

for s in strings:
    if len(s) <= 1:
        new_str = str
    else:
        new_str = ""
        for i in range(len(s)):
            if i % 2 != 0:
                new_str += s[i]
    print(f"{s} : {new_str}")     
print(f"\n")


## exercise 1-8.13 - "check if a string only contains numbers"
strings = ["Hello", "4567", "Hello59", ""]

for s in strings:
    if any(char.isdigit() for char in s):
        print(f"{s} : True")
    else:
        print(f"{s} : False")
print(f"\n")


## exercise 1-8.15 - "remove the nth character from a string"
strings = ["Hello", "World", "Dog", ""]
indices = [1, 3, 15, 2]

for s, index in zip(strings, indices):
    if not s:
        print(f'{s} : {index} : {s}')
    else:
        print(f'{s} : {index} : {s[:index] + s[index + 1:]}')
print(f'\n')


## exercise 1-8.17 - "replace a character in a string"
strings = ["Hello", "World", "Python", "Python"]
current = ["l", "W", "P", "p"]
new = ["S", "A", "x", "a"]

for i in range(len(strings)):
    original_string = strings[i]
    current_char = current[i]
    new_char = new[i]
    # Replace the character only if it matches (case-sensitive)
    updated_string = original_string.replace(current_char, new_char)
    print(f"{original_string} : {current_char} : {new_char} : {updated_string}")
print(f'\n')


## exercise 9-16.1 - "change commas by dots in a string"
strings = ["Hello, World", "3,456,344"]

for s in strings:
    new_str = s.replace(",",".")
    print(f'{s} : {new_str}')
print(f'\n')


## exercise 9-16.3 - "check if the string contains all letters in the alphabet"
import string

strings = [
    "abcdefghijklmnopqrstuvwxyz",
    "The quick brown fox jumps over the lazy dog",
    "Hello"
]
alphabet = set(string.ascii_lowercase)

for s in strings:
    s = s.lower().replace(" ", "")
    contains_all = alphabet.issubset(set(s))
    print(f"{s} : {contains_all}")
print(f'\n')


## exercise 9-16.5 - "remove spaces from a string"
strings = [
    "Hello, World!",
    "Have a great day",
    "Python"
]

for s in strings:
    new_str = s.replace(" ", "")
    print(f"{s} : {new_str}")
print(f'\n')


## exercise 9-16.7 - "check if the string starts with the prefix"
strings = ["Hello", "Coding", "Nora"]
prefix = ["He", "Con", "Circum"]

for s, pref in zip(strings, prefix):
    if len(pref) > len(s):
        result = False
    else:
        result = s.startswith(pref)
    print(f"{s} : {pref} : {result}")
print(f'\n')


## exercise 9-16.9 - "check if a string ends with a suffix"
strings = ["Hello", "Coding", "Nora"]
suffix = ["ello", "eng", "rowing"]

for s, suf in zip(strings, suffix):
    if len(suf) > len(s):
        result = False
    else:
        result = s.endswith(suf)
    print(f"{s} : {suf} : {result}")
print(f'\n')


## exercise 9-16.12 - "reverse words in string"
strings = ["Hello World", "Python is Awesome"]

for s in strings:
    words = s.split()  # Split the string into words
    result = []
    for word in words:
        reversed_word = word[::-1].swapcase()
        result.append(reversed_word)
    
    new_string = ' '.join(result)
    print(f"{s} : {new_string}")
print(f'\n')


## exercise 9-16.14 - "count repeated characters"
strings = ["Hello", "Corporation", "Python"]

for s in strings:
    repeated_count = 0
    repeated_chars = []
    
    for char in s:
        if s.count(char) > 1 and char not in repeated_chars:
            repeated_count += 1
            repeated_chars.append(char)
    print(repeated_count)
    if len(repeated_chars) > 0:
        for char in sorted(repeated_chars):
            print(char, end=" ")
        print()  # Print a newline after the characters
    else:
        print("None")
print(f'\n')


## exercise 9-16.16 - "sort worlds in alphabetical order"
strings = ["Hello World", "Wonderful World"]

for s in strings:
    words = s.split()  # Split the string into words
    result = []
    for word in words:
        new_word = ''.join(sorted(word.lower()))
        result.append(new_word)
    new_string = ' '.join(result)
    print(f"{s} : {new_string}")
print(f'\n')


## exercise 17-24.2  - "multiply all elements in the list"
lists = [[3, 4, 5, 6], ["a", "b", "c"]]
factor = [2, 3]
result = []

for lst, f in zip(lists, factor):
    result.append([x * f for x in lst])
for res in result:
    print(res) 
print(f'\n')

## exercise 17-24.4 - "print elements on the same line without commas"
lists = [[3, 4, 5, 6], ["a", "b", "c"]]

for lst in lists:
    print(" ".join(map(str, lst)))
print(f'\n')

## exercise 17-24.6 - "get max and min values"
lists = [[3, 4, 5, 6], [-1, -2, -3, -4], [0, 0, 0, 0], []]

for lst in lists:
    if lst:
        print(f'{max(lst)} {min(lst)}')
    else:
        print(f'[]')
print(f'\n')


## exercise 17-24.8 - "check if list is empty or not"
lists = [[], [4], [4, 5, 6, 7]]

for lst in lists:
    if lst:
        print("Not Empty")
    else:
        print("Empty")
print(f'\n')


## exercise 17-24.11 - "prints the elements and their indices"
lists = [[1, 2, 3, 4], ["a", "b", "c"], []]

for lst in lists:
    if len(lst) == 0:
        print("Empty list")
    else:
        for i in lst:
            print(f'{i} {lst.index(i)}')
print(f'\n')


## exercise 17-24.13 - "remove matching element"
lists = [[1, 2, 3, 4], [3, 3, 2, 1], ["a", "b", "c", "b"], [3, 4, 5, 6], []]
elem_remove = [2, 3, "b", 7, 0]
new_list = []

for lst, elem in zip(lists, elem_remove):
    if not lst:
        new_list.append("Empty List")
    elif elem not in lst:
        new_list.append("Not Found")
    else:
        new_lst = [x for x in lst if x != elem]
        new_list.append(new_lst)

for result in new_list:
    print(result)
print('\n')


## exercise 17-24.15 - "remove duplicates from a list"
lists = [[1, 1, 2, 3, 4, 4], ["a", "a", "b", "a"], [1, 2, 3], []]
new_list = []

for sublist in lists:
    new_sublist = []
    seen = set()
    for item in sublist:
        if item not in seen:
            new_sublist.append(item)
            seen.add(item)
    new_list.append(new_sublist)

for sublist in new_list:
    print(sublist)
print(f'\n')


## exercise 17-24.17 - "count elements greater than 3"
lists = [[1, -1, 0, 2, 2, 3], [1, 2, 3, 4], [7, 8, 9, 10], []]
counts = []

for lst in lists:
    count = 0
    for x in lst:
        if x>3:
            count +=1
    counts.append(count)
for cnt in counts:
    print(cnt)
print(f'\n')


## exercise 25-32.1 - "difference between two lists"
listA = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], []]
listB = [[1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 3]]
new_list = []

for lst1, lst2 in zip(listA, listB):
    sublist = [item for item in lst1 if item not in lst2]
    new_list.append(sublist)
    
for subl in new_list:
    print(subl)
print(f'\n')


## exercise 25-32.3 - "distance between two 3d points"
import math

pointA = [[1, 2, 3], [3, 4, 5], [-3, 4, -5]]
pointB = [[1, 2, 3], [1, 3, 5], [2, 0, -4]]
distances = []

for pA, pB in zip(pointA, pointB):
    distance = round(math.sqrt((pB[0] - pA[0])**2 + (pB[1] - pA[1])**2 + (pB[2] - pA[2])**2), 5)
    distances.append(float(distance))
for distance in distances:
    print(distance)
print(f'\n')


## exercise 25-32.5 - "print common elements in two lists"
pointA = [[1, 2, 3], [4, 5, 6], [3, 4, 5], [4, 5, 6]]
pointB = [[1, 2, 3], [1, 4, 5], [1, 2, 3], [1, 2, 3]]
result = []

for pA, pB in zip(pointA, pointB):
    sublist = [item for item in pA if item in pB]
    result.append(sublist) 
for res in result:
    print(res)
print(f'\n')


## exercise 25-32.7 - "find the second largest value"
pointA = [[1, 2, 3, 4], [1, 2], [2], []]

for sublist in pointA:
    if len(sublist) > 1:
        sorted_sublist = sorted(sublist, reverse=True)
        print(sorted_sublist[1])
    else:
        print("None")
print(f'\n')


## exercise 25-32.10 - "find the second smallest  value"
pointA = [[1, 2, 3, 4], [1, 3], [2], []]

for sublist in pointA:
    if len(sublist) > 1:
        sorted_sublist = sorted(sublist, reverse=False)
        print(sorted_sublist[1])
    else:
        print("None")
print(f'\n')


## exercise 25-32.12 - "make a frequency dictionary from the elements of the list"
lists = [["a", "a", "b", "c", "a", "b"], [1, 2, 3, 4, 3, 2, 1, 2]]

for sublist in lists:
    frequency_dict = {}
    for item in sublist:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    print(frequency_dict)
print(f'\n')


## exercise 25-32.14 - "flatten a list that contains list"
lists = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [1, 2, 3, 4, 5, 6, [7, 8, 9]],
         [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]]

for sublist in lists:
    output_list = []
    for item in sublist:
        if isinstance(item, list):
            output_list.extend(item)
        else:
            output_list.append(item)
    print(output_list)
print(f'\n')


## exercise 25-31.16 - "generate all permutations in a list"
from itertools import permutations

lists = [1, 2, 3]

perm = list(permutations(lists))
for p in perm:
    print(list(p))

## exercise 25-32 - "challenge use tuples"
from itertools import permutations

lists = [1, 2, 3]

perm = list(permutations(lists))
for p in perm:
    print(p)


## exercise 33-38.2 - "check if a key exists in a dictionary"
dictionary = [{"a": 4, "b": 6}, {"a": 4, "b": 6}, {}]
keys = ["a", "c", "d"]

for dic, key in zip(dictionary, keys):
    if key in dic:
        print("True")
    else:
        print("False")
print(f'\n')

## exercise 33-38.4 - "add a key value pair only if the key is not in the dictionary"
dictionary = [{"January": 45, "February": 56, "March": 67}, 
              {"January": 45, "February": 56, "March": 67}]

new_key_value = [{"April": 67}, {"January": 67}]

for dic, new_pair in zip(dictionary, new_key_value):
    key, value = list(new_pair.items())[0]
    if key in dic:
        print(f"Key '{key}' already exists.")
    else:
        dic[key] = value
print(dictionary)
print(f'\n')


## exercise 33-38.6 - "merge two dictionaries"
my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

merged_dict = my_dict1|my_dict2
print(merged_dict)
print(f'\n')


## exercise 33-38.9 - "check if all values are equal"
my_dict = [{"a": 4, "b": 4, "c": 4},
           {"a": 4, "b": 6, "c": 4},
           {"a": 4, "b": 6, "c": 10},
           {}]

for dic in my_dict:
    if not dic:  
        print("Empty")
    else:
        values = list(dic.values())
        if all(value == values[0] for value in values):
            print(True)
        else:
            print(False)
print(f'\n')


## exercise 33-38.11 - "find the maximum value in a dictionary"
my_dict = [{"a": 4, "b": 3, "c": 7},{"a": 4, "b": 6},{"a": 4, "b": 4},{}]

for dic in my_dict:
    if not dic:  
        print("None")
    else:
        values = list(dic.values())
        print(max(values))
print(f'\n')


## exercise 33-38.13 "find the minimum value in a dictionary"
my_dict = [{"a": 4, "b": 3, "c": 7},{"a": 4, "b": 6},{"a": 4, "b": 4},{}]

for dic in my_dict:
    if not dic:  
        print("None")
    else:
        values = list(dic.values())
        print(min(values))
print(f'\n')


## exercise 39-44.1 - "find frequency of values in a dictionary"
my_dict = {"a": 4, "b": 4, "c": 2, "d": 7, "e": 4, "f": 2, "g": 7, "h": 7}

freq_dict = {}

for value in my_dict.values():
    if value in freq_dict:
        freq_dict[value] += 1
    else:
        freq_dict[value] = 1

for key, value in freq_dict.items():
    print(f"{key}: {value}")
print(f'\n')


## exercise 39-44.3 - "make a dictionary from nested lists"
nested_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

if not nested_list:
    print("empty")
else:
    my_dict = dict(nested_list)
    print(my_dict)
print(f'\n')


## exercise 39-44.5 - "print the largest sum of values"
my_dict = {
    "a": [1, 2, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 100]
}

max_sum = max(sum(values) for values in my_dict.values())
print(max_sum)
print(f'\n')


## exercise 39-44.8 - "make a frequency dictionary for the characters in a string"
strings = [["Hello, World"], ["Excellent"]]

for s in strings:
    freq_dict = {}
    for char in s[0].lower():  # Convert to lowercase and process each character
        if char.isalpha():  # Only include letters
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    print(freq_dict)
print(f'\n')


## exercise 39-44.10 - "sort lists in ascending order"
my_dict = {
    "a": [4, 3, 2],
    "b": [5, 3, 7],
    "c": [1, 9, 10],
    "d": [3, 4, 1]
}

for key in my_dict:
    my_dict[key] = sorted(my_dict[key])
print(my_dict)
print(f'\n')


## exercise 39-44.12 - "convert an dictionary in a list of lists"
product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

list_of_lists = [[key, value] for key, value in product_info.items()]
print(list_of_lists)
print(f'\n')


## exercise 45-50.2 - "check if zero, positive, negative"
numbers = [3, -1, 0]

for numb in numbers:
    if numb == 0:
        print("Zero")
    elif numb > 0:
        print("Positive")
    else:
        print("Negative")
print(f'\n')


## exercise 45-50.4 - "check vowels and consonants"
vowels = "AEIOUaeiou"
string = "Score: 36"

for char in string:
    if char.isalpha():
        if char in vowels:
            print(f"{char} is a vowel")
        else:
            print(f"{char} is a consonant")
    elif not char.isalpha():
        print(f"{char} is not a letter")
print(f'\n')


## exercise 45-50.6 - "print max of three numbers"
a = [1, 1, 3]
b = [3, 4, 3]
c = [4, 15, 3]

for a1, b1, c1 in zip(a, b, c):
    print(max(a1,b1,c1))
print(f'\n')


## exercise 45-50.9 - "print min of three nunmbers"
a = [1, 2, -1]
b = [2, 2, -3]
c = [3, 2, -4]

for a1, b1, c1 in zip(a, b, c):
    print(min(a1,b1,c1))
print(f'\n')


## exercise 45-50.11 - "challenge four seasons"
season_num = [1, 2, 3, 4]

for seasons in season_num:
    if seasons == 1:
        print("Spring")
    elif seasons == 2:
        print("Summer")
    elif seasons == 3:
        print("Fall")
    elif seasons == 4:
        print("Winter")
    else:
        print('')
print(f'\n')


## exercise 45-50.13 - "compare three numbers"
a = [3, 3, 3, 1]
b = [3, 4, 4, 2]
c = [3, 3, 4, 3]

for a1, b1, c1 in zip(a, b, c):
    if a1 == b1 == c1:
        print("Equal")
    else:
        print("Not Equal")
print(f'\n')


## exercise 51-56.1 - "find number of days in month"
days = {
    "January": 31,
    "February": 28,  # Not considering leap years
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

for month, num_days in days.items():
    print(f"{month} has: {num_days} days.")
print(f'\n')


## exercise 51-56.3 - "increasing or decreasing order"
a = [1, 3, 1, 1]
b = [2, 2, 1, 2]
c = [3, 1, 1, 1]

for a1, b1, c1 in zip(a, b, c):
    if a1 > b1 > c1:
        print("Decreasing Order")
    elif a1 < b1 < c1:
        print("Increasing Order")
    else:
        print("None")
print(f'\n')


## exercise 51-56.5 - "solve quadratic equations"
import math

a_list = [1, 2, 3]
b_list = [2, 5, 4]
c_list = [1, -3, 5]

for a, b, c in zip(a_list, b_list, c_list):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        print("Complex Roots")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"{root}")
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2*a)
        root2 = (-b + math.sqrt(discriminant)) / (2*a)
        print(f"{root1}, {root2}")
print(f'\n')


## exercise 51-56.8 - "check if a year is a leap year or not"
years = [2025, 2033, 1836, 1912]

for yr in years:
    if yr % 4 != 0:
        print(f"{yr} is a common year.")
    elif yr % 100 != 0:
        print(f"{yr} is a leap year.")
    elif yr % 400 != 0:
        print(f"{yr} is a common year.")
    else:
        print(f"{yr} is a leap year.")
print(f'\n')


## exercise 51-56.10 - "interactive calculator"
print("Welcome to the Interactive Calculator!")

num1, num2 = float(input("Enter the first number: ")), float(input("Enter the second number: "))
print("These are the available options, choose one.")
print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Integer Division\n6 - Modulo")
operation = int(input("Enter the number of the operation: "))

if operation == 1:
    result, op = num1 + num2, "+"
elif operation == 2:
    result, op = num1 - num2, "-"
elif operation == 3:
    result, op = num1 * num2, "*"
elif operation == 4:
    result, op = num1 / num2 if num2 != 0 else "Error: Division by zero", "/"
elif operation == 5:
    result, op = num1 // num2 if num2 != 0 else "Error: Division by zero", "//"
elif operation == 6:
    result, op = num1 % num2 if num2 != 0 else "Error: Division by zero", "%"
else:
    result = "Please choose a valid operation"

print(f"The result of {num1} {op} {num2} is {result}" if isinstance(result, float) else result)
print(f'\n')


## exercise 51-56.12 - "rock, paper, scissors"
import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You lose!"

print("Welcome to Rock, Paper, Scissors!")
player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
computer_choice = get_computer_choice()

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")

result = get_winner(player_choice, computer_choice)
print(result)
print(f'\n')


## exercise 57-63.2 - "print the first 15 positive integers"
for i in range(1, 16):
    print(i)
print(f'\n')


## exercise 57-63.4 - "print integers in reverse order"
n = int(input('Please enter a number: '))

for i in range(n, 0, -1):
    print(i)
print(f'\n')


## exercise 57-63.6 - "sum of first 100 positive integers"
total_sum = 0

for i in range(1, 101):
    total_sum += i
print(f"{total_sum}")
print(f'\n')


## exercise 57-63.8 - "print the multiplication table"
n = int(input("Enter the value of n: "))

print(f"Multiplication table for {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print(f'\n')


## exercise 57-63.11 - "print the alphabet using a loop"
import string

for letter in string.ascii_uppercase:
    print(letter)
print(f'\n')


## exercise 57-63.13 - "first 100 even numbers"
for i in range(2, 201, 2):
    print(i)
print(f'\n')


## execise 57-63.15 - "calculate factorial"
print("Welcome to Calculator Factorial!")
n = int(input("Please enter number n:"))
factorial = 1
if n == 0:
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial *= i
print(f"The factorial of {n} is: {factorial}")
print(f'\n')


## exercise 57-63.1 - "use while loops"
print("Welcome to Calculator Factorial!")
n = int(input("Please enter number n:"))
factorial = 1
if n == 0:
    factorial = 1
else:
    i = 1
    while i <= n:
        factorial *= i
        i += 1
print(f"The factorial of {n} is: {factorial}")
print(f'\n')


## exercise 64-71.1 - "check if the number is prime"
numbers = [4, 15, 1, 3, 2, 0]

for n in numbers:
    if n <= 1:
        print(f"{n}: Not prime")
        continue
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n}: Not prime")
            break
    else:
        print(f"{n}: Prime")
print(f'\n')


## exercise 64-71.3 - "print a pattern using loops"
n = int(input("Please enter a number n to generate pattern:"))

for i in range(1, n + 1):
    print('*' * i)
print(f'\n')


## exercise 64-71.5 - "print digits in reverse order"
numbers = [1, 123, 3456, 1111, 2662]

for n in numbers:
    reversed_number = int(str(n)[::-1])
    print(reversed_number)
print(f'\n')


## exercise 64-71.7 - "reverse a string using a loop"
strings = ["Hello", "World", "Python"]

for s in strings:
    reversed_s = str(s)[::-1]
    print(reversed_s)
print(f'\n')


## exercise 64-71.10 - "print half pyramid using loop"
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
print(f'\n')


## exercise 64-71.12 - "Floyd's Triangle"
n = int(input("Enter the number of rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
    print()


## exercise 64-71.14 - "triangular letters pattern"
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    letter = chr(64 + i)  # Convert to the corresponding uppercase letter
    print((letter + ' ') * i)


## exercise 64-71.16 - "diamond mad with asterisk"
while True:
    height = int(input("Enter the height of the diamond (odd number): "))

    if height % 2 != 0:
        break
    else:
        print("Please enter an odd number for the height.")

    # Print the upper part of the diamond
for i in range(1, height + 1, 2):
    print(' ' * ((height - i) // 2) + '*' * i)

    # Print the lower part of the diamond
for i in range(height - 2, 0, -2):
    print(' ' * ((height - i) // 2) + '*' * i)


## exercise 72-76.2 - "find the sum of a list using recursion"
def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

lists = [[1, 2, 3], [4, 5, 6], [-1, 2, 0], [0, 0, 0], []]

for lst in lists:
    total = recursive_sum(lst)
    print(total)


## exercise 72-76.4 - "find the nth fibonacci number"
numbers = [0, 1, 2, 3, 9]

for n in numbers:
    if n <= 0:
        fibonacci = 0
    elif n == 1:
        fibonacci = 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        fibonacci = b
    print(f"{n} : {fibonacci}")


## exercise 72-76.6 - "recursive factorial"
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

numbers = [0, 1, 5, 8]

for n in numbers:
    print(f"{n} : {factorial(n)}")


## exercise 72-76.9 - "find the sum of the digits of a positive integer"
def sum_of_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_of_digits(num // 10)

numbers = [2, 23, 111, 1234]

for num in numbers:
    print(f"{num} : {sum_of_digits(num)}")


## exercise 72-76.11 - "solve a power recursively"
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

a = [2, 3, 2, 5]
b = [0, 1, 3, 2]

for base, exponent in zip(a, b):
    print(f"The value of {base} raised to the power {exponent} is: {power(base, exponent)}")


## exercise 77-82.1 - "find the greatest common divisor"
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = [60, 42, 7, 6]
b = [48, 56, 3, 2]

for num1, num2 in zip(a, b):
    print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")


## exercise 77-82.3 - "check if a string is a palindrome"
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    # Recursive case: check the first and last characters and recurse on the remaining substring
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

strings = ["Hello", "Anna", "", "World"]

for s in strings:
    print(f"{s}: {is_palindrome(s)}")


## exercise 77-82.5 - "count vowels in a string"
def vowels(n):
    if n == "":
        return 0
    elif len(n) == 1 and n.lower() not in "aeiou":
        return 0
    elif n[0].lower() in "aeiou":
        return 1 + vowels(n[1:])
    else:
        return vowels(n[1:])

strings = ["H", "Python", "Cake", "Amazing"]

for s in strings:
    print(f"{s} : {vowels(s)}")


## exercise 77-82.8 - "print a pattern using recursion"
def print_pattern(n):
    if n > 0:
        print('*' * n)
        print_pattern(n - 1)

n = int(input("Enter the number of rows (n): "))

print_pattern(n)


## exercise 77-82.10 - "convert from decimal to binary with recursion"
def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
    
inputs = [0, 5, 34, 567]

for num in inputs:
    print(f"{num} : {decimal_to_binary(num)}")


## exercise 77-82.12 - "implement bianry search recursively"
def binary_search(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if high >= low:
        mid = (low + high) // 2
        
        # Check if the element is present at the middle
        if arr[mid] == x:
            return mid
        # If the element is smaller than mid, it's in the left subarray
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)
        # Else, the element is in the right subarray
        else:
            return binary_search(arr, x, mid + 1, high)
    else:
        # Element is not present in the array
        return -1

lists = [[1, 2, 3], [1, 2, 3, 4], [4, 5, 6, 7]]
elements = [2, 0, 6]

for lst, elem in zip(lists, elements):
    result = binary_search(lst, elem)
    print(f"Element {elem} in list {lst}: Index {result}")


## exercise 83-87.2 - "read a text file"
with open('example.txt', 'r') as file:
    file_content = file.readlines()

print(file_content)


## exercise 83-87.4 - "print the first n line of a file"
n = int(input("Enter the number of lines to print: "))

with open('example.txt', 'r') as file:
    file_content = [line.strip() for line in file]

num_lines = len(file_content)
if n > num_lines:
    print(f"Please enter a valid value for n. The file has {num_lines} lines.")
else:
    for line in file_content[:n]:
        print(line)


## exercise 83-87.7 - "print the last n line of a file"
n = int(input("Enter the number of lines to print: "))

with open('example.txt', 'r') as file:
    file_content = [line.strip() for line in file]

num_lines = len(file_content)
if n > num_lines:
    print(f"Please enter a valid value for n. The file has {num_lines} lines.")
else:
    for line in file_content[-n:]:
        print(line)


## exercise 83-87.9 - "find the longest word in a file"
with open('words.txt', 'r') as file:
    file_content = file.read()

# Find the longest word
words = file_content.split()
longest_word = max(words, key=len)

print(f"{longest_word}")


## exercise 83-87.11 - "make frequency dictionary of the words in a file"
with open('words.txt', 'r') as file:
    
    frequency_dict = {}
    
    for line in file:
        word = line.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase
        if word:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1

print(frequency_dict)


## exercise 88-91.1 - "write a list to a file"
elements = [1, 2, 3, 4, 5]

with open('output.txt', 'w') as file:
    for elem in elements:
        file.write(f'{elem}\n')


## exercise 88-91.3 - "count characters in a file"
with open('char_count.txt', 'r') as file:
    character_count = len(file.read().replace('\n', '').replace(' ', ''))

print(f"Total number is characters : {character_count}")


## exercise 88-91.6 - "copy the content of a file to another file"
source_file = 'char_count.txt'

destination_file = 'destination.txt'

with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    dest.write(src.read())

print(f"Content copied from {source_file} to {destination_file}.")


## exercise 88-91.8 - "check if a file exists"
import os

file_path = 'example.txt'

if os.path.isfile(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")


## exercise 92-97.2 - "display current date and time"
from datetime import datetime

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

print(f"{current_date} {current_time}")


## exercise 92-97.4 - "convert seconds to minutes and hours"
seconds = [5400, 7200]

for secon in seconds:
    mins = secon / 60
    hours = mins / 60
    print(f'{secon} is equivalent to {mins} minutes or {hours} hour(s).' )


## exercise 92-97.6 - "calculate the area of a circle"
import math

diameter = [0, 10, 14]

for d in diameter:
    radius = d/2
    area = math.pi*(radius)**2
    print(f"The area of {d} is: {round(area,2)}")


## exercise 92.97.9 - "compute the area of a triangle"
base = int(input("Please enter the value of your base:"))
height = int(input("Please enter the value of your height:"))

if base < 0 or height < 0:
    print("Please enter valid value!")
else:
    area = (base * height) / 2
    print(f"The area of the given triangle is {area:.2f}")


## exercise 92-97.11 - "celsius to farenheit conversion"
degrees_celsius = float(input("Enter degrees Celsius: "))

degrees_fahrenheit = (degrees_celsius * 9/5) + 32

print(f"{degrees_celsius} Celsius = {degrees_fahrenheit} Fahrenheit")


## exercise 92-97.13 - "farenheit to celsius conversion"
degrees_fahrenheit = float(input("Enter degrees Farenheit: "))

degrees_celsius = (degrees_fahrenheit - 32 ) * 5/9

print(f"{degrees_fahrenheit} Fahrenheit = {degrees_celsius} Fahrenheit")


## exercise 98-101.1 = "calculate body mass index"
height_cm = int(input("Enter your height in centimeters: "))
weight_kg = int(input("Enter your weight in kilograms: "))

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is {bmi:.2f}, which is considered {category}.")


## exercise 98-101.3 - "print a calendar"
import calendar

try:
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    if 1 <= month <= 12:
        print(calendar.month(year, month))
    else:
        print("Invalid month. Please enter a value between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter integer values for month and year.")


## exercise 98.101.6 - "find the number of days between two dates"
from datetime import datetime

date1 = input("Enter the first date (Year Month Day): ")
date2 = input("Enter the second date (Year Month Day): ")

date_format = "%Y %m %d"
try:
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
except ValueError:
    print("Invalid date format. Please use the format: Year Month Day (e.g., 2021 1 15).")
    exit()

if d1 > d2:
    print("Please enter valid dates. The first date must be previous or equal to the second date.")
else:
    delta = (d2 - d1).days

    if delta == 0:
        print("The dates are equal.")
    elif delta == 1:
        print("There is 1 day between these dates.")
    else:
        print(f"There are {delta} days between these dates.")


## exercise 98-101.8 - "check a pattern using a regular expression"
import re

input_string = input("Enter a string: ")

pattern = "^My[\w\s]+blue$"

if re.search(pattern, input_string):
    print("Match")
else:
    print("Not Match")