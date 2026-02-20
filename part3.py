from random import randint

ranNums = [] #name your list and make sure it is empty!
def make_list():
    for i in range(10): 
        ranNums.append(randint(1, 50))
    print("The list is: " + str(ranNums))


searchNumber = input("Enter a number between 1 and 50: ")

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
    print(ranNums)
def remove_duplicates():
    set(ranNums)
    print(ranNums)
make_list()
find_smallest()
find_biggest()
find_sum()
ranNums.sort()
print(ranNums)
reverse_list()
remove_duplicates()