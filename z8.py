x= int(input("Unesi broj od 1 do 1001: "))
import random
import statistics

if x < 0 or x > 1001:
    print("Unesena vrijednost nije između 0 i 1001.")

l= []
len(l) == x

for i in range(x):
    l.append(random.randint(0, 1001))
print("list:", l, sep="\n")

a= (statistics.median(l))
print("Medijan =", a)

b= statistics.mode(l)
print("Mode =", b)

c= statistics.mean(l)
print("Aritmetička sredina =", c)

print("Svi brojevi u listi ispred medijana su: ")
d= l.index(a)
e= []
e= l[0:d]
e= (" ".join(map(str, e)))
print(e)

print("Svi brojevi u listi manji od medijana su: ")
for i in range(0, a):
    if i in l:
        print(i)

f= a*0.1
g= a-f
h= a+f
l.append(g)
l.append(h)

ind1= l.index(g)
ind2= l.index(h)

i= []
i= l[:ind1] + l[ind2:]
print(i)