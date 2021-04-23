# Micro RPG text-based game
import random
charStrenght = 0
charSpeed = 0
monsterStrenght = 0
monsterSpeed = 0
charHP = 0
monsterHP = 0
charAttack = 0
monsterAttack = 0
def fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed):
	charHP = 50
	monsterHP = 50
	charPower = 0
	charHits = 0
	avgCharPower = 0
	monsterHits = 0
	monsterPower = 0
	avgMonsterPower = 0
	while charHP or monsterHP <= 0:
		charAttack = random.randint(1, 3)
		charSpeed = random.randint(1,5)
		charAS = charAttack + charSpeed
		monsterAttack = random.randint(1, 3)
		monsterSpeed = random.randint(1,5)
		monsterAS = monsterAttack + monsterSpeed	
		if monsterAttack == charAttack:
			print(f'You and monster landed {charAttack} attack power. ')
		if charAS > monsterAS:
			charHits = charHits + 1
			charPower = charPower + charAttack
			monsterHP = monsterHP - charAttack
			print(f'You hit the monster with {charAttack}.\nMonster have {monsterHP} HP ')
			if monsterHP <= 0:
				avgCharPower = charPower / charHits
				avgCP = "{:.2f}".format(avgCharPower)
				print(f'Congratulations! You win the battle\nYou landed {charHits} hits. Average power {avgCP} ')
				break
		elif charAS < monsterAS:
			monsterHits = monsterHits + 1
			monsterPower = monsterPower + monsterAttack
			charHP = charHP - monsterAttack
			print(f'You try to hit monster with {charAttack}, but monster strikes you back with {monsterAttack}\nYou have {charHP} HP')
			if charHP <= 0:
				avgMonsterPower = monsterPower / monsterHits
				avgMP = "{:.2f}".format(avgMonsterPower)
				print(f'You lost the battle!\nMonster landed {monsterHits}. Average power {avgMP}')
				break
fight(charStrenght, charSpeed,monsterStrenght,monsterSpeed)
