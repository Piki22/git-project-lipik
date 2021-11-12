a, b = input("unesi 2 broja i odvoji ih sa razmakom: ").split(" ")

a= int(a)
b= int(b)

if a != b:
    if a < b:
        print(f"Broj {a} je manji od broja {b}")
    elif a > b:
        print(f"Broj {a} je veći od {b}")


if a <= b:
    if a >= b:
        if a == b:
            print(f"Broj {a} je jednak broju {b}")