# warp to sum of the indices of a string : "python".

text = "python"

# variable to store sum of indices
sum_indices = 0

# loop through indices
for i in range(len(text)):
    sum_indices = sum_indices + i

# print final result
print("Sum of indices =", sum_indices)

# warp to print the factorial from 1 to 8. 

factorial = 1

for i in range(1, 9):
    factorial = factorial * i
print("Factorial of", i, "=", factorial)

    # wap to print only prime number from 1 to 15 . 


for num in range(1, 16):

    if num > 1:

        prime = True

        for i in range(2, num):

            if num % i == 0:
                prime = False

        if prime:
            print(num)


          
    


