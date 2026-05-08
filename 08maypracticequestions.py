# wap to takes start_point and end_point from user input and print all number divisible by 2 and 3.

start_point = int(input("Enter start point: "))
end_point=int(input("Enter end point:"))
print("number divisible by both 2 and 3:")

for i in range(start_point, end_point+1):
    # condition check 
    if i % 2 == 0 and i % 3 == 0:
        print(i,end=" ")


    



