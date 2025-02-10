def is_palindrome(n):
    return str(n) == str(n)[::-1]

with open(r"C:\Users\Marielle\Desktop\IT0011_TSA1-1\MIDTERM\numbers.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    numbers = list(map(int, filter(None, line.strip().split(','))))
    total = sum(numbers)
    result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
    print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")