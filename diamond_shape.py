# Program by: Shervin Marco Mangulabnan 
# Date of Creation: September 26, 2024
# Purpose: A program that generates a diamond shape using the "*" character, based on an odd integer "n".

n = int(input("Please enter an odd integer: ")) #ask user to enter an odd integer

# Check if n is an odd integer
if n % 2 == 0:
    print("Please provide an odd integer.")
else:
    # Calculate the number of rows for the top half and the bottom half
    rows = n // 2 + 1
    
    # Print the top half of the diamond
    for i in range(rows):
        stars = 2 * i + 1  # Number of stars in the current row
        spaces = rows - i - 1  # Number of leading spaces
        print(' ' * spaces + '*' * stars)
        
    # Print the bottom half of the diamond
    for i in range(rows - 2, -1, -1):
        stars = 2 * i + 1  # Number of stars in the current row
        spaces = rows - i - 1  # Number of leading spaces
        print(' ' * spaces + '*' * stars)
