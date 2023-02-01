print('Q2. Write a program that prints ‘Hello World’ to the screen.')
print('Hello World')


print('Q3. Write a program that prints a multiplication table for numbers up to 12.')


def multiplication_table():
    for i in range(1, 13):
        print(f'{i}: ', end='')
        for j in range(1, 13):
            print(j*i, end=' ')
        print()


multiplication_table()


print('Q4. Write a function that tests whether a string is a palindrome and test it in your program.')


def is_palindrome(user_input):
    processed_input = user_input.lower().replace(' ', '')
    if processed_input == processed_input[::-1]:
        print(f'The string you entered: "{user_input}" is a palindrome!')
        return
    print(f'The string you entered: "{user_input}" is not a palindrome!')


is_palindrome('Hello')
is_palindrome('ABBA')

print('Q5. Write a function that combines two lists by alternatingly taking elements, '
      'e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3] and test it in your program.')


def combine_lists(list_a, list_b):
    combined_list = list()
    if len(list_a) > len(list_b):
        length = len(list_a)
    else:
        length = len(list_b)

    for i in range(length):
        if i <= len(list_a) - 1:
            combined_list.append(list_a[i])
        if i <= len(list_b) - 1:
            combined_list.append(list_b[i])

    return combined_list


print(combine_lists(['a', 'b', 'c'], [1, 2, 3]))
print(combine_lists(['a', 'b', 'c', 'd', 'e'], [1, 2, 3]))
print(combine_lists(['a', 'b', 'c'], [1, 2, 3, 4, 5]))


print('Q6. Write a function that computes the list of the first 100 Fibonacci numbers. The first two Fibonacci '
      'numbers are 1 and 1. The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci '
      'number. The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8. Test it in your program.')


def fibonacci(n):
    left = 1
    right = 1
    print(f'The first {n} fibonacci numbers are: ')
    print(left)
    print(right)
    for i in range(n-1):
        print(left + right)
        left, right = right, left + right


fibonacci(100)


print('Q7. Write a function that determines if a given year is a leap year. Test it in your program.')


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'The year {year} is a leap year!')
        return
    print(f'The year {year} is not a leap year!')


is_leap_year(1999)
is_leap_year(2016)
is_leap_year(1600)