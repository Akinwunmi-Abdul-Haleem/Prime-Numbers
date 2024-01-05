print("Enter a number:")


def prime_numbers(limit):
    for num in range(1, limit + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=' ')


prime_numbers(int(input()))
