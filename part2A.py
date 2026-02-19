from random import randint




ranNums = [] #name your list and make sure it is empty!




# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10):
    ranNums.append(randint(1, 50))


print("The list is: " + str(ranNums))


searchNumber = randint(1,50)


print("Searching for number "+ str(searchNumber))


for i in ranNums:
    if searchNumber in ranNums:
        print("Found "+ str(searchNumber)+ " in the list.")
        break


    else:
        print("Number " + str(searchNumber) +" not found in list.")
        break