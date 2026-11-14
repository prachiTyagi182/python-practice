n = 5


for i in range(1, n + 1):  # Row 1 se 5 tak
    for j in range(i):     # Har row me 'i' baar star print hoga
        print("*", end=" ")
    print()                # Nayi line par jaane ke liye
    n = 5

for i in range(n, 0, -1):  # Loop 5 se 1 tak ulta chalega
    for j in range(i):     # Har row me 'i' baar star print hoga
        print("*", end=" ")
    print()                # Nayi line par jaane ke liye