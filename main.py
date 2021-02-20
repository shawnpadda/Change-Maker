# Name - Sirpreet Padda
# Class - MCSCI - 270

# Listing 5.6 - Multiplication Table
print("      Multiplication Table")

# Display the number title
print(" |", end =  ' ')
for j in range(1, 10):
    print(" ", j, end = ' ')

# Jump to the new line
print()
print("_________________________________________________________")

# Display table body
for i in range(1, 10):
    print(i, "|", end = ' ')
    for j in range(1, 10):
        print(format(i * j, "4d"), end = ' ') # Display the product and align properly
    print() # Jump to new line
