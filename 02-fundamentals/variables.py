'''
Proměnné v Pythonu
Python je typově odvozovaný jazyk, proto nemusíme explicitně definovat typ proměnné.
Typ proměnné je určen na základě přiřazené hodnoty.
Pro přiřazení hodnoty proměnné se používá znak rovnítko ("=").
'''

# Proměnné v Pythonu - primitivní datové typy
# Je zvykem používat podtržítko u víceslovných názvů proměnných.
students_count = 1000
rating = 4.99
# Hodnota může být přiřazena i více proměnným najednou:
x = y = z = 0

# Boolean hodnota musí začínat velkým písmenem
is_published = False

# Python obsahuje i speciální literál None - nulovou hodnotu
iq = None
# print('Jeho IQ = ', iq)

'''
V Pythonu se ale ve skutečnosti nepřiřazují do proměnných hodnoty, ale jen reference na objekt (hodnotu).
Každý objekt (instance třídy) má jedinečnou hodnotu (value), typ (type) a identitu (ID).
Proto i typy proměnných poukazují na určitou výchozí třídu, z níž byl objekt vytvořen. 
Identita objektu je vyjádřena jeho identifikačním číslem (ID), které je adresou paměťového místa, ve kterém je hodnota uložena. 
Některé objekty mohou mít explicitně přiřazené jméno, obecně označované jako proměnná:
'''

'''Úkol A'''
#? Najděte na Internetu, jakými funkcemi lze v Pythonu zjistit
#? a) typ objektu
#? b) identitu objektu (jeho adresu v paměti)
#? Ukažte to na příkladech proměnných students_count, rating, is_published a vypište výstupy do konzole
print("TYP OBEKTU")
print(type(students_count))
print(type(rating))
print(type(is_published))
print("ID")
print(id(students_count))
print(id(rating))
print(id(is_published))

# Numerické operátory
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# Zbytek po celočíselném dělení
# print(10 % 3)
# Celočíselné dělení
# print(10 // 3)
# Mocnina
# print(2 ** 10)

'''
Příklady použití numerických literálů (numeric literals)
'''
binary = 0b1010 #Binary Literals
octal = 0o310 #Octal Literal
decimal = 100 #Decimal Literal
hexadecimal = 0x12c #Hexadecimal Literal

# print(binary, octal, decimal, hexadecimal)
# Převod desítkového čísla na binární, oktalové a hexadecimální
# print(bin(255), oct(255), hex(255))


# Převod binárního čísla na desítkové
# print(int('0100', base=2))
# Převod hexadecimálního čísla na desítkové
# print(int('100', base=16))


'''Úkol B'''
#? Vypište do poznámky všechny bitové operátory, které nabízí Python
#? Do proměnné myself_binary uložte binární číslo vytvořené na základě osmi prvních znaků z vašeho jména a příjmení (souhláska = 1, samohláska 0)
#? Příklad - HildaDok: 10110101
#? Vypište toto binární číslo v desítkové soustavě
#? Pro toto binární číslo proveďte nejprve bitový posun o 2 bity vpravo, poté vypište výsledek v desítkové soustavě
#? Proveďte bitový součin hexadecimálního čísla "1A" a vašeho binárního čísla a opět vypište v desítkové soustavě
#? Výsledek zobrazte jako formátovaný řetězec - např. "Binární součin čísla 0b11010 a 0b10110101 je 0b10000"
'''
>>
<<
&
|
~ alt126
^
'''
print("\nUKOL B\n")
cislo = 0
myself_binary = 10101111
myself_binary2 = 0
print(myself_binary)
#převedení z bin na desítkovou soustavu
def preved(bin):
    desitky = 1
    nasobky = 1
    cislo2 = 0
    bin = int(bin)
    while bin > desitky:
        desitky *= 10
        nasobky *= 2
        #print(desitky)
        #print(nasobky)
    if desitky > bin and nasobky > 1:
       nasobky /=2
       desitky /=10
    while desitky != -1:
        #print(cislo2)
        if (bin > desitky) and (desitky != -1):
            bin -= desitky
            cislo2 += nasobky
            #print(nasobky)
            #print(cislo2)
        if nasobky > 1:
            nasobky /= 2
        #print(desitky)
        if desitky == 0:
            return cislo2
        if desitky != 1:
            desitky /= 10
        else:
            desitky -=1
            #print(desitky)

