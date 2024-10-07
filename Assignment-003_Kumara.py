#1.Write a Python function to find the maximum of three numbers
# def find_max(q,w,r):
#     if q>w and q>r:
#         print(f" {q} is the maximum number ")
#     elif w>q and w>r:
#         print(f" {w} is the maximum number ")
#     else:
#         print(f"{r} is the maximum number")
#
# find_max(10,20,30)

#2.Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

#list=[8,2,3,-1,7]
# def mul():
#     result = 1
#     for i in list:
#         result *= i
#     return result
# multiplication = mul()
# print(f"{multiplication} is the product")

#3.Write a Python program to reverse a string.
#Sample String: "1234abcd"


#def reverse_string(s):
#         return s[::1]
#
#     # Example usage:
# string = "1234abcd"
# reverse = reverse_string(string)
# print(f"Reversed string: {reverse}")


#4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
#
# # Example usage:
# number = int(input("Enter Factorial Number:"))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

#5.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def unique_elements(input_list):
#     return list(set(input_list))
#
# # Example usage:
# numbers = [1, 2, 3, 3, 3, 3, 4, 5]
# unique_numbers = unique_elements(numbers)
# print(f"Unique elements: {unique_numbers}")

#Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# num = int(input("Enter the Number:" ))
# Negative numbers, 0 and 1 are not primes
# num = number
# if num > 1:
#
#     # Iterate from 2 to n // 2
#     for i in range(2, (num // 2) + 1):
#
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

#7.Write a Python program to print the even numbers from a given list.

# list=[4,6,8,9,12,13,15]
# def print_even():
#    even_numbers = []
#    for i in list:
#         if i%2==0:
#             even_numbers.append(i)
#
#    print("Even numbers:", even_numbers)

#print_even()

#8.Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
#
# def count_case_letters(input_string):
#     upper_count = 0
#     lower_count = 0
#
#     for char in input_string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#
#     return upper_count, lower_count
#
#
# # Example usage:
# input_string = "Hello World!"
# upper, lower = count_case_letters(input_string)
# print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

#9.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# def sum_numbers(number_list):
#     total = 0
#     for number in number_list:
#         total += number
#     return total
#
# # Example usage:
# numbers = [8, 2, 3, 0, 7]
# result = sum_numbers(numbers)
# print(f"The sum of the numbers is: {result}")

#10.Write a Python function that checks whether a passed string is a palindrome or not.

# def is_palindrome(input_string):
#     # Normalize the string by removing spaces and converting to lowercase
#     #normalized_string = input_string.replace(" ", "").lower()
#     # Check if the string is equal to its reverse
#     return input_string == input_string[::-1]
#
# # Example usage:
# test_string = "madam"
# result = is_palindrome(test_string)
# print(f"Is the string a palindrome? {result}")