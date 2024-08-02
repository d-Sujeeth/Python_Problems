def find_even_numbers(numbers):
    even_numbers = []  # Initialize an empty list to store even numbers
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)  # Add the even number to the list
    return even_numbers  # Return the list of even numbers

# Test the function
output_list = find_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(output_list)  # Expected output: [2, 4, 6, 8, 10]
