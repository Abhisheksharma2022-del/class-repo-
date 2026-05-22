# WAF to count total vowels in a given string using return

# def count_vowels():
#     text = input("Enter a string: ")
    
#     count = 0

#     for ch in text.lower():
#         if ch in "aeiou":
#             count += 1

#     return count


# result = count_vowels()
# print("Total vowels =", result)

## WAF to count character "p" in "python programming"
# and return total occurrence

# count = 0
# def count_char():
#     text = "python programming"
#     global count
#     for ch in text.lower():
#         if ch == "p":
#             count += 1

#     return count

# result = count_char()
# print("Total occurrence of p =", result)

# WAF to retun sum of strings indexes . 
total=0
def indexCheck(str):
    global total
    for i in range (len(str)):
        total+=i
    return total
res=indexCheck("python")
print(res)
