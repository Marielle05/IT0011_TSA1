def pattern_while(n):
    i = 1
    while i <= n:
        if i % 2 == 1:
            print(str(i) * i)
        i += 1

pattern_while(7)