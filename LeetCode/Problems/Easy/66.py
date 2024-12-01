#Plus One

digits = [4,3,2,1]
digits = [9,9,9]

if digits[-1] != 9:
    digits[-1] += 1

else:
    i = len(digits)-1
    carry = 1

    while i > -1:
        if (digits[i] + carry) > 9:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += carry
            carry = 0
            break
        i -= 1
    
    if carry == 1:
        digits.insert(0,1)

print(digits)
