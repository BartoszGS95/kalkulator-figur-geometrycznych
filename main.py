import math
PI = math.pi

print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()

if inp == "a":
    print("ppBryl - a | vBryl - b")
    typ = input("inp: ").lower().strip()

    if typ == "a":
        print("ppSzecianu - a | ppProstopadloscianu - b | ppGraniastoslupa - c | ppOstroslupa - d | ppWalca - e | ppStozka - f | ppKuli - g")
        wybor = input("inp: ").lower().strip()

        if wybor == "a":
            a = float(input("a = "))
            print(f"ppSzecianu o boku {a} = {6 * a ** 2}")

        elif wybor == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu o bokach {a} {b} {c} = {2 * a * b + 2 * b * c + 2 * c * a}")

        elif wybor == "c":
            Pp = float(input("Pp = "))
            Pb = float(input("Pb = "))
            print(f"ppGraniastoslupa = {2 * Pp + Pb}")

        elif wybor == "d":
            Pp = float(input("Pp = "))
            Pb = float(input("Pb = "))
            print(f"ppOstroslupa = {Pp + Pb}")

        elif wybor == "e":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"ppWalca = {2 * PI * r ** 2 + 2 * PI * r * H}")

        elif wybor == "f":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"ppStozka = {PI * r ** 2 + PI * r * l}")

        elif wybor == "g":
            r = float(input("r = "))
            print(f"ppKuli = {4 * PI * r ** 2}")

        else:
            print("Nie ma takiej komendy")

    elif typ == "b":
        print("vSzecianu - a | vProstopadloscianu - b | vGraniastoslupa - c | vOstroslupa - d | vWalca - e | vStozka - f | vKuli - g")
        wybor = input("inp: ").lower().strip()

        if wybor == "a":
            a = float(input("a = "))
            print(f"vSzecianu o boku {a} = {a ** 3}")

        elif wybor == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"vProstopadloscianu o bokach {a} {b} {c} = {a * b * c}")

        elif wybor == "c":
            Pp = float(input("Pp = "))
            H = float(input("H = "))
            print(f"vGraniastoslupa = {Pp * H}")

        elif wybor == "d":
            Pp = float(input("Pp = "))
            H = float(input("H = "))
            print(f"vOstroslupa = {(1 / 3) * Pp * H}")

        elif wybor == "e":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"vWalca = {PI * r ** 2 * H}")

        elif wybor == "f":
            r = float(input("r = "))
            H = float(input("H = "))
            print(f"vStozka = {(1 / 3) * PI * r ** 2 * H}")

        elif wybor == "g":
            r = float(input("r = "))
            print(f"vKuli = {(4 / 3) * PI * r ** 3}")

        else:
            print("Nie ma takiej komendy")

    else:
        print("Nie ma takiej komendy")

elif inp == "b":
    print("obwody fig plaskich - a | pp fig plaskich - b")
    typ = input("inp: ").lower().strip()

    if typ == "a":
        print("obwodKwadratu - a | obwodProstokata - b | obwodTrojkata - c | obwodRownolegloboku - d | obwodTrapezu - e | obwodTrojkatarownoboczenego - f | obwodKola - g | obwodRombu - h")
        wybor = input("inp: ").lower().strip()

        if wybor == "a":
            a = float(input("a = "))
            print(f"Obwod kwadratu = {4 * a}")
        elif wybor == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"Obwod prostokata = {2 * (a + b)}")
        elif wybor == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"Obwod trojkata = {a + b + c}")
        elif wybor == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"Obwod rownolegloboku = {2 * a + 2 * b}")
        elif wybor == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"Obwod trapezu = {a + b + c + d}")
        elif wybor == "f":
            a = float(input("a = "))
            print(f"Obwod trojkatarownoboczengo = {3 * a}")
        elif wybor == "g":
            r = float(input("r = "))
            print(f"Obwod kola = {2 * PI * r}")
        elif wybor == "h":
            a = float(input("a = "))
            print(f"Obwod rombu = {4 * a}")
        else:
            print("Nie ma takiej komendy")

    elif typ == "b":
        print("ppKwadratu - a | ppProstokata - b | ppTrojkata - c | ppKola - d | ppRownolegloboku - e | ppTrapezu - f | ppRombu - g | ppTrojkatarownoboczenego - h")
        wybor = input("inp: ").lower().strip()

        if wybor == "a":
            a = float(input("a = "))
            print(f"ppKwadratu o boku {a} = {a ** 2}")
        elif wybor == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"ppProstokata o bokach {a} {b} = {a * b}")
        elif wybor == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppTrojkata = {0.5 * a * h}")
        elif wybor == "d":
            r = float(input("r = "))
            print(f"ppKola = {PI * r ** 2}")
        elif wybor == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppRownolegloboku = {a * h}")
        elif wybor == "f":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"ppTrapezu = {0.5 * (a + b) * h}")
        elif wybor == "g":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"ppRombu = {e * f / 2}")
        elif wybor == "h":
            a = float(input("a = "))
            print(f"ppTrojkatarownobocznego = {a ** 2 * math.sqrt(3) / 4}")
        else:
            print("Nie ma takiej komendy")
    else:
        print("Nie ma takiej komendy")

else:
    print("Nie ma takiej komendy")


