# Define the sets based on the given Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. Elements in A and B (Intersection)
A_intersect_B = A & B
print("Elements in A and B:", A_intersect_B, "Count:", len(A_intersect_B))

# b. Elements in B but not in A and C
B_exclusive = B - (A | C)
print("Elements in B but not in A and C:", B_exclusive, "Count:", len(B_exclusive))

# c. Showing specific sets using set operations
set_1 = C - (A | B)  # {h, i, j, k}
set_2 = (A & B & C) | (A & B)  # {c, d, f}
set_3 = (A & B) | (B & C)  # {b, c, h}
set_4 = A & B & C  # {d, f}
set_5 = {'c'}  # {c}
set_6 = B - (A | C)  # {l, m, o}

print("Set [h, i, j, k]:", set_1)
print("Set [c, d, f]:", set_2)
print("Set [b, c, h]:", set_3)
print("Set [d, f]:", set_4)
print("Set [c]:", set_5)
print("Set [l, m, o]:", set_6)