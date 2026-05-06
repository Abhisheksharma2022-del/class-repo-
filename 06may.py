# wrap to print the last digit of and number is 456735
#print (456735%10)
num1=3
num2=9
num3=12
#wap to find Largest number 
#wap to find smallest number 
# Largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("Largest:", largest)
print("Smallest:", smallest)


