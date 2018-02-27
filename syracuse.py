#/usr/bin/env python3
n =input("Choissisez un nombre de début: ")
n =int(n)
for i in range(10):
    if n%2 == 0:
        n=n/2
    else:
        n=n*3+1
    print(n)

