x= int(input("Unesi nasumičan broj između 0 i 101: "))
import math

y= x / 2
y= round(y)
z= y / (2*math.pi)

if x < 0 or x > 101:
    print("Unesena vrijednost nije između 0 i 101.")
else:
    print(f"vrijednost polumjera kruga iznosi {z}.")
