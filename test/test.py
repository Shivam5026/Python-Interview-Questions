n = 256
k = 0
a = []

while n != 0:
    k += n % 10
    a.append(n % 10)
    n //= 10

a.sort()
b = 0  # Reset b before iteration

for i in a:
    b += i
    if b != k:
        print("python is fun")
    else:
        print("python is Boring")
