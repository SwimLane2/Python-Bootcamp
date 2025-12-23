# print(0.1 + 0.2 == 0.3)

# import decimal

# a = decimal.Decimal('0.1')
# b = decimal.Decimal('0.2')
# print(a + b)

# item_prices1 = 19.90
# item_prices2 = 5.70
# item_price3 = 3.20
# total_price = item_prices1 + item_prices2 + item_price3
# print(total_price)
# print(f"{total_price:.4f}")

# print("Hello", "World")

# print("Python", "is", "fun", sep="-", end="!")# Your code here

# # Part 1-2 - Create variables 
# num1 = 0.1
# num2 = 0.2
# # Part 6 - Import Decimal class
# import decimal

# # Part 7-8 - Create decimal variables
# num1_decimal = decimal.Decimal(str(num1))
# num2_decimal = decimal.Decimal(str(num2))

# # Part 9 - Print the stringified Decimal versions of the decimal variables
# print(num1_decimal + num2_decimal)

# basket = ["apple", "banana", "orange"]
# for item in basket:
#     print(item)

# def calculate_average(numbers):
#     """
#     Calculate the average of a list of numbers.
    
#     Args:
#         numbers (list): A list of numeric values.
    
#     Returns:
#         float: The average (mean) of the numbers in the list.
    
#     Raises:
#         ZeroDivisionError: If the list is empty.
#         TypeError: If the list contains non-numeric values.
    
#     Example:
#         >>> calculate_average([10, 20, 30])
#         20.0
#         >>> calculate_average([5, 15])
#         10.0
#     """
#     # Start typing here and watch Copilot suggest the function body
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average

# #function to reverse a string
# def reverse_string(s):
#     """
#     Reverse the given string.
    
#     Args:
#         s (str): The string to be reversed.
    
#     Returns:
#         str: The reversed string.
    
#     Example:
#         >>> reverse_string("hello")
#         'olleh'
#         >>> reverse_string("Python")
#         'nohtyP'
#     """
#     # Start typing here and watch Copilot suggest the function body
#     return s[::-1]  

def add(a, b):
    return a + b

