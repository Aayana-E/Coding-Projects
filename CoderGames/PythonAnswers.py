# 1.) Declare a variable and assign it to an integer, then output the number raised to the power of 3.

number = 4
print(number**3) # ** = exponents 

#2.) Declare a variable and assign it to the list [1,2,3,4,5]. Calculate then output the sum of the list.

number = [1,2,3,4,5]
total = 0
for i in range(5):
    total += number[i]

# 3
# Print the numbers from 1 to 100 
# and skip anything that is divisible by 9.
# 20pts
for i in range(1,101):
    # % = mod = remainder
    # 4 % 2 = 0
    # 5 % 2 = 1
    if i % 9 == 0:
        continue
    else:
        print(i)

# 4.) Declare a variable and assign it to "Programming isn't about what you know; it's about what you can figure out." then calculate the count of the number of words in the variable and output the number.
# 30pts

number = "Programming isn't about what you know; it's about what you can figure out." 
number = number.split(" ")
print(number)
print(len(number))


# 5 Declare a variable and assign it to any number, and output the last digit of the number. 
# Input 2345 would output 5, while 9876 would output 6.
# 30pts
number = 43252
number = str(number)
print(type(number))
print(number[len(number)-1])

# 6
# Declare a variable and assign it to a string value. 
# Then output the string where each letter in the word must be one of these characters:
#  't', 'u', 'r', 'i', 'n', 'g'. Otherwise omit that letter. 
# An example would be: 'fun rigid' would output: 'unrigi'.
# 30pts


# 7
# Declare a variable and assign it to the list [1,2,3,4,5]. 
# Calculate then output the list in reverse order. We will be changing the values when grading.
# 40pts


# 8
# Declare a variable and assign it to a string "seven". Output the string with 1 of the first letter followed by 2 of the second letter followed by 3 of the third letter and so on. We will be changing the values when grading.
# 40pts


# 9
# Declare a variable and assign it to a positive integer. Take the remainder of the number divided by 7, assume 0 is "Sunday", and 6 is "Saturday", and the other days in string form correspond to numbers accordingly. Output which day of the week it is. We will be changing the values when grading.
# 50pts


# 10
# Declare a variable and assign it to "froglizardfroglizard". Output True if "frog" and "lizard" appear the same amount of times. Output False if different. We will be changing the values when grading.
# 50pts


# 11
# Declare a variable and assign it to the list[8,6,2,8,7,5,2]. Return the sum of the numbers in the list, except leave out any 8's or 2's. The example would return the answer 18. We will be changing the values when grading.
# 50pts


# 12
# Declare two variables, list1 and list2, and assign them to [1,2,3] and [4,5,6]. Convert them into a dictionary named dict1 in a way that item from list1 is the key and item from list2 is the value.
# 60pts


# 13
# Declare two variables assigned to two positive integers, then output the greatest common divisor of the two numbers. (105,45) would output 15, while (36, 42) would output 6.
# 70pts


# 14
# Declare an integer called debitcard and assign it to 4253665879515786. Output "valid" if the values are valid. Use these rules to determine if the debit card number is valid.
# 1. It must start with a 4, 5, or 6.
# 2. It must contain exactly 16 digits.
# 3. It can not have 4 or more consecutive repeated digits.
# NOTE: We will be changing the values when grading.
# 80pts


# 15
# Declare a string and assign it to "135246ABCzyx". Output the sorted version of the string using these rules.
# 1. Sorted uppercase letters are ahead of lowercase letters.
# 2. Sorted lowercase letters are ahead of digits.
# 3. Sorted odd digits are ahead of sorted even digits.
# NOTE: We will be changing the values when grading.
# 80pts


# 16
# Declare a list and assign it to ["Everywhen", "Erf", "Bumbershoot", "Cleek", "Finifugal"]. Output the score of the list based on the rule that each string has a value of 2 if the number of vowels in the string is odd, 1 otherwise. The answer of the current list is 7. We will be changing the values when grading.
# 90pts


# 17
# Implement bubble sort and call it on a list of 10 numbers, sorting from smallest to largest. Output the sorted list. You cannot use a library for this solution.
