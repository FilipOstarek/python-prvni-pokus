# coding=UTF-8
retezec = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
vysledek = []
komplet = []
kombinace = ()
def charFrequency(retezec):
    #print(retezec[0])
    #retezec = retezec[1:]
    #print(len(retezec))
    #print(retezec[93])
    for i in range(len(retezec)):
        #print(retezec[i])
        o = retezec[i]
        kombinace=(o, retezec.count(retezec[i]))
        vysledek.append(kombinace)
    for k in range(len(vysledek)):
        prvni = vysledek[k]
        for i in range(len(vysledek)):
            druhy = vysledek[i]
            if prvni == druhy and k != i:
                vysledek[i] = ''
    for i in range(len(vysledek)):
        if vysledek[i]!= '':
            komplet.append(vysledek[i])
    """
        for k in range(len(vysledek)):
            if kombinace != vysledek[k]:
                stop = False
                print("FALSE")
            if kombinace == vysledek[k]:
                stop = True
                print("TRUE")
            if stop == False:
                vysledek.append(kombinace)
    """
    komplet.sort(key=lambda item: item[1], reverse=True)
    for i in range(len(komplet)):
        print(komplet[i])
charFrequency(retezec)