import datetime
pomlka= "-"

class CASY:
    MAX = 1000
    MIN = 0
    def __init__(self, mes, den, hod, min, sek):
        try:
            if(hod <= CASY.MAX and min <= CASY.MAX and sek <= CASY.MAX and mes <= CASY.MAX and den <= CASY.MAX and hod >= CASY.MIN and min >= CASY.MIN and sek >= CASY.MIN and mes >= CASY.MIN and den >= CASY.MIN):
                self.mes = int(mes)
                self.den = int(den)
                self.hod = int(hod)
                self.min = int(min)
                self.sek = int(sek)
                self.existujeR = False
            else: ValueError("Nebyly zadany spravne hodnoty")
        except: ValueError("Nebylo zadano cislo")

    def __str__(self):  #string
        return f'({self.mes} mesic/e, {self.den} den/dny, {self.hod} hodina/y, {self.min} minuta/y, {self.sek} sekunda/y)'
    def __eq__(prvni, druhy):  #equal
        return ((prvni.sek + prvni.min * 60 + prvni.hod * 3600 + prvni.den * 86400 + prvni.mes * 2592000) == (druhy.sek + druhy.min * 60 + druhy.hod * 3600 + druhy.den * 86400 + druhy.mes * 2592000))
    def __gt__(prvni, druhy):  #greater than
        return ((prvni.sek + prvni.min * 60 + prvni.hod * 3600 + prvni.den * 86400 + prvni.mes * 2592000) > (druhy.sek + druhy.min * 60 + druhy.hod * 3600 + druhy.den * 86400 + druhy.mes * 2592000))
    def __lt__(prvni, druhy):   #less than
        return ((prvni.sek + prvni.min * 60 + prvni.hod * 3600 + prvni.den * 86400 + prvni.mes * 2592000) < (druhy.sek + druhy.min * 60 + druhy.hod * 3600 + druhy.den * 86400 + druhy.mes * 2592000))
    def __add__(prvni, druhy):   #add
        casP = CASY(prvni.mes + druhy.mes, prvni.den + druhy.den,prvni.hod + druhy.hod, prvni.min + druhy.min, prvni.sek + druhy.sek)
        CASY.pretoceni(casP)
        return casP
    def __sub__(prvni, druhy):   #substrack
        if (((prvni.mes >= druhy.mes) == False)):
            print("Byly pretoceny strany argumentu - aby vyraz neskoncil v negaci (duvod: mesic)")
        if (((prvni.mes == druhy.mes) and (prvni.den >= druhy.den) == False)):
            print("Byly pretoceny strany argumentu - aby vyraz neskoncil v negaci (duvod: dny)")
        if (((prvni.mes == druhy.mes) and (prvni.den == druhy.den) and (prvni.hod >= druhy.hod) == False)):
            print("Byly pretoceny strany argumentu - aby vyraz neskoncil v negaci (duvod: hodiny)")
        if (((prvni.mes == druhy.mes) and (prvni.den == druhy.den) and (prvni.hod == druhy.hod) and (prvni.min >= druhy.min) == False)):
            print("Byly pretoceny strany argumentu - aby vyraz neskoncil v negaci (duvod: minuty)")
        if ((prvni.mes == druhy.mes) and (prvni.den == druhy.den) and (prvni.hod == druhy.hod) and (prvni.min == druhy.min) and (prvni.sek >= druhy.sek)):
            print("Byly pretoceny strany argumentu - aby vyraz neskoncil v negaci (duvod: sekundy)")
        casP = CASY(abs(prvni.mes - druhy.mes), abs(prvni.den - druhy.den), abs(prvni.hod - druhy.hod), abs(prvni.min - druhy.min), abs(prvni.sek - druhy.sek))
        CASY.pretoceni(casP)
        return casP

    @property
    def existujeR(self):
        return self.__existujeR

    @existujeR.setter
    def existujeR(self, __existujeR):
        radic = True
        if (self.mes > 365):
            self.__existujeR = radic

    def pretoceni(casP):
        while (casP.sek >= 60):
            casP.sek -= 60
            casP.min += 1
        while (casP.min >= 60):
            casP.min -= 60
            casP.hod += 1
        while (casP.hod >= 24):
            casP.hod -= 24
            casP.den += 1
        while (casP.den >= 30): #budeme dělat ze jeden mesic ma 30 dni prozatim
            casP.den -= 30
            casP.mes += 1

    @classmethod
    def zmena(cls, novMAX):
        cls.MAX = novMAX

class esceLepsiCASY(CASY):
    lunarni_rok = ""
    def __init__(self, rok, mes, den, hod, min, sek):
        try:
            if(mes <= CASY.MAX and hod <= CASY.MAX and min <= CASY.MAX and sek <= CASY.MAX and rok <= CASY.MAX and den <= CASY.MAX and hod >= CASY.MIN and min >= CASY.MIN and sek >= CASY.MIN and rok >= CASY.MIN and den >= CASY.MIN and mes >= CASY.MIN):
                self.rok = int(rok)
                self.mes = int(mes)
                self.den = int(den)
                self.hod = int(hod)
                self.min = int(min)
                self.sek = int(sek)
                self.prestupnyR = False
            else: ValueError("Nebyly zadany spravne hodnoty")
        except: ValueError("Nebylo zadano cislo")

    def pretoceni(casP):
        while (casP.sek >= 60):
            casP.sek -= 60
            casP.min += 1
        while (casP.min >= 60):
            casP.min -= 60
            casP.hod += 1
        while (casP.hod >= 24):
            casP.hod -= 24
            casP.den += 1
        while (casP.den >= 30): #budeme dělat ze jeden mesic ma 30 dni prozatim
            casP.den -= 30
            casP.mes += 1
        while (casP.mes >= 13):
            casP.mes -= 13
            casP.rok += 1

    def lunar(self):
        casP = self
        esceLepsiCASY.pretoceni(casP)
        pocetniRok = 1912
        while pocetniRok < casP.rok:
            pocetniRok += 12
        cisloZvire = pocetniRok - casP.rok
        if cisloZvire == 0:
            self.lunarni_rok = "Krysy"
        if cisloZvire == 1:
            self.lunarni_rok = "Buvola"
        if cisloZvire == 2:
            self.lunarni_rok = "Tygra"
        if cisloZvire == 3:
            self.lunarni_rok = "Zajice"
        if cisloZvire == 4:
            self.lunarni_rok = "Draka"
        if cisloZvire == 5:
            self.lunarni_rok = "Hada"
        if cisloZvire == 6:
            self.lunarni_rok = "Kone"
        if cisloZvire == 7:
            self.lunarni_rok = "Kozy"
        if cisloZvire == 8:
            self.lunarni_rok = "Opice"
        if cisloZvire == 9:
            self.lunarni_rok = "Kohout"
        if cisloZvire == 10:
            self.lunarni_rok = "Psa"
        if cisloZvire == 11:
            self.lunarni_rok = "Vepre"
        #print(cisloZvire)


    @staticmethod
    def prestupnyRok():
        datum = datetime.datetime.now()
        datumm = str(datum).replace('.', ' ').replace(':', ' ').replace('-', ' ')
        rok = str(datumm)[0:4]
        #print(rok)
        if (int(rok) % 4 == 0 or int(rok) % 400 == 0):
            print(rok + " je prestupny rok !!!")
        else: print(rok + "neni prestupny rok :(")


bod1 = CASY(26,0,1,2,5)
bod2 = CASY(400,100,3,5,6)
print(pomlka * 30+ "\nVYPSANI HODNOT\n" + pomlka * 30)
print(bod1)
print(bod2)
print(pomlka * 30+ "\nZMENA\n" + pomlka * 30)
print("Stara hodnota MAX = " + str(CASY.MAX))
CASY.zmena(5000)
print("Nova hodnota MAX = " + str(CASY.MAX))
print(pomlka * 30+ "\nMATEMATICKE FUNKCE\n" + pomlka * 30)
print("-")
print(bod1 - bod2)
print("+")
print(bod1 + bod2)
print("==")
print(bod1 == bod2)
print("<")
print(bod1 < bod2)
print(">")
print(bod1 > bod2)

print(pomlka * 30+ "\nPRESTUPNY ROK\n" + pomlka * 30)

print("Existuje rok v tomto casovem obdobi ? = " + str(bod2.existujeR))
#print("\n Prestupny rok = " + str(bod2.prestupnyRok()))
bod3 = esceLepsiCASY(2020,5,4,8,2,1)

esceLepsiCASY.prestupnyRok()
bod3.lunar()
print(pomlka * 30+ "\nLUNARNI ROK\n" + pomlka * 30)
print("Rok " + str(bod3.rok) +" je rok " + bod3.lunarni_rok)