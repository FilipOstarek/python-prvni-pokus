import physics

volba = input("Zadejde číslo vaší volby\n"
              "1)Za jak dlouho urazí světlo metrů\n"
              "2)Kolik metrů urazí zvuk\n"
              "3)Kolik má těleso kg pokud je přitahováno na Zemi\n"
              "4)Kolik má těleso kg pokud je přitahováno na mesíci\n"
              ":")

if int(volba) <= 0 or int(volba) >= 5:
    volba = input("ŠPATNÉ ČÍSLO, zadejte prosím číslo vaší volby\n"
                  "1)Za jak dlouho urazí světlo metrů\n"
                  "2)Kolik metrů urazí zvuk\n"
                  "3)Kolik má těleso kg pokud je přitahováno na Zemi\n"
                  "4)Kolik má těleso kg pokud je přitahováno na mesíci\n"
                  ":")

if int(volba) == 1:
    cislo = input("Zadejte čas:")
    print("Světlo urazí " + str(physics.drahaS(int(cislo))) + " metrů")
if int(volba) == 2:
    cislo = input("Zadejte metry:")
    print("Zvuk se na určité místo mělo dostat za " + str(physics.drahaZ(int(cislo))) + " sekund")
if int(volba) == 3:
    cislo = input("Zadejte kg:")
    print("Síla přitahující věc na Zemi je " + str(physics.silaNaZemi(int(cislo))) + " N")
if int(volba) == 4:
    cislo = input("Zadejte kg:")
    print("Síla přitahující věc na měsící je " + str(physics.silaNaMesici(int(cislo))) + " N")


