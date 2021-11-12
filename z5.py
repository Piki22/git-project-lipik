a, b, c, d, e, f, g, h = input("unesi 8 racionalnih brojeva i odvoji ih sa razmakom: ").split(" ")

a= float(a)
b= float(b)
c= float(c)
d= float(d)
e= float(e)
f= float(f)
g= float(g)
h= float(h)

x = a + b / c * d**e // f - g % h 
print (x)

#Sve funkcionira eventualno ako neki broj bude 
#prevelik ("e" I'm looking at you) izbacuje OverflowError
#i naravno ako dijelimo s 0 bude ZeroDivisionError