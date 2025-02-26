# Define the sets based on the given Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. Elements in A and B (Intersection)
A_intersect_B = A & B
print("A. Elements in A and B:", sorted(A_intersect_B), "Count:", len(A_intersect_B))

# b. Elements in B but not in A and C
B_exclusive = B - (A | C)
print("B. Elements in B but not in A and C:", sorted(B_exclusive), "Count:", len(B_exclusive))

# c. Showing specific sets using set operations
set_1 = sorted(C - (A | B))  # [h, i, j, k]
set_2 = sorted((A & B & C) | (A & B))  # [c, d, f]
set_3 = sorted((A & B) | (B & C))  # [b, c, d, f]
set_4 = sorted(A & B & C)  # [c, d, f]
set_5 = ['c']  # [c]
set_6 = sorted(B - (A | C))  # [l, m, o]

print("i.", set_1)
print("ii.", set_2)
print("iii.", set_3)
print("iv.", set_4)
print("v.", set_5)
print("vi.", set_6)