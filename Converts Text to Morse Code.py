print("This program will convert your message into morse code.\n")
message = input("Enter your message here: ")
messageLower = message.lower()
length = len(messageLower)
number = 0
lst = []
lst2 = []
lst2.extend(messageLower)
a = "._"
b = "_..."
c = "_._."
d = "_.."
e = "."
f = ".._."
g = "_ _."
h = "...."
i = ".."
j = "._ _ _"
k = "_._"
l = "._.."
m = "_ _"
n = "_."
o = "_ _ _"
p = "._ _."
q = "_ _._"
r = "._."
s = "..."
t = "_"
u = ".._"
v = "..._"
w = "._ _"
x = "_.._"
y = "_._ _"
z = "_ _.."
n0 = "_ _ _ _ _"
n1 = "._ _ _ _"
n2 = ".._ _ _"
n3 = "..._ _"
n4 = "...._"
n5 = "....."
n6 = "_...."
n7 = "_ _..."
n8 = "_ _ _.."
n9 = "_ _ _ _."
space = "/"
for index in range(0, length):
    if lst2[number] == "a":
        number += 1
        lst.append(a)
    elif lst2[number] == "b":
        number += 1
        lst.append(b)
    elif lst2[number] == "c":
        number += 1
        lst.append(c)
    elif lst2[number] == "d":
        number += 1
        lst.append(d)
    elif lst2[number] == "e":
        number += 1
        lst.append(e)
    elif lst2[number] == "f":
        number += 1
        lst.append(f)
    elif lst2[number] == "g":
        number += 1
        lst.append(g)
    elif lst2[number] == "h":
        number += 1
        lst.append(h)
    elif lst2[number] == "i":
        number += 1
        lst.append(i)
    elif lst2[number] == "j":
        number += 1
        lst.append(j)
    elif lst2[number] == "k":
        number += 1
        lst.append(k)
    elif lst2[number] == "l":
        number += 1
        lst.append(l)
    elif lst2[number] == "m":
        number += 1
        lst.append(m)
    elif lst2[number] == "n":
        number += 1
        lst.append(n)
    elif lst2[number] == "o":
        number += 1
        lst.append(o)
    elif lst2[number] == "p":
        number += 1
        lst.append(p)
    elif lst2[number] == "q":
        number += 1
        lst.append(q)
    elif lst2[number] == "r":
        number += 1
        lst.append(r)
    elif lst2[number] == "s":
        number += 1
        lst.append(s)
    elif lst2[number] == "t":
        number += 1
        lst.append(t)
    elif lst2[number] == "u":
        number += 1
        lst.append(u)
    elif lst2[number] == "v":
        number += 1
        lst.append(v)
    elif lst2[number] == "w":
        number += 1
        lst.append(w)
    elif lst2[number] == "x":
        number += 1
        lst.append(x)
    elif lst2[number] == "y":
        number += 1
        lst.append(y)
    elif lst2[number] == "z":
        number += 1
        lst.append(z)
    elif lst2[number] == "0":
        number += 1
        lst.append(n0)
    elif lst2[number] == "1":
        number += 1
        lst.append(n1)
    elif lst2[number] == "2":
        number += 1
        lst.append(n2)
    elif lst2[number] == "3":
        number += 1
        lst.append(n3)
    elif lst2[number] == "4":
        number += 1
        lst.append(n4)
    elif lst2[number] == "5":
        number += 1
        lst.append(n5)
    elif lst2[number] == "6":
        number += 1
        lst.append(n6)
    elif lst2[number] == "7":
        number += 1
        lst.append(n7)
    elif lst2[number] == "8":
        number += 1
        lst.append(n8)
    elif lst2[number] == "9":
        number += 1
        lst.append(n9)
    elif lst2[number] == " ":
        number += 1
        lst.append(space)
    print("LOADING...")
"""messageT = str(lst2)
messageT2 = messageT.replace("'", "")
messageT3 = messageT2.replace(",", "")
messageT4 = messageT3.replace("[", "")
messageT5 = messageT4.replace("]", "")
print(messageT5)"""
code = str(lst)
code2 = code.replace("'", "")
code3 = code2.replace(",", "")
code4 = code3.replace("[", "")
code5 = code4.replace("]", "")
print(code5)

