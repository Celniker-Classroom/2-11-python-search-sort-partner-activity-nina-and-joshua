from random import randint


ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): 
    ranNums.append(randint(1, 50))

print("The list is: " + str(ranNums))


searchNumber = input("Enter a number between 1 and 50.")

def find_smallest():
    smallest=min(ranNums)
    print(smallest)
find_smallest()