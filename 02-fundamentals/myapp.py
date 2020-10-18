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
    physics.drahaS(int(cislo))
if int(volba) == 2:
    cislo = input("Zadejte metry:")
    physics.drahaZ(int(cislo))
if int(volba) == 3:
    cislo = input("Zadejte kg:")
    physics.silaNaZemi(int(cislo))
if int(volba) == 4:
    cislo = input("Zadejte kg:")
    physics.silaNaMesici(int(cislo))


