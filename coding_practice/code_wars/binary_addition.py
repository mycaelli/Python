def add_binary(a, b) :
    """this function adds two numbers together and returns their sum in binary"""
    binary = bin(a+b)
    return str(binary[2:])

print(add_binary(1, 1))