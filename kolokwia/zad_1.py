T = ["ABCABCABCABCABC", "AAAA", "ASDHASDJAHSIUSHJDHJSBFKBAF"]
list_1 = []

x = 0

for i in T:
    for j in range(len(i)):
        if i[0] == i[j]:
            while x < j: