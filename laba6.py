####### 1 ########
print(len(set(input().split())))

####### 2 ########
print(len(set(input().split()) & set(input().split())))

####### 3 ########
n = int(input())
A = set()
for i in range(n):
    S = input().split()
    for elem in S:
        A.add(elem)
print(len(A))

####### 4 ########
lang = []
union = set()
all = set()
for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)}
    all.update(a)
    if i == 1:
        union.update(a)
    else:
        union &= a
print(len(union))
print('\n'.join(sorted(union)))
print(len(all))
print('\n'.join(sorted(all)))

####### 5 ########
