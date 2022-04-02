
def selfDividingNumbers(left, right):
    is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit  in str(num))
    return filter(is_self_dividing, range(left, right + 1))

print(selfDividingNumbers(120, 130))               


