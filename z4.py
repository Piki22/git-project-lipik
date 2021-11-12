a, b = input("unesi 2 dvoznamenkasta broja i odvoji ih sa razmakom: ").split(" ")

a= int(a)
b= int(b)

if a > 99 or b > 99:
    print("Unio si broj sa više od 2 znamenke")
if a < 10 or b < 10:
        print("Unio si jednoznamenkast broj")
else:
    a= str(a)
    z= a
    b= str(b)
    
    a = b[1] 
    b = z[1]
    print(a, b, sep="\n")