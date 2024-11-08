def rev_bits(num):
    result = 0
    while num > 0:
        result = (result << 1) | (num & 1)
        num = num >> 1
    return result

number = int(input("Enter your original number: "))
reversed_number = rev_bits(number)

print("Reversed Number:", reversed_number)
