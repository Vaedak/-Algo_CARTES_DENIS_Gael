##Début du jeu de carte .

from ast import Pow
from re import M
from tokenize import ContStr
from unicodedata import name

## Définition de la classe parent Mage /

class Mage():
    def __init__(self,nom,pv,mana,main,defausse,terrain):
        self.__name = nom
        self.__hp = pv
        self.__mana = mana
        self.__hand = main
        self.__graveyard = defausse
        self.__terrain = terrain
    def getname(self):
        return self.__name
    def gethp(self):
        return self.__hp
    def getmana(self):
        return self.__mana
    def gethand(self):
        return self.__hand
    def getgraveyard(self):
        return self.__graveyard
    def getterrain(self):
        return self.__terrain

##Definition de l'ennemi /
class Mage2():
    def __init__(self,nom,pv,mana,main,defausse,terrain):
        self.__name = nom
        self.__hp = pv
        self.__mana = mana
        self.__hand = main
        self.__graveyard = defausse
        self.__terrain = terrain
    def getname(self):
        return self.__name
    def gethp(self):
        return self.__hp
    def getmana(self):
        return self.__mana
    def gethand(self):
        return self.__hand
    def getgraveyard(self):
        return self.__graveyard
    def getterrain(self):
        return self.__terrain

## Définition de la classe parent carte /


class Card():
    def __init__(self,nom,cout):
        self.__name = nom
        self.__cost = cout
    def getname(self):
        return self.__name
    def getcost(self):
        return self.__cost


## Définition de la classe enfant de carte et parent des cartes type blast /

class DAKKA(Card):
    def __init__ (self,nom,cout,effect,terrain):
        super(Card) .__init__ (self,nom,cout,effect)
        super(Mage) .__init__ (self,terrain)
        self.__name = nom
        self.__cost = cout
        self.__effect = effect
        self.__terrain = terrain
    def getname(self):
        return self.__name
    def getcost(self):
        return self.__cost
    def geteffect(self):
        return self.__effect
    def getterrain(self):
        self.__terrain = Mage.__terrain
    def useDAKKA(self):
        if Mage2.__terrain[2] == Nobz:
            Nobz.__endurance = Nobz.__endurance - 5
            print("machinegun noise")


##Définition de la classe enfant de carte de type creature,nobz /

class Nobz(Card):
    def __init__ (self,nom,cout,attaque,endurance):
        super(Card) .__init__ (self,nom,cout,attaque,endurance)
        self.__name = nom
        self.__cost = cout
        self.__attack = attaque
        self.__endurance = endurance
    def getname(self):
        return self.__name
    def getcost(self):
        return self.__cost
    def getattack(self):
        return self.__attack
    def getendurance(self):
        return self.__endurance 
    def printname(self):
        print(self.__name)

##Définition de la carte crystal "Powa'+" /

class Powaplus(Card):
    def __init__ (self,nom,cout,effect):
        super(Card) .__init__ (self,nom,cout,effect)
        self.__name = nom
        self.__cost = cout
        self.__effect = effect
    def getname(self):
        return self.__name
    def getcost(self):
        return self.__cost
    def geteffect(self):
        return self.__effect
    def printname(self):
        print(self.__name)

##input du nom du joueur, nombre de mana présent au début du tour du joueur /

print("Please enter your name :")
Mage.__name = input()
print("Wulcom' to da Waaaagh leada' Boss", Mage.__name ,".")
Mage.__mana = 8
print ("Y'have dat' much mana Boss:",Mage.__mana)

##Definit les attributs de Creature /

Nobz.__name = "Nobz"
Nobz.__cost = "4"
Nobz.__attack = "5"
Nobz.__endurance = "6"

##Definir les attributs de Powa'+ /

Powaplus.__name = "Powa'+"
Powaplus.__cost = 0
Powaplus.__effect = Mage.__mana = Mage.__mana + 1

DAKKA.__name = "Powa'+"
DAKKA.__cost = 0
DAKKA.__effect = Mage.__mana = Mage.__mana - 8
##Definir le contenu du terrain /

Mage2.__terrain =[]
Mage2.__terrain.append(Nobz)

##Definir le contenu de la main /

Mage.__hand = []
Mage.__hand.append(Powaplus.__name) 
Mage.__hand.append(Nobz.__name) 
Mage.__hand.append(Powaplus.__name) 
Mage.__hand.append(Nobz.__name)
Mage.__hand.append(Powaplus.__name)
print("Dit is ya' hand Boss", Mage.__hand)

print("Der is :", Mage2.__terrain ,"on da battlefiel' !")
