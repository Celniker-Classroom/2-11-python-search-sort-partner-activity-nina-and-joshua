from random import randint


ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): 
    ranNums.append(randint(1, 50))

print("The list is: " + str(ranNums))

searchNumber = randint(1,50)

print("Searching for number "+ str(searchNumber))

comparisons = 0 
found = False

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found


for i in ranNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if i == searchNumber:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

if found == True:
    print("Number " + str(searchNumber) + " found in " + str(comparisons) + " comparisons")
if found == False:
    print("Number " + str(searchNumber) + " not found in " + str(comparisons)+ " comparisons")


