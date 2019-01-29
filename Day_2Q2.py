name = input("Enter any string:")
alpha = 0
digit = 0

for item in name:
    if item.isalpha():
        alpha = alpha + 1
    if item.isdigit():
        digit = digit + 1

print ("No of alphas :", alpha)
print ("No of digits :", digit)


