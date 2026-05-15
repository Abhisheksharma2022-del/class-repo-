# # # wap to print the total of even number from 1 to 15 .

# # total = 0

# # for num in range(1, 16):

# #     if num % 2 == 0:
# #         total = total + num

# # print("Total of even numbers =", total)

# #wap to check the give string by user is "polindrome" or "not polindrom"


# text = "madam"

# copy_text = text
# rev = ""

# i = len(text) - 1

# while i >= 0:
#     rev = rev + text[i]
#     i -= 1

# if copy_text == rev:
#     print("Palindrome")

# else:
#     print("Not Palindrome")



#wap to reverse a digit : 1234 output : 4321


num = 1234

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse Number =", rev)
