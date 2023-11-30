message = input("Enter encoded: ")  # Remove the str() conversion

encoded_list = message.strip("[]").split(",")  # Split the input list by comma and remove square brackets
encoded_string = ""

for code in encoded_list:
    code = code.strip()  # Remove any leading or trailing whitespace
    code = code.zfill(4)  # Fill each number to 4 characters with leading zeroes
    encoded_string += code

print("-------------")
print(encoded_string)
