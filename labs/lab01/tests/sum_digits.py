def sum_digits(n):
    sum = 0
    while n != 0:
        sum = sum + n % 10
        n = n // 10
    return sum
    #print(sum)

#sum_digits(10)
#sum_digits(28)
