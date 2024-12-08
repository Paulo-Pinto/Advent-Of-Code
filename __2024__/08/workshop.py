# 1, 8 x 2, 5 -> 0, 11 ; 3, 2
a = (1, 8)
b = (2, 5)

# 2, 5 x 3, 7 -> 1,  3 ; 4, 9
# a = (2,5)
# b = (3,7)


# r for row, c for col
diff_r = abs(a[0] - b[0])
diff_c = abs(a[1] - b[1])

a_r, a_c, b_r, b_c = 0, 0, 0, 0

# TODO : Is there a way to abstract this conditional ?

if a[0] < b[0]:
    a_r = min(a[0], b[0]) - diff_r
    b_r = max(a[0], b[0]) + diff_r
else:
    a_r = max(a[0], b[0]) + diff_r
    b_r = min(a[0], b[0]) - diff_r

if a[1] < b[1]:
    a_c = min(a[1], b[1]) - diff_c
    b_c = max(a[1], b[1]) + diff_c
else:
    a_c = max(a[1], b[1]) + diff_c
    b_c = min(a[1], b[1]) - diff_c

print((a, b), " -> ", (a_r, a_c), (b_r, b_c))
