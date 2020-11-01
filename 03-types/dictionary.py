'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Sbírka, která je neuspořádaná, proměnlivá a indexovaná.
# V Pythonu jsou slovníky psány složenými závorkami a obsahují klíče a hodnoty.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

pomlky = '--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
mezera = ' '
mezery = mezera*20
filmy = {
  'Halloween Returns': {
    'žánr': 'horror',
    'tržby': {5876500000, 'Kč'},
    'premiéra': [8, 'září', 2018],
    'inspirováno_knihou': False,
    'herci': ('Jamie Lee Curtis', 'Judy Greer', 'Andi Matichak'),
    'délka_minuty': 106
  },
  'Mama Mia': {
    'žánr': 'komedie',
    'tržby': {14027700000000,'Kč'},
    'premiéra': [30, 'června', 2008],
    'inspirováno_knihou': True,
    'herci': ('Meryl Streep', 'Amanda Seyfried', 'Pierce Brosnan'),
    'délka_minuty': 108
  },
  'Jurský park': {
    'žánr': 'sci-fi thriller',
    'tržby': {23000000000,'Kč'},
    'premiéra': ['X', 'X', 1993],
    'inspirováno_knihou': True,
    'herci': ('Sam Neill','Laura Dern', 'Richard Attenborough'),
    'délka_minuty': 127
  }
}
del filmy['Jurský park']['premiéra']
#print(filmy['Jurský park'])
filmy['Jurský park']['premiéra'] = ['9', 'června', 1993]
#print(filmy['Jurský park'])
#print(str(len(filmy["Mama Mia"]["herci"][2])))
print(str(len(mezery)))
#MAX = 45
print(f'Filmy \n'+pomlky+'\nNázev\žánr'+mezery+'tržby'+mezery+'premiéra'+mezery+'inspirováno_knihou'+mezery+'délka_minuty'+mezery+'herci\n'+pomlky)
i = 0
for i in range(3):
  if i == 0:
    i = "Jurský park"
    print(i+f'\{filmy[i]["žánr"]}'+mezera*3+f'{filmy[i]["tržby"]}'+mezera*6+f'{filmy[i]["premiéra"]}'+mezera*7+f'{filmy[i]["inspirováno_knihou"]}'+mezera*34+f'{filmy[i]["délka_minuty"]}'+mezera*29+f'{filmy[i]["herci"]}')
  if i == 1:
    i = "Mama Mia"
    print(i+f'\{filmy[i]["žánr"]}'+mezera*14+f'{filmy[i]["tržby"]}'+mezera*3+f'{filmy[i]["premiéra"]}'+mezera*8+f'{filmy[i]["inspirováno_knihou"]}'+mezera*34+f'{filmy[i]["délka_minuty"]}'+mezera*29+f'{filmy[i]["herci"]}')
  if i == 2:
    i = "Halloween Returns"
    print(i+f'\{filmy[i]["žánr"]}'+mezera*6+f'{filmy[i]["tržby"]}'+mezera*7+f'{filmy[i]["premiéra"]}'+mezera*11+f'{filmy[i]["inspirováno_knihou"]}'+mezera*33+f'{filmy[i]["délka_minuty"]}'+mezera*29+f'{filmy[i]["herci"]}')