input_string = str(input("Input: "))
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result
output_string = remove_vowels(input_string)
print("Output: ", output_string)
