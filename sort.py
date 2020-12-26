'''
#버블정렬
a = [7, 5, 4, 3]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

# 선택정렬
a = [5, 7, 4, 1, 2]
b = 0
for j in range(len(a)):
    b = j
    for i in range(j, len(a)):
        if a[i] < a[b]:
            b = i
    a[j], a[b] = a[b], a[j]
print(a)
'''
# 삽입정렬
a = [7, 4, 5, 1, 8, 2]
b = 1
for i in range(len(a)):
    b = i
    for j in range(i, len(a)):
        if a[b] > a[j]:
            b = j
    a[i], a[b] = a[b], a[i]
print(a)