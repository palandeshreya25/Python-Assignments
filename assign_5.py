numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Calculate the sum of all the elements in the list
sum_of_numbers = sum(numbers)
print("Sum of all the numbers:", sum_of_numbers)

# Find the smallest number
smallest_number = min(numbers)
print("Smallest number:", smallest_number)

# Find the largest number
largest_number = max(numbers)
print("Largest number:", largest_number)

# Display list in ascending order
ascending_order = sorted(numbers)
print("List in ascending order:", ascending_order)

# Display list in descending order
descending_order = sorted(numbers, reverse=True)
print("List in descending order:", descending_order)

# Convert list into tuple
numbers_tuple = tuple(numbers)
print("List converted to tuple:", numbers_tuple)

# Delete the list
del numbers
print("List deleted")