print(int(preved(myself_binary)))
print(int(preved(myself_binary)) >> 2)
'''
       1010 1111
  1A =    1 1010
  --------------
       0000 0000
     1 0101 1110 - (o jednu 0 navíc)
  ---------------
     1 0101 1110 - první výsledek
    00 0000 0000 - (o 2 0 navíc)
  ---------------
     1 0101 1110 - druhý védledek
   101 0111 1000 - (o 3 0 navíc)
  --------------
   110 1101 0110 - třetí výsledek
  1010 1111 0000 - (o 4 0 navíc)
  --------------
1 0001 1100 0110 - finální výsledek xd
nope nope nope 
'''
#print("1A")
#print(preved(11010))
soucet = int(preved(11010)) * int(preved(myself_binary))
print(soucet)

def prevedDES (des):
    nasobky = 1
    desitky = 1
    bin = 0
    while des > nasobky:
        nasobky *= 2
        desitky *=10
        #print(nasobky)
    if des > nasobky:
        nasobky /= 2
        desitky /=10
    while nasobky >= 1:
        if des - nasobky >= 0:
            des -= nasobky
            bin += desitky
            #print(bin)
            #print(des)
        nasobky /= 2
        desitky /= 10
    if nasobky < 1:
        return bin
#print(int(prevedDES(soucet)))
print("Binární součin čísla "+ str(myself_binary) +" a 11010 je "+ str(int(prevedDES(soucet))))





'''
if myself_binary >=10000000:
    cislo += 128
    myself_binary -=10000000
if myself_binary >= 1000000:
    cislo += 64
    myself_binary -=1000000
if myself_binary >= 100000:
    cislo += 32
    myself_binary -=100000
if myself_binary >= 10000:
    cislo += 16
    myself_binary -=10000
if myself_binary >= 1000:
    cislo += 8
    myself_binary -=1000
if myself_binary >= 100:
    cislo += 4
    myself_binary -=100
if myself_binary >= 10:
    cislo += 2
    myself_binary -=10
if myself_binary >= 1:
    cislo += 1
    myself_binary -=1
print(cislo)
myself_binary2 = cislo >> 2
print(myself_binary2)
'''


'''Python plně podporuje operace v plovoucí řádové čárce (tj. desetinná čísla). 
Operátor pracující s různými typy operandů si nejprve zkonvertuje celá čísla na čísla 
v plovoucí řádové čárce a následně provede výpočet (obdobné chování jako v jazyce C).
Výsledek je vždy desetinné číslo.
'''
#Float Literal
float_1 = 10.5
float_2 = 1.5e2 # Zápis reálného čísla pomocí exponentu = 1.5 * (10 ** 2)
#print(float_1 + float_2)


# Použití vestavěných matematických funkcí
# print(round(rating))
# Použití importovaného modulu math a jeho metod
# print(math.floor(rating))
# print(math.cos(45))

# Zjištění datového typu
# x = input("x: ")
# Vrátí typ str - proto je nutná typová konverze - int(), float()
# Typová konverze
# print(int(x) + 20)

# Komplexní čísla a Python
'''Python plně podporuje komplexní čísla, přičemž imaginární číslo je zapisováno s příponou "j" nebo "J". 
Komplexní čísla zapisujeme ve tvaru "(Re + Imj)" nebo je můžeme vytvořit pomocí interní funkce "complex(Re, Im)":
'''
#Complex Literal
complex = 3.14j

'''Komplexní čísla jsou vždy reprezentována dvojicí desetinných čísel, reálnou a imaginární částí. 
Chceme-li získat velikosti těchto částí čísla z, použijeme zápisu z.real a z.imag:'''
# z = 4.5 + 0.5j
# print(z, z.imag, z.real)

'''Poněvadž v matematice neexistuje způsob, jak převést komplexní číslo na reálné, 
ani Python nedovoluje použití konverzních funkcí float(), int() a long() s komplexním argumentem. 
Raději použijte funkci abs(z) pro získání absolutní hodnoty komplexního čísla, 
nebo zápis z.real reprezentují reálnou část čísla: 
'''
# Následující řádek vyvolá chybu
# print(float(z))
#
# print(abs(z))
# Je totéž jako sqrt(z.real**2 + z.imag**2)

'''
Funguje pouze  v interaktivní konzoli!
Speciální proměnná _ reprezentuje předešlý výsledek.

>>> urok = 12.5 / 100
>>> penize = 100.50
>>> penize * urok
12.5625
>>> penize + _
113.0625
>>> round(_, 2)
113.06
>>>

Varování: Hodnota proměnné _ by nikdy neměla být modifikována uživatelem. 
Pokud byste jí přiřadili hodnotu, vytvořili byste nezávislou lokální proměnnou se stejným jménem, 
která by zakryla interní proměnnou s tímto chováním.'''


