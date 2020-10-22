'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299796 #? rychlost světla ve vakuu m/s
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

def drahaS(s):
    '''
    Vypočítání dráhy světla v metrech
    '''
    return float(s*SPEED_OF_LIGHT)

def drahaZ(m):
    '''
    Vypočítání času uražení zvuku v sekundách
    '''
    return float(m/SPEED_OF_SOUND)

def silaNaZemi(kg):
    '''
    Vypočítání síly působící na těleso na Zemi
    '''
    return float(kg*EARTH_GRAVITY)

def silaNaMesici(kg):
    '''
    Vypočítání síly působící na těleso na měsící
    '''
    return float(kg*MOON_GRAVITY)

'''
import random
def roll_dice(num):
    return random.randint(1, num)
def greeting(name):
  return print("Hello, " + name)
'''
'''  
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
