print("Välkommen till hackerman kryptodomain")

meny = 0

while meny != 3:

    try:
        meny = int(input("Välj vad du vill kryptera: "))
    except:
            print("vÄLJ EN SIFFRA!!!")

    print("1. Kryptera")
    print("2. Dekryptera")
    print("3. Avsluta")
    
    letters = "Orvar"
    for l in letters:
        print(l)
        print(ord(l))

if meny == 1:
    letters = input("Skriv in vad du vill kryptera: ")
elif meny == 2:
    print("")
else meny == 3: 
    print("Leaving the cryptodomain")
    
