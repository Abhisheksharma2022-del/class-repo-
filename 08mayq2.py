  # wap to take a number from user input input and print formated table . 
    # # format:
    # 3x1=3
    # 3x2=6
    # 3x3=9
    # ....
    # 3x10=30

print("Table printer")

x= int(input("Enter the number::: "))
for i in range(1,11,1):
    y= i * x
    print(f"{x} * {i} = {y}", end=" ")