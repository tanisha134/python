Wr = open("tanisha.html","w")

Wr.write("<h1>Hello everyone, how are you all</h1>")

Wr.write("<p>Hello everyone, how are you all</p>")

Wr1 = open("tanisha.txt","w")

Wr1.write("tumi kemon acho\n")

Wr2 = open("tanisha.txt","a")

Wr2.write("tumi kemon acho\n")
Wr2.write("tumi ki ghost\n")
Wr2.write("hello world\n")
Wr2.write("happy\n")

Wr2 = open("tanisha.txt","r")

print(Wr2.read())
