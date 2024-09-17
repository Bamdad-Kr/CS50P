def camel_to_snake(name):
    result = ""
    for char in name:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result.lstrip('_')
name = str(input("camelCase: "))
print("snake_case:", camel_to_snake(name))
