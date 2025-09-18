a, b = map(int, input().split())

#Bitwise Operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a |b)
print("Bitwise NOT:", ~a)
print("Bitwise XOR:", a ^ b)
print("Bitwise Left Shift:", a << 2)
print("Bitwise Right Shift:", a >> 2)
print("Bitwise AND:", b & a)
print("Bitwise OR:", b | a)
print("Bitwise NOT:", ~b)
print("Bitwise XOR:", b ^ a)
print("Bitwise Left Shift:", b << 2)
print("Bitwise Right Shift:", b >> 2)

#Membership Operators
list1 = [1, 2, 3, 4, 5]
print("Membership in list:", a in list1)
print("Membership not in list:", a not in list1)
print("Membership in list:", b in list1)
print("Membership not in list:", b not in list1)

#Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("Identity is:", x is z)
print("Identity is not:", x is not y)
print("Identity is:", x is y)
print("Identity is not:", x is not z)
print("Identity is:", y is z)
print("Identity is not:", y is not z)