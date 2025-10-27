A = int(input("bilangan 1: "))
B = int(input("bilangan 2: "))
C = int(input("bilangan 3: "))
D = int(input("bilangan 4: "))

# carilah bilangan terbesar dari empat bilangan tersebut 

if A >= B and A >= C and A>= D:
    print("1 bilangan terbesar")
elif B >= A and B >= C and B >= D:
    print("2 bilangan terbesar")
elif C >= A and C >= B and C>= D:
    print("3 bilangan terbesar")
else:
    print("4 bilangan terbesar")