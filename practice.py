'''
Mock Lab-Based Practical – Version 2

Open this file in IDLE editor and complete all 5 tasks.

Each task has a prompt and you must write your code where it says:

"your code here"

Once done, save and upload the file as instructed.

Name: ________________________

Student ID: ___________________
'''

'''
Task 1 - Even or Odd:
Ask the user for a number and print whether it's even or odd.
'''

number = int(input("Enter a number: "))

if "your code here":
    print("your code here")
else:
    print("your code here")

# Total for Task 1 (10 marks)


'''
Task 2 - Number Guesser:
Keep asking the user to guess a secret number (e.g., 7) until they get it right.
Then print a success message.
'''

secret = 7
guess = None

while "your code here":
    guess = int(input("Guess the number: "))
    if "your code here":
        print("Correct! You guessed it.")
    else:
        print("Wrong. Try again.")

# Total for Task 2 (20 marks)


'''
Task 3 - Display Multiples:
Ask user for a number and print the first 5 multiples of that number using a loop.
'''

num = int(input("Enter a number to see its first 5 multiples: "))

for "your code here":
    print("your code here")

# Total for Task 3 (20 marks)


'''
Task 4 - Function to Count Vowels:
Write a function that takes a word as input and returns how many vowels it has.
Call the function and display the result.
'''

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for "your code here":
        if "your code here":
            count += 1
    return count

user_word = input("Enter a word: ")
result = count_vowels(user_word)
print(f"Number of vowels: {result}")

# Total for Task 4 (25 marks)


'''
Task 5 - Student Pass/Fail:
Ask how many students' results to enter.
For each student, ask for name and marks.
Print “Pass” if marks >= 50, else “Fail”.
'''

num_students = int(input("How many students? "))

for "your code here":
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    if "your code here":
        print(f"{name} has Passed")
    else:
        print(f"{name} has Failed")

# Total for Task 5 (25 marks)
