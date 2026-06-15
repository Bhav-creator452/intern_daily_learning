# string type hinting
def even_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = int(input("Enter a number: "))
result = even_odd(number)
print(result)

# float type hinting
def larger_number(num1: float, num2: float) -> str:
    if num1 > num2:
        return f"The larger number is: {num1}"
    else:
        return f"The larger number is: {num2}"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = larger_number(num1, num2)
print(result)

# int type hinting
def count_vowels(word: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input("Enter a word: ")
result = count_vowels(word)
print(f"The number of vowels in '{word}' is: {result}")


#tuple type hinting
def min_max(numbers: tuple) -> tuple:
    if not numbers:
        return None, None
    min_num = min(numbers)
    max_num = max(numbers)
    return min_num, max_num

numbers = tuple(map(float, input("Enter numbers separated by space: ").split()))
result = min_max(numbers)
print(f"The minimum number is: {result[0]}, The maximum number is: {result[1]}")