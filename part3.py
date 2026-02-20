from random import randint

ranNums = [] #name your list and make sure it is empty!
def make_list():
    for i in range(10): 
        ranNums.append(randint(1, 50))
    print("The list is: " + str(ranNums))


def findUserNum():
    searchNumber = input("Enter a number between 1 and 50: ")
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


def find_smallest():
    smallest=min(ranNums)
    print("The smallest number is "+ str(smallest))

def find_biggest():
    biggest = max(ranNums)
    print("The largest number is " + str(biggest))

def find_sum():
    sum = 0
    for i in ranNums:
        sum = sum + i
    print("The sum is "+ str(sum))
def reverse_list():
    ranNums.reverse()
    print("List reversed: "+str(ranNums))
def remove_duplicates():
    duplicates = set(ranNums)
    print("Now without duplicates: " + str(duplicates))

def onlyEvens():
    evens = []
    for i in ranNums:
        if i % 2 == 0:
            evens.append(i)
    print("Only the evens: "+ str(evens))

make_list()
findUserNum()
find_smallest()
find_biggest()
find_sum()
ranNums.sort()
print(ranNums)
reverse_list()
remove_duplicates()
onlyEvens()