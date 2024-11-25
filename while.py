#Cristian Garcia
#11/19/24

#Problem 1 this program prints out the word infinite an infinite ammount of times 


i = 1

# Starts a while loop that will run as long as i equals True
while i == True:

    #Prints infinite 
    print("Infinite")


#Problem 2 This program creates a list with two initial numbers, then adds the numbers 0 through 10 to the list, and finally prints the total number of elements and the third element in the list.


# A list with two elements: 57 and 83
L = [57, 83]

# Starts the counter variable to 0
counter = 0

# A while loop that runs as long as the counter is less than or equal to 10
while counter <=10:
   L.append(counter) # Append the current value of counter to the list L
   counter += 1 # Increase the counter by 1 after each iteration

print("The list has," ,len(L), "elements")
print("The third element in the list has," ,L[10],)

#Problem 3 This program asks the user to enter numbers then adds them to a list and keeps a running total t stops when the sum of the numbers in the list is grater than 100.

#Starts an empty list to store the numbers
numbers = []

# Starts a variable to keep track of the sum of numbers
sum = 0

# A while loop that continues as long as the sum is less than or equal to 100
while sum <= 100:
    num = input ("Enter a number: ")
    num = int(num) # Convert the input to an integer
    numbers.append(num) # Append the number to the list of numbers
    sum += num # Add the entered number to the sum

print("List of numbers:" ,numbers,)
print("Sum of numbers:" ,sum,)



