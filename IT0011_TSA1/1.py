def count_chars(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    v_count = c_count = space_count = other_count = 0

    for char in s:
        if char in vowels:
            v_count += 1
        elif char in consonants:
            c_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")
    print(f"Spaces: {space_count}")
    print(f"Other Characters: {other_count}")

input_str = input("Enter a string: ")
count_chars(input_str)
