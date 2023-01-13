from random import randint as rand
import math


def MenuSelection(array):
	while True:
		
			
		listPrint(array)
		print("\n>>")
		choice = input()
		try:
			choice = int(choice)
			if(type(array) == dict):
				choice = list(array.keys())[choice]
			else:
				choice = array[choice]
		except:
			print("Bad stuff")
			print()
			continue
		break
	return choice

def listPrint(array, indent = False):
	if(type(array) == dict):
		for index, key in enumerate(array):
			print(str(index) + " = " + str(key))
			if (type(array[key]) == dict):
				listPrint(zip(list(array[key].keys()), list(array[key].values())), True)
			else:
				listPrint(array[key], True)
			print("\n")
	else:
		for index, item in enumerate(array):
			if type(item) != str and type(item) != int:
				temp = ""
				for x in item[:-1]:
					temp += str(x) + " -- "
				temp += str(item[len(item) - 1])
				item = temp
			print((str(index) + " = " + str(item)) if not indent else ("|>" + " " + str(item)) )
		


class Entity():
	def __init__(self):
		self.maxHp = 0
		self.hp = 0
		self.Maxmana = 0
		self.mana = 0
		self.critChance = 0
		self.critDamage = 0
	
	def __str__(self):
		return f"{self.hp} / {self.maxHp}"

class Player(Entity):
	def __init__(self, jem, startingClass: dict = {} ):

		super().__init__()


		#vals = list(startingClass.values())
		self.hpStat = jem
		self.memoryStat = jem
		self.strengthStat = jem
		self.visionStat = jem
		self.dexterityStat = jem
		self.arcaneStat = jem
		
		self.ReCalculateStats()

	

	def ReCalculateStats(self):
		initialise = False
		if (self.maxHp > 0):
			initialise = True
			hpRatio = (self.hp / self.maxHp)
			manaRatio = (self.mana / self.maxMana)
		
		self.maxHp = round(((10 + (math.log(self.hpStat + 3) - .5) * 6) + (self.hpStat/2)) * 10) # 0 = 136,   7 = 243,	20 = 358
		self.maxMana = round(((10 + (math.log(self.memoryStat + 3) - .5) * 6) + (self.hpStat/2)) * 5)
		self.critChance = round(((self.visionStat/5) + 2 ) * 10)
		self.critDamage = (round(math.log(self.dexterityStat, 10) * 1.2 + (self.dexterityStat/30), 2) if self.dexterityStat > 0 else 0) # Log returning strange result
		if self.critDamage < 1:
			self.critDamage = 1


		if (initialise):   
			self.hp = self.maxHp * hpRatio
			self.mana = self.maxMana * manaRatio




def MainMenu():
	print("Welome to RPG\nWhat is your Name?\n\n>>")
	playerName = input()
	print("What would you like your starting class to be?")

	########
	# Stats
	# Hp				-->	 Increases max hp
	# Memory			-->	 Increases max mana
	# Strength		  -->	 Increases damage of melee attacks
	# Vision			-->	 Increases critical hit chance
	# Dexterity		 -->	 Increases critical hit damage
	# Arcane			-->	 Increases magic effectiveness - Damage, status effects etc
	########

	# Each class should start off with 25 stat points allocated
	##### PUT THIS IS A JSON AT SOME POINT
	classes = {
		"Warrior":{
			"Hp": 7,
			"Memory": 2,
			"Strength": 7,
			"Vision": 3,
			"Dexterity": 4,
			"Arcane": 2
		},
		"Mage":{
			"Hp": 4,
			"Memory": 8,
			"Strength": 2,
			"Vision": 1,
			"Dexterity": 2,
			"Arcane": 8
		},
		"Thief":{
			"Hp": 5,
			"Memory": 1,
			"Strength": 6,
			"Vision": 6,
			"Dexterity": 6,
			"Arcane": 1
		}
	}

	
	# Warrior has raw stats
	# Mages can use magic
	# Thieves have a chance to avoid damage as well as enhanced crits
	
	SelectedClass = MenuSelection(classes)

	print("\n\n ~~Stats~~\n")
	for stat, val in zip(list(classes[SelectedClass].keys()), list(classes[SelectedClass].values())):
		print(str(stat) + " --> " + str(val))
	

for x in range(51):
   print(str(x) + " = " + str(Player(x).maxHp), end= "  ---  ")
   print(str(x) + " = " + str(Player(x).maxMana), end= "  ---  ")
   print(str(x) + " = " + str(Player(x).critChance), end= "  ---  ")
   print(str(x) + " = " + str(Player(x).critDamage), end= "  ---  ")
   print()


MainMenu()


