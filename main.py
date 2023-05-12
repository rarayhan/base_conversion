def convert_base(number, base_in, base_out):
    decimal_number = int(str(number), base_in)
    converted_number = ""
    
    while decimal_number > 0:
        remainder = decimal_number % base_out
        converted_number = str(remainder) + converted_number
        decimal_number = decimal_number // base_out
    
    return converted_number

# Example usage:
number = "FF"  # Number in base 16 (hexadecimal)
base_in = 16   # Base of the input number
base_out = 2   # Base to convert to (binary)

result = convert_base(number, base_in, base_out)
print(result)  # Output: 11111111
