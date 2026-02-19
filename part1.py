from random import randint


ranNum = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): 
    ranNum.append(randint(1, 50))


print(ranNum) #print the list!
